Name:              flawfinder
Summary:           Examines C/C++ source code for security flaws
Version:           2.0.19
Release:           1%{?dist}
Group:             Development/Tools

License:           GPLv2+
URL:               http://dwheeler.com/flawfinder/
Source:            http://dwheeler.com/flawfinder/%{name}-%{version}.tar.gz

BuildArch:         noarch
BuildRequires:     flex
BuildRequires:     make
BuildRoot:         %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Provides:          flawfinder = %{version}-%{release}
Requires:          python

%description
Flawfinder scans through C/C++ source code,
identifying lines ("hits") with potential security flaws.
By default it reports hits sorted by severity, with the riskiest lines first.

%prep
%setup  -q

%build
%{__make} %{?_smp_mflags}

%install
%{__make} install DESTDIR=${RPM_BUILD_ROOT} prefix=%{_usr}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.md ChangeLog COPYING flawfinder.ps
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Tue Sep 21 2021 Weilun Fong <wlf@zhishan-iot.tk>
- Improve install command
- Add <Provides> SPEC Directive

* Mon Aug 27 2007 Horst H. von Brand <vonbrand@inf.utfsm.cl>  1.27-2
- Fix specfile as per Fedora guidelines

* Sat Feb  1 2003 Jose Pedro Oliveira <jpo@di.uminho.pt>
- changed build architecture to noarch
- replaced hardcoded directories by rpm macros
- removed several rpmlint warnings/errors
