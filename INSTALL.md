# Installing flawfinder

You can install flawfinder a number of different ways.
Choose the approach that's most convenient for you!
The options (described below) are (1) pip, (2) package for Unix-like system, (3) source install, and (4) run directly.


## 1. PIP

For many, the simple approach is to first install Python
(2.7 or something reasonable in the 3.X series).
Then use `pip` to install flawfinder
(this will normally download the package):

~~~~
pip install flawfinder
~~~~

One advantage for using pip is that you'll generally get the
*current* released version.


## 2. PACKAGE FOR UNIX-LIKE SYSTEM (including Cygwin):

If you use an RPM-based system (e.g., Red Hat) or deb-based system
(e.g., Debian), you can use their respective RPM or debian installation
program and just install it; then ignore the rest of these instructions.
For a ports-based system where you have a current port, just use that.

This will work out-of-the-box; it may not be the most recent version.

One way to accomplish this is:

~~~~
sudo apt install flawfinder
~~~~


## 3. TARBALL (SOURCE INSTALL)

QUICK START:
The quick way to install flawfinder from the tarball is to
unpack the tarball and type in something like this on the command line:

~~~~
sudo make prefix=/usr install
~~~~

Omit prefix=/usr to install in /usr/local instead.
Omit "sudo" if you are already root.
Note that this installation approach follows the usual install conventions
as described below, including prefix= and DESTDIR.

Not enough?  Here are more detailed step-by-step instructions and options.

* Download the "tarball" and uncompress it.
  GNU-based systems can run `tar xvzf flawfinder-<version>.tar.gz` to do so,
  then move into the newly created directory with `cd flawfinder-<version>`
  If that doesn't work (e.g., you have an old tar program), use:
    `gunzip flawfinder-<version>.tar.gz`
    `tar xvf flawfinder-<version>.tar`
    `cd flawfinder-<version>`

* Decide where you want to put it.  Flawfinder normally installs everything
  in /usr/local, with the program in /usr/local/bin and the man page in
  /usr/local/share/man/man1, per GNU conventions.  You can override this
  when installing (with "make install") by setting some environment
  variables.  You can do this by setting traditional GNU variables, e.g.,
  "prefix" = prefix of all files, default /usr/local
  "bindir" = directory for binaries, default $(prefix)/bin
             (the program "flawfinder" is put here)
  "datarootdir" = data for shared data, by default $(prefix)/share
  "mandir" = directory for all man pages, default $(datarootdir)/man
  "man1dir" = directory for all man1 pages, default $(mandir)/man1
             (the man page "flawfinder.1" is put here).  Given the
             previous definitions, its default is $(prefix)/share/man/man1
  It is common to override "prefix" with "/usr" instead.

  You can also use the older flawfinder makefile variables to control
  installation; you can set:
  `INSTALL_DIR` = prefix, default $(prefix);
  `INSTALL_DIR_BIN` = program location, default `$(bindir)`;
  `INSTALL_DIR_MAN` = manual location, default `$(man1dir)`.
  Note that the default of `INSTALL_DIR_MAN` has changed; at one time
  it was `$(prefix)/man/man1`, but now it is `$(prefix)/share/man/man1`

* If you're using Cygwin on Windows, you can install it using "make install"
  but you need to tell the makefile to use the .py extension
  whenever you use make.  This will be another make install override.
  If you'll just install it, do this:

  `make PYTHONEXT=.py install`

  If you don't want to pass the "PYTHONEXT" extension each time,
  you can change the file "makefile" to remember this. Just change
  the line beginning with "PYTHONEXT=" so that it reads as follows:
  PYTHONEXT=.py

* Now install it, giving whatever overrides you need.  Currently it really
  only installs two files, an executable and a man page (documentation).
  In most cases, you'll need to be root, so run this first:
  `su`

  Then give the `make install` command appropriate for your system.
  For an all-default installation, which is what you need for most cases:
  make install

  (you need to be root; `make uninstall` reverses it).

  To install in /usr (the program in /usr/bin, the manual in /usr/man):
    `make prefix=/usr install`
  or alternatively, using the older flawfinder conventions:
    `make INSTALL_DIR=/usr install`

  To install in /usr on Cygwin:
    `make prefix=/usr PYTHONEXT=.py install`

  To put the binaries in /usr/bin, and the manuals under /usr/local/share/man
  (common for Red Hat Linux), do:
    `make prefix=/usr mandir=/usr/local/share/man install`

  The installer and uninstaller honor `DESTDIR`.

## 4. DIRECT EXECUTION

You can also simply run the program in the directory you've unpacked it
into.   It's a simple Python program, just type into a command line:

~~~~
./flawfinder FILES-OR-DIRECTORY
~~~~
