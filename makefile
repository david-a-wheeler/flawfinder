# Flawfinder.  Released under the General Public License (GPL).
# (C) 2001 David A. Wheeler.

# To change version number, edit this here, the beginning of the
# "flawfinder" script, flawfinder.spec, setup.py, and index.html.
# Then "make test-is-correct" to get the updated version number.
# To distribute, "make distribute && su && make rpm".
# Then use make my_install to install to website image.
# Eventually switch to using DistUtils to autogenerate.

NAME=flawfinder
VERSION=1.27
RPM_VERSION=1
VERSIONEDNAME=$(NAME)-$(VERSION)
ARCH=noarch

SAMPLE_DIR=/usr/src/linux-2.2.16

INSTALL_DIR=/usr/local
INSTALL_DIR_BIN=$(INSTALL_DIR)/bin
INSTALL_DIR_MAN=$(INSTALL_DIR)/man/man1

# For Cygwin on Windows, set PYTHONEXT=.py
# (EXE=.exe would be needed on some systems, but not for flawfinder)
EXE=
PYTHONEXT=
# EXE=.exe
# PYTHONEXT=.py

# The rpm build command.  "rpmbuild" for rpm version 4.1+
# (e.g., in Red Hat Linux 8), "rpm" for older versions.

RPMBUILD=rpmbuild

all: flawfinder.pdf flawfinder.1.gz
	chmod -R a+rX *


# This installer doesn't install the compiled Python bytecode.
# It doesn't take long to compile the short Python code, so
# it doesn't save much time, and having the source code available
# makes it easier to see what it does.  It also avoids the
# (admittedly rare) problem of bad date/timestamps causing the
# compiled code to override later uncompiled Python code.
# Note that this uses the "-p" option of mkdir; some very old Unixes
# might not support this option, but it's a really common option
# and required by SUSv3 (and probably earlier, I haven't checked).
install:
	-mkdir -p $(INSTALL_DIR_BIN)
	cp flawfinder$(PYTHONEXT) $(INSTALL_DIR_BIN)/flawfinder$(PYTHONEXT)
	-mkdir -p $(INSTALL_DIR_MAN)
	cp flawfinder.1 $(INSTALL_DIR_MAN)/flawfinder.1

uninstall:
	rm $(INSTALL_DIR_BIN)/flawfinder$(PYTHONEXT)
	rm $(INSTALL_DIR_MAN)/flawfinder.1

flawfinder.1.gz: flawfinder.1
	gzip -c9 < flawfinder.1 > flawfinder.1.gz

flawfinder.ps: flawfinder.1
	man -t ./flawfinder.1 > flawfinder.ps

flawfinder.pdf: flawfinder.ps
	ps2pdf flawfinder.ps flawfinder.pdf


clean:
	rm -f *.pyc
	rm -f flawfinder-$(VERSION).tar.gz
	rm -f *.tar

distribute: clean flawfinder.pdf flawfinder.ps
	chmod -R a+rX *
	mkdir ,1
	cp -p [a-zA-Z]* ,1
	rm -f ,1/*.tar.gz
	rm -f ,1/*.rpm
	# We don't need both "flawfinder" and "flawfinder.py":
	rm -f ,1/flawfinder.py
	mv ,1 flawfinder-$(VERSION)
	# Nobody else needs "update" either.
	rm -f ,1/update
	# Don't include (out of date) index.html
	rm -f ,1/index.html
	tar cvfz flawfinder-$(VERSION).tar.gz flawfinder-$(VERSION)
	chown --reference=. flawfinder-$(VERSION).tar.gz
	rm -fr flawfinder-$(VERSION)


time:
	echo "Timing the program. First, time taken:"
	time ./flawfinder $(SAMPLE_DIR)/*/*.[ch] > /dev/null
	echo "Lines examined:"
	wc -l $(SAMPLE_DIR)/*/*.[ch] | tail -2

test: flawfinder test.c test2.c
	# Omit time report so that results are always the same textually.
	./flawfinder --omittime test.c test2.c > test-results.txt
	./flawfinder --omittime --html --context test.c test2.c > test-results.html
	less test-results.txt

check:
	diff -u correct-results.txt test-results.txt

test-is-correct: test-results.txt
	mv test-results.txt correct-results.txt
	mv test-results.html correct-results.html

profile:
	/usr/lib/python1.5/profile.py ./flawfinder > profile-results $(SAMPLE_DIR)/*/*.[ch] > profile-results 


rpm: distribute
	chmod -R a+rX *
	cp $(VERSIONEDNAME).tar.gz /usr/src/redhat/SOURCES
	cp flawfinder.spec /usr/src/redhat/SPECS
	cd /usr/src/redhat/SPECS
	$(RPMBUILD) -ba flawfinder.spec
	chmod a+r /usr/src/redhat/RPMS/$(ARCH)/$(VERSIONEDNAME)-$(RPM_VERSION)*.rpm
	chmod a+r /usr/src/redhat/SRPMS/$(VERSIONEDNAME)-$(RPM_VERSION)*.src.rpm
	# cp -p /usr/src/redhat/RPMS/$(ARCH)/$(VERSIONEDNAME)-$(RPM_VERSION)*.rpm .
	# cp -p /usr/src/redhat/RPMS/$(ARCH)/$(VERSIONEDNAME)-$(RPM_VERSION)*.rpm  $(VERSIONEDNAME)-$(RPM_VERSION).noarch.rpm
	cp -p /usr/src/redhat/RPMS/$(ARCH)/$(VERSIONEDNAME)-$(RPM_VERSION)*.rpm  .
	cp -p /usr/src/redhat/SRPMS/$(VERSIONEDNAME)-$(RPM_VERSION)*.src.rpm .
	chown --reference=README *.rpm
	# Install, for testing.  Ignore the "not installed" message here,
	# unless you already installed it; we're just removing any old copies:
	-rpm -e flawfinder
	rpm -ivh /usr/src/redhat/RPMS/$(ARCH)/$(VERSIONEDNAME)-$(RPM_VERSION)*.rpm
	echo "Use rpm -e $(NAME) to remove the package"
	chown --reference=. *.rpm

my_install: flawfinder.pdf flawfinder.ps
	cp -p $(VERSIONEDNAME)-$(RPM_VERSION).$(ARCH).rpm \
	      $(VERSIONEDNAME)-$(RPM_VERSION).src.rpm \
	      $(VERSIONEDNAME).tar.gz \
	      flawfinder makefile \
	      flawfinder.pdf flawfinder.ps ChangeLog \
	      test.c test2.c test-results.txt test-results.html \
	           /home/dwheeler/dwheeler.com/flawfinder

.PHONY: install clean test check profile test-is-correct rpm uninstall distribute


# When I switch to using "DistUtils", I may need to move the MANIFEST.in
# file into a subdirectory (named flawfinder-versionnumber).
# I can then create all the distribution files by just typing:
#  python setup.py bdist_rpm

