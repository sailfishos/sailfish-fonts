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
%{_datadir}/fonts/sail-sans-pro/*
%{_datadir}/fonts/wqy-zenhei/*
%{_datadir}/fonts/amiri/*
%{_datadir}/fonts/lohit-devanagari/*
%{_datadir}/fonts/lohit-gujarati/*
%{_datadir}/fonts/lohit-bengali
%{_datadir}/fonts/lohit-tamil
%{_datadir}/fonts/lohit-telugu
%{_datadir}/fonts/lohit-punjabi
%{_datadir}/fonts/lohit-kannada
%{_datadir}/fonts/lohit-malayalam
%{_datadir}/fonts/dejavu
%{_datadir}/fonts/liberation
%{_datadir}/fonts/symbola/*
%{_datadir}/fonts/umpush/*
%{_datadir}/fontconfig/conf.avail/*
%{_sysconfdir}/fonts/conf.d/*

