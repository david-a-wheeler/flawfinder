#!/usr/bin/env python

# This is the setup.py script for "flawfinder" by David A. Wheeler.
# My thanks to Jon Nelson, who created the initial setup.py script.

"""Setup script for the flawfinder tool."""

from setuptools import setup # Don't need find_packages

setup (# Distribution meta-data
       name = "flawfinder",
       version = "2.0.19",
       # We install a script, not a separate package.
       # packages = ["flawfinder"], # Must be same as name
       # Do not need: packages=find_packages(),
       description = "a program that examines source code looking for security weaknesses",
       author = "David A. Wheeler",
       author_email = "dwheeler@dwheeler.com",
       license = 'GPL-2.0+',
       long_description = """Flawfinder is a program that can scan
C/C++ source code and identify out potential security flaws,
ranking them by likely severity.
It is released under the GNU GPL license.""",
       url = "http://dwheeler.com/flawfinder/",
       download_url = "https://sourceforge.net/projects/flawfinder/files/flawfinder-2.0.8.tar.gz/download",
       zip_safe = True,
       keywords = ['analysis', 'security', 'analyzer'],
       classifiers = [
           'Development Status :: 5 - Production/Stable',
           'Environment :: Console',
           'Intended Audience :: Developers',
           'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
           'Natural Language :: English',
           'Programming Language :: Python :: 2.7',
           'Programming Language :: Python :: 3',
           'Programming Language :: Python :: 3.6',
           'Operating System :: OS Independent',
           'Topic :: Security',
           'Topic :: Software Development :: Build Tools',
           'Topic :: Software Development :: Quality Assurance',
           'Topic :: Software Development :: Testing'
           ],
       python_requires = '>=2.7',
       entry_points={
        'console_scripts': [
            'flawfinder = flawfinder:main',
        ],
       },
       data_files = [ ('share/man/man1', [ 'flawfinder.1.gz' ]) ],
       py_modules = ['flawfinder'],
      )
