Name:       sailfish-fonts
Summary:    Sailfish platform fonts
Version:    0.0.1
Release:    1
Group:      User Interface/X
License:    OFL (Sail Sans Pro), GPLv2 (WenQuanYi Zen Hei), Apache License v2.0 (Roboto)
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.gz
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
for fontname in sail-sans-pro wqy-zenhei roboto amiri lohit-devanagari; do
    cp -R $fontname %{buildroot}/%{_datadir}/fonts/$fontname
done

%post
{
    [ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache
} &> /dev/null || :

%files
%defattr(-,root,root,0755)
/etc/fonts/local.conf
%{_datadir}/fonts/sail-sans-pro/*
%{_datadir}/fonts/wqy-zenhei/*
%{_datadir}/fonts/roboto/*
%{_datadir}/fonts/amiri/*
%{_datadir}/fonts/lohit-devanagari/*

