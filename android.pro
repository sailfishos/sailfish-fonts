TEMPLATE = aux

FONTS = \
    amiri/amiri-regular.ttf \
    roboto/*.ttf \
    sail-sans-pro/*.ttf \
    wqy-zenhei/wqy-zenhei.ttc

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
