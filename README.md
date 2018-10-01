# About

This is "flawfinder" by [David A. Wheeler](mailto:dwheeler@dwheeler.com).

Flawfinder is a simple program that scans C/C++ source code and reports
potential security flaws.  It can be a useful tool for examining software
for vulnerabilities, and it can also serve as a simple introduction to
static source code analysis tools more generally.  It is designed to
be easy to install and use.  Flawfinder supports the Common Weakness
Enumeration (CWE) and is officially CWE-Compatible.

For more information, see the [project website](http://dwheeler.com/flawfinder)

# Platforms

Flawfinder is designed for use on Unix/Linux/POSIX systems
(including Cygwin, Linux-based systems, MacOS, and various BSDs) as a
command line tool.  It requires Python 2.7 or Python 3.

# Installation

If you just want to *use* it, you can install flawfinder with
Python's "pip" or with your system's package manager (flawfinder has
packages for many systems).  It also supports easy installation
following usual `make install` source installation conventions.
The file [INSTALL.md](INSTALL.md) has more detailed installation instructions.
You don't HAVE to install it to run it, but it's easiest that way.

# Usage

To run flawfinder, just give it a list of source files or directories to
example.  For example, to examine all files in "src/" and down recursively:

`flawfinder src/`

The manual page (flawfinder.1 or flawfinder.pdf) describes how to use
flawfinder (including its various options) and related information
(such as how it supports CWE).  For example, the `--html` option generates
output in HTML format. The `--help` option gives a brief list of options.

# Under the hood

More technically, flawfinder uses lexical scanning to find tokens
(such as function names) that suggest likely vulnerabilities, estimates their
level of risk (e.g., by the text of function calls), and reports the results.
Flawfinder does not use or have access to information about control flow,
data flow, or data types.  Thus, flawfinder will necessarily
produce many false positives for vulnerabilities and fail to report
many vulnerabilities.  On the other hand, flawfinder can find
vulnerabilities in programs that cannot be built or cannot be linked.
Flawfinder also doesn't get as confused by macro definitions
and other oddities that more sophisticated tools have trouble with.

# Contributions

We love contributions!  For more information on contributing, see
the file [CONTRIBUTING.md](CONTRIBUTING.md).

# License

Flawfinder is released under the GNU GPL license version 2 or later (GPL-2.0+).
See the [COPYING](COPYING) file for license information.
