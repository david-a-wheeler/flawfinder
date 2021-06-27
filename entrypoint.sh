#!/bin/sh -l
# $1 arguments. BEWARE: Some filenames may need to be escaped.
# $2 output filename

flawfinder $1 > "$2"

echo "Executed with success."
