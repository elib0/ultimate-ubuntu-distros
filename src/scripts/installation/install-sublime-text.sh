#!/bin/bash
#

# Installing the GPG key
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -

# Selecting the channel to use
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

# Plugins usados, ruta del archivo ~/.config/sublime-text-3/Packages/User/Package Control.sublime-settings
#"installed_packages":
#	[
#		"A File Icon",
#		"AdvancedNewFile",
#		"Alignment",
#		"Autoprefixer",
#		"Bootstrap 4 Snippets",
#		"BracketHighlighter",
#		"cdnjs",
#		"Color Highlighter",
#		"DocBlockr",
#		"Emmet",
#		"Gitignore",
#		"HTML5",
#		"HTMLAttributes",
#		"Icon Fonts",
#		"Icon Fonts (Legacy)",
#		"JavaScript & NodeJS Snippets",
#		"jQuery",
#		"jQuery Snippets pack",
#		"Laravel 5 Artisan",
#		"Laravel 5 Snippets",
#		"Laravel Blade Highlighter",
#		"Laravel Blade Spacer",
#		"LaravelCollective HTML Form Snippets",
#		"Material Theme",
#		"Modific",
#		"Nodejs",
#		"Package Control",
#		"Pretty JSON",
#		"Sass",
#		"SideBarEnhancements",
#		"Sublime Bookmarks",
#		"SublimeCodeIntel",
#		"Sublimerge 3",
#		"TabsExtra",
#		"Terminal",
#		"Text Pastry",
#		"TrailingSpaces",
#		"Vue Syntax Highlight",
#		"Vuejs Snippets",
#		"Vuetify"
#	]

##################################################################################################################

echo "################################################################"
echo "################      sublime text instalado    ################"
echo "################################################################"

