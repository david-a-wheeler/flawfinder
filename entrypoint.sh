#!/bin/sh -l
# $1 arguments
# $2 output filename

flawfinder $1 > $2

echo "Executed with success."
