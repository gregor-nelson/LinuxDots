# Nerd Font v2 → v3 Migration Report

**Mode**: APPLIED

## Summary

- MDI translation table entries: 1950
- Unmapped MDI icon names: 169
- Ambiguous MDI mappings: 0
- Icons migrated in iconsMap.go: 117
- Icons skipped (ASCII literals): 0
- Icons unmapped/missing: 0
- Non-MDI icons validated in v3: 117
- formatterStuff.go changes: 1

## Migrated Icons (iconsMap.go)

| Line | Icon Name | Old Codepoint | New Codepoint | Action |
|------|-----------|---------------|---------------|--------|
| 32 | markdown | U+F853 | U+F0354 | migrated (mdi: markdown → language_markdown) |
| 33 | css | U+F81B | U+F031C | migrated (mdi: language_css3) |
| 39 | xml | U+F72D | U+F05C0 | migrated (mdi: file_xml → xml) |
| 40 | image | U+F71E | U+F021F | migrated (mdi: file_image) |
| 43 | test-jsx | U+F595 | U+F0096 | migrated (mdi: flask_outline) |
| 44 | test-js | U+F595 | U+F0096 | migrated (mdi: flask_outline) |
| 49 | typescript-def | U+FBE4 | U+F06E6 | migrated (mdi: language_typescript) |
| 50 | test-ts | U+F595 | U+F0096 | migrated (mdi: flask_outline) |
| 51 | pdf | U+F724 | U+F0226 | migrated (mdi: file_pdf → file_pdf_box) |
| 52 | table | U+F71A | U+F021B | migrated (mdi: file_excel) |
| 58 | csharp | U+F81A | U+F031B | migrated (mdi: language_csharp) |
| 61 | java | U+F675 | U+F0176 | migrated (mdi: coffee) |
| 62 | c | U+FB70 | U+F0671 | migrated (mdi: language_c) |
| 63 | cpp | U+FB71 | U+F0672 | migrated (mdi: language_cpp) |
| 64 | go | U+FCD1 | U+F07D3 | migrated (mdi: language_go) |
| 65 | go-mod | U+FCD1 | U+F07D3 | migrated (mdi: language_go) |
| 66 | go-test | U+FCD1 | U+F07D3 | migrated (mdi: language_go) |
| 67 | python | U+F81F | U+F0320 | migrated (mdi: language_python) |
| 68 | python-misc | U+F820 | U+F0320 | migrated (mdi: language_python_text → language_python) |
| 69 | url | U+F836 | U+F0337 | migrated (mdi: link) |
| 70 | console | U+F68C | U+F018D | migrated (mdi: console) |
| 71 | word | U+F72B | U+F022C | migrated (mdi: file_word) |
| 72 | certificate | U+F623 | U+F0124 | migrated (mdi: certificate) |
| 73 | key | U+F805 | U+F0306 | migrated (mdi: key) |
| 75 | lib | U+F831 | U+F0331 | migrated (mdi: library_books → library) |
| 79 | swift | U+FBE3 | U+F06E5 | migrated (mdi: language_swift) |
| 81 | powerpoint | U+F726 | U+F0227 | migrated (mdi: file_powerpoint) |
| 82 | video | U+F72A | U+F022B | migrated (mdi: file_video) |
| 83 | virtual | U+F822 | U+F0322 | migrated (mdi: laptop_chromebook → laptop) |
| 84 | email | U+F6ED | U+F01EE | migrated (mdi: email) |
| 85 | audio | U+FB75 | U+F075A | migrated (mdi: itunes → music) |
| 86 | coffee | U+F675 | U+F0176 | migrated (mdi: coffee) |
| 87 | document | U+F718 | U+F0219 | migrated (mdi: file_document) |
| 90 | xaml | U+FB72 | U+F0673 | migrated (mdi: xaml → language_xaml) |
| 96 | r | U+FCD2 | U+F07D4 | migrated (mdi: language_r) |
| 98 | mxml | U+F72D | U+F05C0 | migrated (mdi: file_xml → xml) |
| 100 | vue | U+FD42 | U+F0844 | migrated (mdi: vuejs) |
| 101 | vue-config | U+FD42 | U+F0844 | migrated (mdi: vuejs) |
| 102 | lock | U+F83D | U+F033E | migrated (mdi: lock) |
| 110 | smarty | U+F834 | U+F0335 | migrated (mdi: lightbulb) |
| 112 | verilog | U+FB19 | U+F061A | migrated (mdi: chip) |
| 113 | robot | U+FBA7 | U+F06A9 | migrated (mdi: robot) |
| 114 | solidity | U+FCB9 | U+F07BB | migrated (mdi: currency_eth) |
| 115 | yang | U+FB7E | U+F0680 | migrated (mdi: yin_yang) |
| 118 | cake | U+F5EA | U+F00EB | migrated (mdi: cake_variant) |
| 119 | nim | U+F6A4 | U+F01A5 | migrated (mdi: crown) |
| 123 | webpack | U+FC29 | U+F072B | migrated (mdi: webpack) |
| 126 | nodejs | U+F898 | U+F0399 | migrated (mdi: nodejs) |
| 128 | yarn | U+F61A | U+F011B | migrated (mdi: cat) |
| 129 | android | U+F531 | U+F0032 | migrated (mdi: android) |
| 130 | tune | U+FB69 | U+F066A | migrated (mdi: tune_vertical) |
| 131 | contributing | U+F64D | U+F014D | migrated (mdi: clipboard_text) |
| 132 | readme | U+F7FB | U+F02FC | migrated (mdi: information) |
| 133 | changelog | U+FBA6 | U+F099B | migrated (mdi: restore) |
| 134 | credits | U+F75F | U+F0260 | migrated (mdi: format_align_center) |
| 142 | conduct | U+F64B | U+F014E | migrated (mdi: clipboard_check) |
| 144 | code-climate | U+F7F4 | U+F0509 | migrated (mdi: image_filter_hdr) |
| 145 | log | U+F719 | U+F0219 | migrated (mdi: file_document_box → file_document) |
| 149 | makefile | U+F728 | U+F0229 | migrated (mdi: file_presentation_box) |
| 152 | mdx | U+F853 | U+F0354 | migrated (mdi: markdown → language_markdown) |
| 154 | azure | U+FD03 | U+F0805 | migrated (mdi: azure → microsoft_azure) |
| 155 | razor | U+F564 | U+F0065 | migrated (mdi: at) |
| 156 | asciidoc | U+F718 | U+F0219 | migrated (mdi: file_document) |
| 157 | edge | U+F564 | U+F0065 | migrated (mdi: at) |
| 158 | scheme | U+FB26 | U+F0627 | migrated (mdi: lambda) |
| 160 | svg | U+FC1F | U+F0721 | migrated (mdi: svg) |
| 163 | codeowners | U+F507 | U+F0008 | migrated (mdi: account_check) |
| 166 | tcl | U+FBD1 | U+F06D3 | migrated (mdi: feather) |
| 169 | husky | U+F8E8 | U+F03E9 | migrated (mdi: paw) |
| 170 | coconut | U+F5D2 | U+F00D3 | migrated (mdi: bowling) |
| 171 | sketch | U+F6C7 | U+F0B8A | migrated (mdi: diamond) |
| 173 | commitlint | U+FC16 | U+F0718 | migrated (mdi: source_commit) |
| 175 | dune | U+F7F4 | U+F0509 | migrated (mdi: image_filter_hdr) |
| 176 | shaderlab | U+FBAD | U+F06AF | migrated (mdi: unity) |
| 177 | command | U+FB32 | U+F0633 | migrated (mdi: apple_keyboard_command) |
| 180 | roadmap | U+FB6D | U+F066E | migrated (mdi: chart_timeline) |
| 195 | routing | U+FB40 | U+F0641 | migrated (mdi: directions_fork) |
| 198 | blink (The Foundry Nuke) | U+F72A | U+F022B | migrated (mdi: file_video) |
| 199 | postcss | U+F81B | U+F031C | migrated (mdi: language_css3) |
| 205 | vala | U+F7AB | U+F02AC | migrated (mdi: gnome) |
| 209 | powershell | U+FCB5 | U+F07B7 | migrated (mdi: console_line) |
| 210 | gradle | U+FCC4 | U+F07C6 | migrated (mdi: elephant) |
| 212 | tex | U+F783 | U+F0284 | migrated (mdi: format_text) |
| 215 | actionscript | U+FB25 | U+F0626 | migrated (mdi: json → code_json) |
| 216 | autohotkey | U+F812 | U+F0313 | migrated (mdi: keyboard_variant) |
| 217 | flash | U+F740 | U+F0241 | migrated (mdi: flash) |
| 218 | swc | U+FBD3 | U+F06D5 | migrated (mdi: flash_outline) |
| 223 | puppet | U+F595 | U+F0096 | migrated (mdi: flask_outline) |
| 224 | purescript | U+F670 | U+F0171 | migrated (mdi: code_not_equal_variant) |
| 230 | babel | U+F5A0 | U+F00A1 | migrated (mdi: beta) |
| 233 | eslint | U+FBF6 | U+F06F8 | migrated (mdi: nut) |
| 234 | mocha | U+F6A9 | U+F01AA | migrated (mdi: cup) |
| 236 | stylelint | U+FB76 | U+F0678 | migrated (mdi: bow_tie) |
| 237 | prettier | U+F8E2 | U+F03E3 | migrated (mdi: parking) |
| 239 | storybook | U+FD2C | U+F082E | migrated (mdi: notebook) |
| 240 | fastlane | U+FBFF | U+F0700 | migrated (mdi: pentagon_outline) |
| 241 | helm | U+FD31 | U+F0833 | migrated (mdi: ship_wheel) |
| 242 | i18n | U+F7BE | U+F02BF | migrated (mdi: google_translate) |
| 243 | semantic-release | U+F70F | U+F0210 | migrated (mdi: fan) |
| 244 | godot | U+FBA7 | U+F06A9 | migrated (mdi: robot) |
| 245 | godot-assets | U+FBA7 | U+F06A9 | migrated (mdi: robot) |
| 247 | tailwindcss | U+FC8B | U+F078D | migrated (mdi: waves) |
| 248 | gcp | U+F662 | U+F0163 | migrated (mdi: cloud_outline) |
| 250 | pascal | U+F8DA | U+F03DB | migrated (mdi: pandora) |
| 342 | dir-include | U+F756 | U+F0257 | migrated (mdi: folder_plus) |
| 343 | dir-import | U+F756 | U+F0257 | migrated (mdi: folder_plus) |
| 344 | dir-upload | U+F758 | U+F0259 | migrated (mdi: folder_upload) |
| 345 | dir-download | U+F74C | U+F024D | migrated (mdi: folder_download) |
| 346 | dir-secure | U+F74F | U+F0250 | migrated (mdi: folder_lock) |
| 347 | dir-images | U+F74E | U+F024F | migrated (mdi: folder_image) |
| 348 | dir-environment | U+F74E | U+F024F | migrated (mdi: folder_image) |
| 353 | unknown | U+F74A | U+F024B | migrated (mdi: folder) |
| 354 | unknown | U+FC6E | U+F0770 | migrated (mdi: folder_open) |
| 355 | unknown | U+F755 | U+F0256 | migrated (mdi: folder_outline) |
| 356 | unknown | U+F713 | U+F0214 | migrated (mdi: file) |
| 357 | unknown | U+F723 | U+F0224 | migrated (mdi: file_outline) |
| 358 | unknown | U+FB12 | U+F0613 | migrated (mdi: file_hidden) |

