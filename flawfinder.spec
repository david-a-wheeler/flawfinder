Name: flawfinder
Summary: Examines C/C++ source code for security flaws
Version: 1.27
Release: 1
License: GPL
Group: Development/Tools
URL: http://www.dwheeler.com/flawfinder/
Source: http://www.dwheeler.com/flawfinder/%{name}-%{version}.tar.gz
Packager: David A. Wheeler <dwheeler@dwheeler.com>
Requires: python
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Flawfinder scans through C/C++ source code,
identifying lines ("hits") with potential security flaws.
By default it reports hits sorted by severity, with the riskiest lines first.
Flawfinder is released under the GNU Public License (GPL).

%prep
%setup  -q

%build
make

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"
install -m755 -D flawfinder ${RPM_BUILD_ROOT}%{_bindir}/flawfinder
install -m644 -D flawfinder.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/flawfinder.1

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc README ChangeLog COPYING flawfinder.ps
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Sat Feb 1 2003 Jose Pedro Oliveira <jpo@di.uminho.pt>
- changed build architecture to noarch
- replaced hardcoded directories by rpm macros
- removed several rpmlint warnings/errors

# vim:set ai ts=4 sw=4:
