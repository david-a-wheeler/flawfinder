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
command line tool.  It requires either Python 2.7 or Python 3.

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

~~~~
flawfinder src/
~~~~

To examine all files in the *current* directory and down recursively:

~~~~
flawfinder ./
~~~~

Hits (findings) are given a risk level from 0 (very low risk) to 5 (high risk),
By default, findings of risk level 1 or higher are shown.
You can show only the hits of risk level 4 or higher in the current
directory and down this way:

~~~~
flawfinder --minlevel 4 ./
~~~~

The manual page (flawfinder.1 or flawfinder.pdf) describes how to use
flawfinder (including its various options) and related information
(such as how it supports CWE).  For example, the `--html` option generates
output in HTML format. The `--help` option gives a brief list of options.

# Character Encoding Errors

Flawfinder must be able to correctly interpret your source code's
character encoding.
In the vast majority of cases this is not a problem, especially
if the source code is correctly encoded using UTF-8 and your system
is configured to use UTF-8 (the most common situation by far).

However, it's possible for flawfinder to halt if there is a
character encoding problem and you're running Python3.
The usual symptom is error messages like this:
`Error: encoding error in FILENAME 'ENCODING' codec can't decode byte ... in position ...: invalid start byte`

Unfortunately, Python3 fails to provide useful built-ins to deal with this.
Thus, it's non-trivial to deal with this problem without depending on external
libraries (which we're trying to avoid).

If you have this problem, see the flawfinder manual page for a collection
of various solutions.
One of the simplest is to simply convert the source code and system
configuration to UTF-8.
You can convert source code to UTF-8 using tools such as the
system tool `iconv` or the Python program
[`cvt2utf`](https://pypi.org/project/cvt2utf/);
you can install `cvt2utf` using `pip install cvt2utf`.

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

# Flawfinder GitHub Action

There's a GitHub action available for those who use GitHub.

## Usage

See [action.yml](https://github.com/david-a-wheeler/flawfinder/blob/main/action.yml)

Create a .yml file under .github/workflows with the following contents:

### Basic demo:

```yml
- name: flawfinder_scan
  uses: david-a-wheeler/flawfinder@2.0.19
  with:
    arguments: '--sarif ./'
    output: 'flawfinder_results.sarif'
```

You can add many other additions to the arguments.
For example, `--error-level=4` will cause an error to be returned if
flawfinder finds a vulnerability of level 4 or higher.
Notice the version number after the `@` symbol; you can select a
different version.

You can find the action name and version string from [Marketplace](https://github.com/marketplace/actions/flawfinder_scan)
by clicking "Use latest/xxx version" button.

### Input options:

- arguments: [Flawfinder command arguments](ttps://github.com/david-a-wheeler/flawfinder/blob/master/README.md#usage)
- output: Flawfinder output file name. Can be uploaded to GitHub.

# Contributions

We love contributions!  For more information on contributing, see
the file [CONTRIBUTING.md](CONTRIBUTING.md).

# License

Flawfinder is released under the GNU GPL license version 2 or later (GPL-2.0+).
See the [COPYING](COPYING) file for license information.
