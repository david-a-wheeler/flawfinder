#!/bin/sh -l
# $1 whitespace-separated arguments. Some filenames may need to be escaped.
# $2 output filename

flawfinder $1 | tee "$2"
