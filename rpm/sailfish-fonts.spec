Name:       sailfish-fonts
Summary:    Sailfish platform fonts
Version:    0.0.5
Release:    1
Group:      User Interface/X
License:    OFL (Sail Sans Pro, Lohit, Liberation, Amiri), GPLv2 (WenQuanYi Zen Hei), GPLv2+font exception(Umpush), Bitstream Vera Fonts (DejaVu), Public Domain (Symbola)
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.gz
Requires:   fontpackages-filesystem
Requires:   fontconfig
Obsoletes:  source-sans-pro-font
Obsoletes:  wqy-zenhei-font
Obsoletes:  roboto-font

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/etc/fonts/
install -m 0644 -p fontconfig/local.conf %{buildroot}/etc/fonts/
mkdir -p %{buildroot}/%{_datadir}/fonts
for fontname in sail-sans-pro wqy-zenhei amiri lohit-devanagari lohit-gujarati lohit-bengali lohit-tamil lohit-telugu lohit-punjabi lohit-kannada lohit-malayalam liberation dejavu symbola umpush; do
    cp -R $fontname %{buildroot}/%{_datadir}/fonts/$fontname
done

# Drop there here as they are covered with %license macro in the %files section
rm %{buildroot}/%{_datadir}/fonts/*/*{.txt,COPYING,GPL,LICENSE}

mkdir -p %{buildroot}/%{_datadir}/fontconfig/conf.avail
mkdir -p %{buildroot}/%{_sysconfdir}/fonts/conf.d
install -m 0644 dejavu-fontconfig/* %{buildroot}/%{_datadir}/fontconfig/conf.avail
ln -s %{_datadir}/fontconfig/conf.avail/20-unhint-small-dejavu-serif.conf %{buildroot}/%{_sysconfdir}/fonts/conf.d
ln -s %{_datadir}/fontconfig/conf.avail/20-unhint-small-dejavu-sans-mono.conf %{buildroot}/%{_sysconfdir}/fonts/conf.d
ln -s %{_datadir}/fontconfig/conf.avail/20-unhint-small-dejavu-sans.conf %{buildroot}/%{_sysconfdir}/fonts/conf.d
# override default priority so these get picked before droid fonts
ln -s %{_datadir}/fontconfig/conf.avail/57-dejavu-sans-mono.conf %{buildroot}/%{_sysconfdir}/fonts/conf.d/54-dejavu-sans-mono.conf
ln -s %{_datadir}/fontconfig/conf.avail/57-dejavu-sans.conf %{buildroot}/%{_sysconfdir}/fonts/conf.d/54-dejavu-sans.conf
ln -s %{_datadir}/fontconfig/conf.avail/57-dejavu-serif.conf %{buildroot}/%{_sysconfdir}/fonts/conf.d/54-dejavu-serif.conf


%post
{
    [ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache
} &> /dev/null || :

%files
%defattr(-,root,root,0755)
/etc/fonts/local.conf
%license sail-sans-pro/sail-sans-pro-LICENSE.txt
%{_datadir}/fonts/sail-sans-pro/*.ttf
%license wqy-zenhei/wqy-zenhei-LICENSE.txt
%{_datadir}/fonts/wqy-zenhei/*.ttc
%license amiri/amiri-OFL.txt amiri/amiri-OFL-FAQ.txt amiri/amiri-README.txt
%{_datadir}/fonts/amiri/*.ttf
%license lohit-devanagari/lohit-devanagari-OFL.txt
%{_datadir}/fonts/lohit-devanagari/*.ttf
%license lohit-gujarati/lohit-gujarati-OFL.txt
%{_datadir}/fonts/lohit-gujarati/*.ttf
%license lohit-bengali/lohit-bengali-OFL.txt
%{_datadir}/fonts/lohit-bengali/*.ttf
%license lohit-tamil/lohit-tamil-OFL.txt
%{_datadir}/fonts/lohit-tamil/*.ttf
%license lohit-telugu/lohit-telugu-OFL.txt
%{_datadir}/fonts/lohit-telugu/*.ttf
%license lohit-punjabi/lohit-punjabi-OFL.txt
%{_datadir}/fonts/lohit-punjabi/*.ttf
%license lohit-kannada/lohit-kannada-OFL.txt
%{_datadir}/fonts/lohit-kannada/*.ttf
%license lohit-malayalam/lohit-malayalam-OFL.txt
%{_datadir}/fonts/lohit-malayalam/*.ttf
%license dejavu/dejavu-LICENSE
%{_datadir}/fonts/dejavu/*.ttf
%license liberation/liberation-LICENSE
%{_datadir}/fonts/liberation/*.ttf
%license symbola/symbola-LICENSE
%{_datadir}/fonts/symbola/*.ttf
%license umpush/umpush-GPL umpush/umpush-COPYING
%{_datadir}/fonts/umpush/*.otf
%{_datadir}/fontconfig/conf.avail/*.conf
%{_sysconfdir}/fonts/conf.d/*.conf

