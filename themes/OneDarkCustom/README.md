# OneDarkCustom GTK Theme

A custom GTK theme based on your One Dark terminal color palette.

## Color Palette

| Role       | Color     |
|------------|-----------|
| Background | `#1E222A` |
| Foreground | `#ABB2BF` |
| Red        | `#E06C75` |
| Green      | `#7EC7A2` |
| Yellow     | `#EBCB8B` |
| Blue       | `#61AFEF` |
| Purple     | `#C678DD` |
| Cyan       | `#6D8DAD` |

Blue (`#61AFEF`) is used as the accent color throughout the theme.

## Installation

### Linux (GNOME / GTK-based desktops)

1. Copy the theme folder to your local themes directory:

   ```bash
   mkdir -p ~/.themes
   cp -r OneDarkCustom ~/.themes/
   ```

2. Apply the theme using GNOME Tweaks, or from the terminal:

   ```bash
   # GTK 3 apps
   gsettings set org.gnome.desktop.interface gtk-theme "OneDarkCustom"

   # If on GNOME 42+ with libadwaita, GTK 4 apps may need:
   mkdir -p ~/.config/gtk-4.0
   ln -sf ~/.themes/OneDarkCustom/gtk-4.0/gtk.css ~/.config/gtk-4.0/gtk.css
   ```

3. Log out and back in, or restart your apps to see the changes.

### Flatpak Apps

Flatpak apps may not pick up user themes automatically. You can override:

```bash
sudo flatpak override --filesystem=~/.themes
sudo flatpak override --env=GTK_THEME=OneDarkCustom
```

## GTK 2 Note

The GTK 2 theme uses the **Murrine** engine. Install it if you haven't:

- **Debian/Ubuntu:** `sudo apt install gtk2-engines-murrine`
- **Fedora:** `sudo dnf install gtk-murrine-engine`
- **Arch:** `sudo pacman -S gtk-engine-murrine`

## Customization

All colors are defined as variables at the top of each CSS file (`@define-color`),
making it easy to adjust the palette to your liking. Edit the files in:

- `gtk-3.0/gtk.css` — GTK 3 applications
- `gtk-4.0/gtk.css` — GTK 4 / libadwaita applications
- `gtk-2.0/gtkrc` — Legacy GTK 2 applications

## Libadwaita Note

Apps built with libadwaita (GNOME 42+) use their own styling and may ignore GTK themes.
The symlink method above partially works, but some elements may still use Adwaita defaults.
For full libadwaita theming, consider tools like `gradience` to override the color palette.
