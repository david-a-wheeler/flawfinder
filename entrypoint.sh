#!/bin/sh -l
# $1 whitespace-separated arguments. Some filenames may need to be escaped.
# $2 output filename

output="${2:-flawfinder-output.txt}"

flawfinder $1 > "$output"
result="$?"

cat "$output"
exit "$result"
