#!/usr/bin/env python3
"""
Nerd Font v2 → v3 Codepoint Migration Script for logo-ls.

This script:
1. Downloads Nerd Font CSS files (v2.3.3 and v3 master)
2. Parses icon name→codepoint mappings
3. Builds old→new translation table for MDI icons (nf-mdi-* → nf-md-*)
4. Validates non-MDI codepoints against v3 master
5. Patches iconsMap.go and formatterStuff.go with updated codepoints
6. Generates a migration report

Usage:
    python3 migrate_nf_v3.py --dry-run   # Preview changes
    python3 migrate_nf_v3.py             # Apply changes
"""

import argparse
import os
import re
import shutil
import sys
import urllib.request
from collections import defaultdict

# --- Configuration ---

V2_CSS_URL = "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v2.3.3/css/nerd-fonts-generated.css"
V3_CSS_URL = "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/master/css/nerd-fonts-generated.css"

ICONS_MAP_FILE = "assets/iconsMap.go"
FORMATTER_FILE = "internal/dir/formatterStuff.go"

# MDI range in Nerd Font v2: F500–FD46
MDI_RANGE_START = 0xF500
MDI_RANGE_END = 0xFD46

# Codepoints that are literal ASCII characters (not icon glyphs)
ASCII_LITERALS = set(ord(c) for c in "FZhJD")

# Manual overrides for icons whose names changed between nf-mdi-* and nf-md-*
# These can't be auto-matched by name alone.
# Format: old_codepoint → (new_codepoint, description)
MANUAL_OVERRIDES = {
    0xF853: (0xF0354, "markdown → language_markdown"),
    0xF72D: (0xF05C0, "file_xml → xml"),
    0xF724: (0xF0226, "file_pdf → file_pdf_box"),
    0xF820: (0xF0320, "language_python_text → language_python"),
    0xF831: (0xF0331, "library_books → library"),
    0xF822: (0xF0322, "laptop_chromebook → laptop"),
    0xFB75: (0xF075A, "itunes → music"),
    0xFB72: (0xF0673, "xaml → language_xaml"),
    0xF719: (0xF0219, "file_document_box → file_document"),
    0xFD03: (0xF0805, "azure → microsoft_azure"),
    0xFB25: (0xF0626, "json → code_json"),
}


