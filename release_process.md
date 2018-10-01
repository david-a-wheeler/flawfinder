# Release process

Here's information on how to release an update to flawfinder.

## Changing version number

You should really change the version number before changing anything else.
Make sure every release has a unique version number.

To change version number, edit the following files:
makefile
flawfinder
flawfinder.spec
setup.py
index.html

Then run:
`make test && make test-is-correct` # update version number in tests

## Test it

`make check` # Run tests in Python 2 and 3

## Tag version

Once you're sure this is the *real* version, tag it:

`git tag VERSION`
`git push --tags`

## Create tarball

Run:
`make distribute`


## Post tarball

Then post the tarball flawfinder-VERSION.tar.gz to
the usual places:

* SourceForge "files" directory, and set it to be the default download.
* dwheeler.com/flawfinder

## Post to pip

Create a PyPi distribution package:

`make pypi`

And upload it:

`make upload-pypi`
