# COBOL-Date-Interpreter
given a text file of cobol dates delimited by new lines, return a human readable date

# CLI help
python3 COBOLDateInterp.py -h                         
usage: COBOLDateInterp.py [-h] [-S DATEASSTRING] [-s SOURCE] [-d DESTINATION]

Convert a COBOL date to a human readable date

optional arguments:
  -h, --help            show this help message and exit
  -S DATEASSTRING, --dateAsString DATEASSTRING
                        The date to convert, EX: C20531
  -s SOURCE, --source SOURCE
                        Location of a new line delimited file of dates to convert
  -d DESTINATION, --destination DESTINATION
                        destination for converted dates 
