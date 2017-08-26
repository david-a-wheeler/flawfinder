#!/usr/bin/env python

# This is the setup.py script for "flawfinder" by David A. Wheeler.
# My thanks to Jon Nelson, who created the initial setup.py script.

# Template for creating your own setup.py.  See the USAGE file in
# the Distutils source distribution for descriptions of all the
# options shown below.  Brief instructions on what to do:
#   - set the other metadata: version, description, author, author_email
#     and url.  All of these except 'description' are required, although
#     you may supply 'maintainer' and 'maintainer_email' in place of (or in
#     addition to) 'author' and 'author_email' as appropriate.
#   - fill in or delete the 'packages', 'package_dir', 'py_modules',
#     and 'ext_modules' options as appropriate -- see USAGE for details
#   - delete this comment and change '__revision__' to whatever is
#     appropriate for your revision control system of choice (just make
#     sure it stores the revision number for your distribution's setup.py
#     script, *not* the examples/template_setup.py file from Distutils!)


"""Setup script for the flawfinder tool."""

from distutils.core import setup
import commands

setup (# Distribution meta-data
       name = "flawfinder",
       packages = ["flawfinder"], # Must be same as name
       version = "2.0.2",
       description = "a program that examines source code looking for security weaknesses",
       author = "David A. Wheeler",
       author_email = "dwheeler@dwheeler.com",
       license = 'GPL-2.0+',
       long_description = """Flawfinder is a program that can scan
C/C++ source code and identify out potential security flaws,
ranking them by likely severity.
It is released under the GNU GPL license.""",
       url = "http://www.dwheeler.com/flawfinder/",
       download_url = "https://sourceforge.net/projects/flawfinder/files/flawfinder-2.0.2.tar.gz/download",
       keywords = ['analysis', 'security', 'analyzer'],
       classifiers = [
           'Development Status :: 5 - Production/Stable',
           'Environment :: Console',
           'Intended Audience :: Developers',
           'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
           'Natural Language :: English',
           'Programming Language :: Python :: 2.7',
           'Operating System :: OS Independent',
           'Topic :: Security',
           'Topic :: Software Development :: Build Tools',
           'Topic :: Software Development :: Quality Assurance',
           'Topic :: Software Development :: Testing'
           ],
       python_requires = '~=2.7',
       scripts = [ 'flawfinder' ],
       data_files = [ ('share/man/man1', [ 'flawfinder.1.gz' ]) ],
       py_modules = [ ],
      )
