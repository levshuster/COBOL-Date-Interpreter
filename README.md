# COBOL-Date-Interpreter
Given a text file of cobol dates delimited by new lines, return a human readable date.

# CLI help
python3 COBOLDateInterp.py -h
usage: COBOLDateInterp.py [-h] [-S DATEASSTRING] [-s SOURCE] [-d DESTINATION] [-n]

Convert a COBOL date to a human readable date

optional arguments:
  -h, --help            show this help message and exit
  -S DATEASSTRING, --dateAsString DATEASSTRING
                        The date to convert, EX: C20531
  -s SOURCE, --source SOURCE
                        Location of a new line delimited file of dates to convert
  -d DESTINATION, --destination DESTINATION
                        Destination for converted dates
  -n, --numbers         Results will be in digits instead of words EX: 6/31/22 instead of June 31 2022
  