## Validated Non-MDI Icons

| Line | Icon Name | Codepoint | Status |
|------|-----------|-----------|--------|
| 31 | html | U+F13B | confirmed in v3 (fa-html5) |
| 34 | css-map | U+E749 | confirmed in v3 (dev-css3) |
| 35 | sass | U+E603 | confirmed in v3 (seti-sass) |
| 36 | less | U+E60B | confirmed in v3 (seti-less) |
| 37 | json | U+E60B | confirmed in v3 (seti-less) |
| 38 | yaml | U+E60B | confirmed in v3 (seti-less) |
| 41 | javascript | U+E74E | confirmed in v3 (dev-javascript_alt) |
| 42 | javascript-map | U+E781 | confirmed in v3 (dev-javascript_badge) |
| 45 | react | U+E7BA | confirmed in v3 (dev-react) |
| 46 | react_ts | U+E7BA | confirmed in v3 (dev-react) |
| 47 | settings | U+F013 | confirmed in v3 (fa-gear) |
| 48 | typescript | U+E628 | confirmed in v3 (seti-typescript) |
| 53 | visualstudio | U+E70C | confirmed in v3 (dev-visualstudio) |
| 54 | database | U+E706 | confirmed in v3 (dev-database) |
| 55 | mysql | U+E704 | confirmed in v3 (dev-mysql) |
| 56 | postgresql | U+E76E | confirmed in v3 (dev-postgresql) |
| 57 | sqlite | U+E7C4 | confirmed in v3 (dev-sqlite) |
| 59 | zip | U+F410 | confirmed in v3 (oct-file_zip) |
| 60 | exe | U+F2D0 | confirmed in v3 (fa-window_maximize) |
| 74 | font | U+F031 | confirmed in v3 (fa-font) |
| 76 | ruby | U+E739 | confirmed in v3 (dev-ruby) |
| 77 | gemfile | U+E21E | confirmed in v3 (fae-ruby_o) |
| 78 | fsharp | U+E7A7 | confirmed in v3 (dev-fsharp) |
| 80 | docker | U+F308 | confirmed in v3 (linux-docker) |
| 88 | rust | U+E7A8 | confirmed in v3 (dev-rust) |
| 89 | raml | U+E60B | confirmed in v3 (seti-less) |
| 91 | haskell | U+E61F | confirmed in v3 (seti-haskell) |
| 92 | git | U+E702 | confirmed in v3 (dev-git) |
| 93 | lua | U+E620 | confirmed in v3 (seti-lua) |
| 94 | clojure | U+E76A | confirmed in v3 (dev-clojure_alt) |
| 95 | groovy | U+F2A6 | confirmed in v3 (fa-glide_g) |
| 97 | dart | U+E798 | confirmed in v3 (dev-dart) |
| 99 | assembly | U+F471 | confirmed in v3 (oct-file_binary) |
| 103 | handlebars | U+E60F | confirmed in v3 (seti-mustache) |
| 104 | perl | U+E769 | confirmed in v3 (dev-perl) |
| 105 | elixir | U+E62D | confirmed in v3 (seti-elixir) |
| 106 | erlang | U+E7B1 | confirmed in v3 (dev-erlang) |
| 107 | twig | U+E61C | confirmed in v3 (seti-twig) |
| 108 | julia | U+E624 | confirmed in v3 (seti-julia) |
| 109 | elm | U+E62C | confirmed in v3 (seti-elm) |
| 111 | stylus | U+E600 | confirmed in v3 (seti-stylus) |
| 116 | vercel | U+F47E | confirmed in v3 (oct-triangle_up) |
| 117 | applescript | U+F302 | confirmed in v3 (linux-apple) |
| 120 | todo | U+F058 | confirmed in v3 (fa-ok_sign) |
| 121 | nix | U+F313 | confirmed in v3 (linux-nixos) |
| 122 | http | U+F484 | confirmed in v3 (oct-globe) |
| 124 | ionic | U+E7A9 | confirmed in v3 (dev-ionic) |
| 125 | gulp | U+E763 | confirmed in v3 (dev-gulp) |
| 127 | npm | U+E71E | confirmed in v3 (dev-npm) |
| 135 | authors | U+F0C0 | confirmed in v3 (fa-users) |
| 136 | favicon | U+E623 | confirmed in v3 (seti-favicon) |
| 137 | karma | U+E622 | confirmed in v3 (seti-karma) |
| 138 | travis | U+E77E | confirmed in v3 (dev-travis) |
| 139 | heroku | U+E607 | confirmed in v3 (seti-heroku) |
| 140 | gitlab | U+F296 | confirmed in v3 (fa-gitlab) |
| 141 | bower | U+E61A | confirmed in v3 (seti-bower) |
| 143 | jenkins | U+E767 | confirmed in v3 (dev-jenkins) |
| 146 | ejs | U+E618 | confirmed in v3 (seti-ejs) |
| 147 | grunt | U+E611 | confirmed in v3 (seti-grunt) |
| 148 | django | U+E71D | confirmed in v3 (dev-django) |
| 150 | bitbucket | U+F171 | confirmed in v3 (fa-bitbucket) |
| 151 | d | U+E7AF | confirmed in v3 (dev-dlang) |
| 153 | azure-pipelines | U+F427 | confirmed in v3 (oct-rocket) |
| 159 | 3d | U+E79B | confirmed in v3 (dev-contao) |
| 161 | vim | U+E62B | confirmed in v3 (custom-vim) |
| 162 | moonscript | U+F186 | confirmed in v3 (fa-moon_o) |
| 164 | disc | U+E271 | confirmed in v3 (fae-disco) |
| 167 | liquid | U+E275 | confirmed in v3 (fae-drop) |
| 168 | prolog | U+E7A1 | confirmed in v3 (dev-prolog) |
| 172 | pawn | U+E261 | confirmed in v3 (fae-chess_pawn) |
| 174 | dhall | U+F448 | confirmed in v3 (oct-pencil) |
| 178 | stryker | U+F05B | confirmed in v3 (fa-crosshairs) |
| 179 | modernizr | U+E720 | confirmed in v3 (dev-angularmaterial) |
| 181 | debian | U+F306 | confirmed in v3 (linux-debian) |
| 182 | ubuntu | U+F31C | confirmed in v3 (linux-ubuntu_inverse) |
| 183 | arch | U+F303 | confirmed in v3 (linux-archlinux) |
| 184 | redhat | U+F316 | confirmed in v3 (linux-redhat) |
| 185 | gentoo | U+F30D | confirmed in v3 (linux-gentoo) |
| 186 | linux | U+E712 | confirmed in v3 (dev-linux) |
| 187 | raspberry-pi | U+F315 | confirmed in v3 (linux-raspberry_pi) |
| 188 | manjaro | U+F312 | confirmed in v3 (linux-manjaro) |
| 189 | opensuse | U+F314 | confirmed in v3 (linux-opensuse) |
| 190 | fedora | U+F30A | confirmed in v3 (linux-fedora) |
| 191 | freebsd | U+F30C | confirmed in v3 (linux-freebsd) |
| 192 | centOS | U+F304 | confirmed in v3 (linux-centos) |
| 193 | alpine | U+F300 | confirmed in v3 (linux-alpine) |
| 194 | mint | U+F30F | confirmed in v3 (linux-linuxmint_inverse) |
| 196 | laravel | U+E73F | confirmed in v3 (dev-laravel) |
| 197 | pug | U+E60E | confirmed in v3 (seti-html) |
| 200 | jinja | U+E000 | confirmed in v3 (pom-clean_code) |
| 201 | sublime | U+E7AA | confirmed in v3 (dev-sublime) |
| 202 | markojs | U+F13B | confirmed in v3 (fa-html5) |
| 203 | vscode | U+E70C | confirmed in v3 (dev-visualstudio) |
| 204 | qsharp | U+F292 | confirmed in v3 (fa-hashtag) |
| 211 | arduino | U+E255 | confirmed in v3 (fae-infinity) |
| 213 | graphql | U+E284 | confirmed in v3 (fae-benzene) |
| 214 | kotlin | U+E70E | confirmed in v3 (dev-android) |
| 219 | cmake | U+F425 | confirmed in v3 (oct-tools) |
| 220 | nuxt | U+E2A6 | confirmed in v3 (fae-mountains) |
| 221 | ocaml | U+F1CE | confirmed in v3 (fa-circle_o_notch) |
| 222 | haxe | U+F425 | confirmed in v3 (oct-tools) |
| 225 | merlin | U+F136 | confirmed in v3 (fa-maxcdn) |
| 226 | mjml | U+E714 | confirmed in v3 (dev-ghost_small) |
| 227 | terraform | U+E20F | confirmed in v3 (fae-tools) |
| 228 | apiblueprint | U+F031 | confirmed in v3 (fa-font) |
| 229 | slim | U+F24E | confirmed in v3 (fa-scale_balanced) |
| 231 | codecov | U+E37C | confirmed in v3 (weather-umbrella) |
| 232 | protractor | U+F288 | confirmed in v3 (fa-product_hunt) |
| 235 | firebase | U+E787 | confirmed in v3 (dev-firebase) |
| 246 | vagrant | U+F27D | confirmed in v3 (fa-vimeo_v) |
| 249 | opam | U+F1CE | confirmed in v3 (fa-circle_o_notch) |
| 251 | nuget | U+E77F | confirmed in v3 (dev-dotnet) |
| 337 | dir-config | U+E5FC | confirmed in v3 (custom-folder_config) |
| 338 | dir-controller | U+E5FC | confirmed in v3 (custom-folder_config) |
| 339 | dir-git | U+E5FB | confirmed in v3 (custom-folder_git_branch) |
| 340 | dir-github | U+E5FD | confirmed in v3 (custom-folder_github) |
| 341 | dir-npm | U+E5FA | confirmed in v3 (custom-folder_npm) |

## formatterStuff.go Changes

- Line 163: `file icon comparison` U+F723 → U+F0224 (migrated (mdi: file_outline))

## Post-Migration Reminders

1. Run `go build ./...` to verify all escape sequences are valid Go
2. Regenerate ALL test snapshots: `go test ./... -update`
3. Run `go test ./...` to verify tests pass
4. Review any unmapped/missing icons above for manual fixes