def download_css(url, cache_name):
    """Download a CSS file, caching locally."""
    cache_path = f".nf_cache_{cache_name}.css"
    if os.path.exists(cache_path):
        print(f"  Using cached {cache_path}")
        with open(cache_path, "r", encoding="utf-8") as f:
            return f.read()

    print(f"  Downloading {url} ...")
    req = urllib.request.Request(url, headers={"User-Agent": "migrate_nf_v3/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read().decode("utf-8")

    with open(cache_path, "w", encoding="utf-8") as f:
        f.write(data)
    print(f"  Saved to {cache_path} ({len(data)} bytes)")
    return data


def parse_css(css_text):
    """
    Parse nerd-fonts-generated.css to extract icon mappings.
    Returns: dict of {prefix: {name: codepoint_int}}
    e.g. {"mdi": {"android": 0xF531}, "md": {"android": 0xF0065}}
    """
    # Pattern: .nf-{prefix}-{name}:before { content: "\{hex}"; }
    # Also handles .nf-{prefix}-{name}:before{content:"\{hex}"}  (minified)
    pattern = re.compile(
        r'\.nf-([a-zA-Z0-9]+)-([a-zA-Z0-9_-]+):before\s*\{\s*content:\s*"\\([0-9a-fA-F]+)";\s*\}'
    )

    result = defaultdict(dict)
    for match in pattern.finditer(css_text):
        prefix = match.group(1)
        name = match.group(2)
        codepoint = int(match.group(3), 16)
        result[prefix][name] = codepoint

    return dict(result)


def build_mdi_translation(v2_css_map):
    """
    Build old→new codepoint translation from v2.3.3 CSS.
    The v2.3.3 CSS contains BOTH nf-mdi-* (old) and nf-md-* (new) entries.
    """
    old_mdi = v2_css_map.get("mdi", {})
    new_md = v2_css_map.get("md", {})

    # Build: old_codepoint → (new_codepoint, icon_name)
    translation = {}
    unmapped_names = []
    ambiguous = []

    for name, old_cp in old_mdi.items():
        if name in new_md:
            new_cp = new_md[name]
            if old_cp in translation and translation[old_cp] != (new_cp, name):
                # Same old codepoint maps to different new ones — ambiguous
                ambiguous.append((name, old_cp, new_cp, translation[old_cp]))
            translation[old_cp] = (new_cp, name)
        else:
            unmapped_names.append((name, old_cp))

    # Merge in manual overrides for renamed icons
    for old_cp, (new_cp, desc) in MANUAL_OVERRIDES.items():
        if old_cp not in translation:
            translation[old_cp] = (new_cp, desc)
            # Remove from unmapped if present
            unmapped_names = [(n, c) for n, c in unmapped_names if c != old_cp]

    return translation, unmapped_names, ambiguous


def build_v3_all_codepoints(v3_css_map):
    """Build a set of all codepoints present in v3 CSS."""
    all_cps = set()
    for prefix_map in v3_css_map.values():
        all_cps.update(prefix_map.values())
    return all_cps


def build_v3_reverse_lookup(v3_css_map):
    """Build codepoint → (prefix, name) lookup from v3 CSS."""
    reverse = {}
    for prefix, names in v3_css_map.items():
        for name, cp in names.items():
            reverse[cp] = (prefix, name)
    return reverse


def format_go_codepoint(cp):
    """Format a codepoint as a Go string escape."""
    if cp <= 0xFFFF:
        return f"\\u{cp:04x}"
    else:
        return f"\\U{cp:08x}"


def extract_go_codepoints(line):
    """
    Extract codepoint escape sequences from a Go source line.
    Returns list of (match_text, codepoint_int, start_pos, end_pos).
    """
    results = []
    # Match \uXXXX (4 hex digits) or \UXXXXXXXX (8 hex digits)
    for m in re.finditer(r'\\[uU]([0-9a-fA-F]{4,8})', line):
        hex_str = m.group(1)
        cp = int(hex_str, 16)
        results.append((m.group(0), cp, m.start(), m.end()))
    return results


def patch_icons_map(content, translation, v3_all_cps, v3_reverse):
    """
    Patch iconsMap.go content. Returns (new_content, changes_list).
    changes_list: [(line_num, icon_name, old_cp, new_cp, action)]
    """
    lines = content.split("\n")
    changes = []
    skipped = []
    unmapped = []
    validated = []

    new_lines = []
    for line_num, line in enumerate(lines, 1):
        codepoints = extract_go_codepoints(line)
        if not codepoints:
            new_lines.append(line)
            continue

        # Try to extract icon name from comment at end of line
        comment_match = re.search(r'//\s*(.+?)(?:\s*\(Not supported.*\))?\s*$', line)
        icon_name = comment_match.group(1).strip() if comment_match else "unknown"

        new_line = line
        offset = 0  # Track character offset from replacements

        for match_text, cp, start, end in codepoints:
            # Skip ASCII literal characters
            if cp in ASCII_LITERALS:
                skipped.append((line_num, icon_name, cp, "ASCII literal"))
                continue

            if MDI_RANGE_START <= cp <= MDI_RANGE_END:
                # MDI range — needs translation
                if cp in translation:
                    new_cp, mdi_name = translation[cp]
                    new_escape = format_go_codepoint(new_cp)
                    adj_start = start + offset
                    adj_end = end + offset
                    new_line = new_line[:adj_start] + new_escape + new_line[adj_end:]
                    offset += len(new_escape) - (end - start)
                    changes.append((line_num, icon_name, cp, new_cp, f"migrated (mdi: {mdi_name})"))
                else:
                    unmapped.append((line_num, icon_name, cp, "in MDI range but no mapping found"))
            else:
                # Non-MDI — validate against v3
                if cp in v3_all_cps:
                    v3_info = v3_reverse.get(cp, ("?", "?"))
                    validated.append((line_num, icon_name, cp, f"confirmed in v3 ({v3_info[0]}-{v3_info[1]})"))
                else:
                    # Check if this is a very low codepoint (likely a different icon set)
                    # or custom. Still flag it.
                    unmapped.append((line_num, icon_name, cp, "NOT found in v3 CSS"))

        new_lines.append(new_line)

    return "\n".join(new_lines), changes, skipped, unmapped, validated


def patch_formatter(content, translation):
    """
    Patch formatterStuff.go — update hardcoded "\uf723" comparison.
    """
    changes = []

    # Find the specific comparison: i.GetGlyph() == "\uf723"
    # 0xf723 is in the MDI range
    old_cp = 0xF723
    if old_cp in translation:
        new_cp, mdi_name = translation[old_cp]
        old_escape = format_go_codepoint(old_cp)
        new_escape = format_go_codepoint(new_cp)
        if old_escape in content:
            content = content.replace(f'"{old_escape}"', f'"{new_escape}"')
            changes.append((163, "file icon comparison", old_cp, new_cp, f"migrated (mdi: {mdi_name})"))
        else:
            changes.append((163, "file icon comparison", old_cp, None, "escape not found in file"))
    else:
        changes.append((163, "file icon comparison", old_cp, None, "no mapping for 0xF723"))

    return content, changes


def generate_report(
    mdi_translation, unmapped_mdi_names, ambiguous_mdi,
    icon_changes, icon_skipped, icon_unmapped, icon_validated,
    formatter_changes,
    dry_run
):
    """Generate migration_report.md."""
    lines = []
    lines.append("# Nerd Font v2 → v3 Migration Report\n")
    lines.append(f"**Mode**: {'DRY RUN (no files modified)' if dry_run else 'APPLIED'}\n")

    # Summary
    lines.append("## Summary\n")
    lines.append(f"- MDI translation table entries: {len(mdi_translation)}")
    lines.append(f"- Unmapped MDI icon names: {len(unmapped_mdi_names)}")
    lines.append(f"- Ambiguous MDI mappings: {len(ambiguous_mdi)}")
    lines.append(f"- Icons migrated in iconsMap.go: {len(icon_changes)}")
    lines.append(f"- Icons skipped (ASCII literals): {len(icon_skipped)}")
    lines.append(f"- Icons unmapped/missing: {len(icon_unmapped)}")
    lines.append(f"- Non-MDI icons validated in v3: {len(icon_validated)}")
    lines.append(f"- formatterStuff.go changes: {len(formatter_changes)}")
    lines.append("")

    # Migrated icons
    lines.append("## Migrated Icons (iconsMap.go)\n")
    lines.append("| Line | Icon Name | Old Codepoint | New Codepoint | Action |")
    lines.append("|------|-----------|---------------|---------------|--------|")
    for line_num, name, old_cp, new_cp, action in icon_changes:
        lines.append(f"| {line_num} | {name} | U+{old_cp:04X} | U+{new_cp:04X} | {action} |")
    lines.append("")

    # Validated (non-MDI, confirmed in v3)
    lines.append("## Validated Non-MDI Icons\n")
    lines.append("| Line | Icon Name | Codepoint | Status |")
    lines.append("|------|-----------|-----------|--------|")
    for line_num, name, cp, status in icon_validated:
        lines.append(f"| {line_num} | {name} | U+{cp:04X} | {status} |")
    lines.append("")

    # Skipped
    if icon_skipped:
        lines.append("## Skipped (ASCII Literals)\n")
        lines.append("| Line | Icon Name | Char | Reason |")
        lines.append("|------|-----------|------|--------|")
        for line_num, name, cp, reason in icon_skipped:
            lines.append(f"| {line_num} | {name} | {chr(cp)} (U+{cp:04X}) | {reason} |")
        lines.append("")

    # Unmapped
    if icon_unmapped:
        lines.append("## ⚠ Unmapped / Missing Icons (NEEDS MANUAL REVIEW)\n")
        lines.append("| Line | Icon Name | Codepoint | Issue |")
        lines.append("|------|-----------|-----------|-------|")
        for line_num, name, cp, issue in icon_unmapped:
            lines.append(f"| {line_num} | {name} | U+{cp:04X} | {issue} |")
        lines.append("")

    # Ambiguous MDI
    if ambiguous_mdi:
        lines.append("## ⚠ Ambiguous MDI Mappings\n")
        for name, old_cp, new_cp, existing in ambiguous_mdi:
            lines.append(f"- `{name}`: U+{old_cp:04X} → U+{new_cp:04X} (conflicts with {existing})")
        lines.append("")

    # Formatter changes
    lines.append("## formatterStuff.go Changes\n")
    for line_num, name, old_cp, new_cp, action in formatter_changes:
        if new_cp:
            lines.append(f"- Line {line_num}: `{name}` U+{old_cp:04X} → U+{new_cp:04X} ({action})")
        else:
            lines.append(f"- Line {line_num}: `{name}` U+{old_cp:04X} — {action}")
    lines.append("")

    # Reminders
    lines.append("## Post-Migration Reminders\n")
    lines.append("1. Run `go build ./...` to verify all escape sequences are valid Go")
    lines.append("2. Regenerate ALL test snapshots: `go test ./... -update`")
    lines.append("3. Run `go test ./...` to verify tests pass")
    lines.append("4. Review any unmapped/missing icons above for manual fixes")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Migrate Nerd Font v2→v3 codepoints in logo-ls")
    parser.add_argument("--dry-run", action="store_true", help="Generate report without modifying files")
    args = parser.parse_args()

    # Ensure we're in the right directory
    if not os.path.exists(ICONS_MAP_FILE):
        print(f"Error: {ICONS_MAP_FILE} not found. Run this script from the logo-ls root directory.")
        sys.exit(1)

    # Step 1: Download CSS files
    print("Step 1: Downloading CSS files...")
    v2_css = download_css(V2_CSS_URL, "v2")
    v3_css = download_css(V3_CSS_URL, "v3")

    # Step 2: Parse CSS
    print("Step 2: Parsing CSS files...")
    v2_map = parse_css(v2_css)
    v3_map = parse_css(v3_css)

    print(f"  v2.3.3 prefixes: {sorted(v2_map.keys())}")
    for prefix, names in sorted(v2_map.items()):
        print(f"    nf-{prefix}-*: {len(names)} icons")

    print(f"  v3 master prefixes: {sorted(v3_map.keys())}")
    for prefix, names in sorted(v3_map.items()):
        print(f"    nf-{prefix}-*: {len(names)} icons")

    # Step 3: Build MDI translation table
    print("Step 3: Building MDI translation table...")
    mdi_translation, unmapped_mdi_names, ambiguous_mdi = build_mdi_translation(v2_map)
    print(f"  Translation entries: {len(mdi_translation)}")
    print(f"  Unmapped MDI names: {len(unmapped_mdi_names)}")
    print(f"  Ambiguous: {len(ambiguous_mdi)}")

    # Step 4: Build v3 validation data
    print("Step 4: Building v3 validation data...")
    v3_all_cps = build_v3_all_codepoints(v3_map)
    v3_reverse = build_v3_reverse_lookup(v3_map)
    print(f"  Total v3 codepoints: {len(v3_all_cps)}")

    # Step 5: Read and patch source files
    print("Step 5: Patching source files...")

    with open(ICONS_MAP_FILE, "r", encoding="utf-8") as f:
        icons_content = f.read()

    with open(FORMATTER_FILE, "r", encoding="utf-8") as f:
        formatter_content = f.read()

    new_icons, icon_changes, icon_skipped, icon_unmapped, icon_validated = patch_icons_map(
        icons_content, mdi_translation, v3_all_cps, v3_reverse
    )

    new_formatter, formatter_changes = patch_formatter(formatter_content, mdi_translation)

    # Step 6: Generate report
    print("Step 6: Generating report...")
    report = generate_report(
        mdi_translation, unmapped_mdi_names, ambiguous_mdi,
        icon_changes, icon_skipped, icon_unmapped, icon_validated,
        formatter_changes,
        args.dry_run
    )

    report_path = "migration_report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"  Report written to {report_path}")

    # Step 7: Apply changes (unless dry-run)
    if args.dry_run:
        print("\n=== DRY RUN — no files modified ===")
        print(f"  Would migrate {len(icon_changes)} icons in {ICONS_MAP_FILE}")
        print(f"  Would update {len(formatter_changes)} entries in {FORMATTER_FILE}")
        print(f"  Review {report_path} for details")
    else:
        # Create backups
        backup_icons = ICONS_MAP_FILE + ".bak"
        backup_formatter = FORMATTER_FILE + ".bak"
        shutil.copy2(ICONS_MAP_FILE, backup_icons)
        shutil.copy2(FORMATTER_FILE, backup_formatter)
        print(f"  Backed up {ICONS_MAP_FILE} → {backup_icons}")
        print(f"  Backed up {FORMATTER_FILE} → {backup_formatter}")

        # Write patched files
        with open(ICONS_MAP_FILE, "w", encoding="utf-8") as f:
            f.write(new_icons)
        print(f"  Wrote {ICONS_MAP_FILE} ({len(icon_changes)} changes)")

        with open(FORMATTER_FILE, "w", encoding="utf-8") as f:
            f.write(new_formatter)
        print(f"  Wrote {FORMATTER_FILE} ({len(formatter_changes)} changes)")

        print(f"\n=== Migration complete ===")
        print(f"  Review {report_path} for details")
        print(f"  Next: go build ./... && go test ./... -update && go test ./...")


if __name__ == "__main__":
    main()
