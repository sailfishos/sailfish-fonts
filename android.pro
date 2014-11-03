TEMPLATE = aux

FONTS = \
    amiri/amiri-regular.ttf \
    sail-sans-pro/SailSansPro-Light.ttf

for(glob, FONTS) {
    expanded = $$files($$glob)
    for(font, expanded) {
        FONTS_CONFIG += 'assets:/fonts/$$basename(font);'
    }
}

fonts.files = $$FONTS
fonts.path = /assets/fonts
fonts.extra = /bin/echo -e \'$$FONTS_CONFIG\' > $(INSTALL_ROOT)$${fonts.path}/fonts.list

INSTALLS += fonts
