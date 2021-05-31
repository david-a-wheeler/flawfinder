# Release process

Here's information on how to release an update to flawfinder.

## Changing version number

Ensure that the version number is the intended final value.
Make sure every release has a unique version number.

To change version number, edit the following files:
makefile
flawfinder.py
flawfinder.spec
setup.py
index.html # in dwheeler.com/flawfinder

Then run several times:

~~~~
make test ; make test-is-correct # update version number in tests
~~~~

## Test it

~~~~
make check # Run tests in Python 2 and 3
~~~~

## Commit it

~~~~
git commit -asv
~~~~

## Tag version

Once you're sure this is the *real* version, tag it:

~~~~
git tag VERSION
git push --tags origin # SourceForge
git push --tags github # GitHub
~~~~

## Create tarball

Run:

~~~~
make distribute
~~~~


## Post tarball

Then post the tarball flawfinder-VERSION.tar.gz to
the usual places:

* SourceForge "files" directory, and set it to be the default download.
* dwheeler.com/flawfinder

Do this *before* creating the PyPi distribution package for pip.

## Post to pip

First, install the programs to create a PyPi distribution package
if they are not already installed.  On Cygwin first run:

~~~~
python -m ensurepip
pip install --upgrade pip
pip install wheel
pip install twine
~~~~

Then create a PyPi distribution package (for Python2 and Python3):

~~~~
make pypi
~~~~

Now upload the PyPi distribution package:

~~~~
make upload-pypi
~~~~

## After it's uploaded

Change the version number in the repo NOW, so that there will not
be two different released versions with the same version number.
See the list at the beginning of this document for the list of
files to change.
