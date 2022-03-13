
Modified version of the [sphinx-rtd-theme](https://github.com/rtfd/sphinx_rtd_theme). Files are manually modified instead of built from source because I refuse to go through the nightmare of using any garbage based on Node.js.

- Removed **versions.html** template file.
- Removed **badges_only.css** CSS file.
- Removed **html5shiv** JS *library*.
- Removed maximum width limits of the page content from CSS file.
- Removed all IE specific garbage from CSS file.
- Removed all shipped fonts and references to them. Except for FontAwesome (it is used in several places by the theme and I might want to use it in the future too). The reason is very simple, DEATH TO SERIF FONTS!!!
- Added some custom styling classes to CSS file.
- Changed almost all **theme.conf** file options.
