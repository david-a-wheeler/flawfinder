# About

This is "flawfinder" by [David A. Wheeler](mailto:dwheeler@dwheeler.com).

Flawfinder is a simple program that scans C/C++ source code and reports
potential security flaws.  It can be a useful tool for examining software
for vulnerabilities, and it can also serve as a simple introduction to
static source code analysis tools more generally.  It is designed to
be easy to install and use.  Flawfinder supports the Common Weakness
Enumeration (CWE) and is officially CWE-Compatible.
It supports various output formats including SARIF, SonarQube, and HTML.

Flawfinder can be used alongside AI-based code analysis tools.
Flawfinder output can be used to quickly identify which areas of code
deserve closer attention, which an AI system can then examine in more detail.

For more information, see the [project website](http://dwheeler.com/flawfinder)

# Platforms

Flawfinder is designed for use on Unix/Linux/POSIX systems
(including Cygwin, Linux-based systems, MacOS, and various BSDs) as a
command line tool.  It requires Python (we test with Python 3;
Python 2.7 should work but this is increasingly untested).

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

In a terminal, that report is drawn as a compact color summary: risk
levels are grouped, each hit stays on a short block, and the totals sit
in a single frame. Redirecting the output, or passing `--classic`, keeps
the original plain text so scripts and diffs do not change. `--pretty`
forces the color report even when output is redirected (color is still
omitted unless the stream is a terminal or `FORCE_COLOR` is set).
`NO_COLOR` turns the colors off and leaves the layout.

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
Flawfinder does not use or have access to most information about control flow,
data flow, data types, namespaces, and scopes.
Thus, flawfinder will necessarily
produce many false positives for vulnerabilities and fail to report
many vulnerabilities.  On the other hand, flawfinder can find
vulnerabilities in programs that cannot be built or cannot be linked.
Flawfinder also doesn't get as confused by most macro definitions
and other oddities that more sophisticated tools have trouble with.

# Flawfinder GitHub Action

There's a GitHub action available for those who use GitHub.

## Usage

See [action.yml](https://github.com/david-a-wheeler/flawfinder/blob/main/action.yml)

Create a .yml file under .github/workflows with the following contents:

### Basic demo:

```yml
- name: flawfinder_scan
  uses: david-a-wheeler/flawfinder@2.0.20
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

# SonarQube Integration

Flawfinder integrates with SonarQube's cxx plugin. Add the Flawfinder rules in
SonarQube under "Administration > CXX External Analyers > Other Rule Definitions"
by running Flawfinder once using the following options.

~~~~
flawfinder --listrules --sonar [...]
~~~~

The in your CI/CD run Flawfinder like this to generate output that SonarQube
can understand.

~~~~
flawfinder -CDQ --sonar [...]
~~~~

You want to redirect the output to a file that you can then load into
SonarQube via the `sonar.cxx.other.reportPaths` option.

# Contributions

We love contributions!  For more information on contributing, see
the file [CONTRIBUTING.md](CONTRIBUTING.md).

# License

Flawfinder is released under the GNU GPL license version 2 or later (GPL-2.0+).
See the [COPYING](COPYING) file for license information.
