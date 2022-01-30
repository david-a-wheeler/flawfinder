# How to contribute to Flawfinder

We love contributions!  Here's how to do them in a way that will
make everyone's lives easy.

Flawfinder has long been maintained on SourceForge.
We now support reporting and changes using either SourceForge or GitHub.

## Reporting

For normal problems, bugs, and feature requests, *except* for
vulnerabilities, please file a
[GitHub issue](https://github.com/david-a-wheeler/flawfinder/issues) or
[SourceForge ticket](https://sourceforge.net/p/flawfinder/_list/tickets).

If you find a vulnerability, please separately send a private email to
[David A. Wheeler](https://dwheeler.com/contactme.html).
To maintain confidentiality,
please use an email system that implements STARTTLS hop-by-hop email
encryption on outgoing email (many do, including
Gmail, hotmail.com, live.com, outlook.com, and runbox.com).
For more about STARTTLS, see the
EFF's [STARTTLS Everywhere](https://www.starttls-everywhere.org/) project.
We plan to handle vulnerabilities separately, fixing them and *then*
telling the world.  We will gladly provide credit to vulnerability reporters
(unless you don't want the credit).  We've never had a vulnerability
report, so this is theoretical at this time.

## Change process

We use "git" to track changes.  To propose a change, create a fork
(copy) of the repository, make your changes, and create a
GitHub pull request or SourceForge merge request (they are the same thing).

If you're not familiar with the process, here's some
documentation for
[GitHub](https://help.github.com/articles/about-pull-requests/)
and
[SourceForge](https://sourceforge.net/p/forge/documentation/Git/).

## License and DCO

All proposed changes must be released under at least the project license,
in this case the GNU GPL version 2 or later (GPL-2.0+).

Proposers must agree to the
[Developer's Certificate of Origin](https://developercertificate.org/),
aka DCO.
The DCO basically says that you assert that you're legally allowed to
provide the commit.  Please include in your commit a statement of the
form to confirm this ("git commit -s" will do this):

> Signed-off-by: Your-name \<your-email-address\>

You must include the DCO in your first commit proposal.
If you forget occasionally, we'll assume that you just forgot, but
please try to not forget.

## Development environment setup

As always, if you're modifying the software, you'll need to have
your development environment set up. You need:

* make
* python2 (invocable as "python2")
* python3 (invocable as "python3")
* pylint (see below)

An easy way to install pylint is to use pip.
Most python installs have pip, but if yours does not
(e.g., Cygwin), install pip with:

~~~~
python -m ensurepip
~~~~

You may want to upgrade pip with:

~~~~
pip install --upgrade pip
~~~~

Finally, you can actually install pylint using:

~~~~
pip install pylint
~~~~

## Code Conventions

To make the program easy to install everywhere, the main executable
is exactly one self-contained file.  That involves some compromises,
but for now, please keep it that way.

We generally use the code conventions of
[PEP 8](https://www.python.org/dev/peps/pep-0008/).
The Python code uses 4-space indents (we used to use 2-space indents).
Do not use tabs.  In some cases the code doesn't yet comply;
patches to improve that are often welcome.

The code must run on both Python 2.7 and Python 3.
To check that it works on both, run:

~~~~
make check
~~~~

We use "pylint" to check for style and other generic quality problems.
To check that the code passes these quality tests, run:

~~~~
make pylint
~~~~

We require that the pylint results for contributions be at least 9.5/10 as
configured with the provided "pylintrc" file, without any errors ("E").
Better is better.  The current version *does* cause some pylint reports
(patches to fix those are welcome!).  Note that we configure pylint
with the included "pylintrc" file.
We intentionally disable some checks as being "less important",
for example, the current code has many lines longer than 80 characters.
That said, patches to make lines fit in 80 characters are welcome.

## Tests

Make *sure* that your code passes the automated tests.
As noted above, invoke tests with
"make check", which tests the code using both Python2 and Python3.

It's our policy that as major new functionality is added to the software
produced by the project, tests of that functionality should be added to
the automated test suite.

## Other

Project documentation tends to be in markdown (.md) format.
We use "~~~~" so that it's easy to cut-and-paste commands if desired.
The main document is a man page, which is then converted to PDF.

Avoid trailing space or tab on a line in source files - those can create
hard-to-understand "differences" on lines.

We have earned a
[CII Best Practices Badge](https://bestpractices.coreinfrastructure.org/projects/323)... make sure we keep it!
