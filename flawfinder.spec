Name: flawfinder
Summary: Examines C/C++ source code for security flaws
Version: 1.31
Release: 1%{?dist}
License: GPLv2+
Group: Development/Tools
URL: http://www.dwheeler.com/flawfinder/
Source: http://www.dwheeler.com/flawfinder/%{name}-%{version}.tar.gz
Requires: python
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Flawfinder scans through C/C++ source code,
identifying lines ("hits") with potential security flaws.
By default it reports hits sorted by severity, with the riskiest lines first.

%prep
%setup  -q

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
install -m755 -D flawfinder ${RPM_BUILD_ROOT}%{_bindir}/flawfinder
install -m644 -D flawfinder.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/flawfinder.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README ChangeLog COPYING flawfinder.ps
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Aug 27 2007 Horst H. von Brand <vonbrand@inf.utfsm.cl>  1.27-2
- Fix specfile as per Fedora guidelines

* Sat Feb  1 2003 Jose Pedro Oliveira <jpo@di.uminho.pt>
- changed build architecture to noarch
- replaced hardcoded directories by rpm macros
- removed several rpmlint warnings/errors

# vim:set ai ts=4 sw=4:
