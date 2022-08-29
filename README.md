# COBOL-Date-Interpreter

Given a text file of cobol dates delimited by new lines, return a human readable date.

# Warning

This function throws out year infomation.

# CLI help

```python3 COBOLDateInterp.py -h
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
  -n, --numbers         Results will be in digits instead of words EX: 6/31 instead of June 31
  
```
  
# Instaltion and Usage

```Learning git clone https://github.com/levshuster/COBOL-Date-Interpreter.git
Cloning into 'COBOL-Date-Interpreter'...
remote: Enumerating objects: 21, done.
remote: Counting objects: 100% (21/21), done.
remote: Compressing objects: 100% (16/16), done.
remote: Total 21 (delta 9), reused 11 (delta 5), pack-reused 0
Receiving objects: 100% (21/21), 16.65 KiB | 487.00 KiB/s, done.
Resolving deltas: 100% (9/9), done.
➜  Learning cd COBOL-Date-Interpreter 
➜  COBOL-Date-Interpreter git:(main) ls
COBOLDateInterp.py LICENSE            README.md          convert.py


➜  COBOL-Date-Interpreter git:(main) python3 COBOLDateInterp.py -S C20531                              
June 31


➜  COBOL-Date-Interpreter git:(main) cat >> source.txt
C10712
C10720
C10721
C10721
C10721
C10721
C10721
C10721
C10722
C10722
C10723
C10723
C10723
C10723
C10727
C10803
C10803
C10803
C10803
C10803
C10804
C10804
C10805
C10805
C10811
C10811
C10824
C10824
C10824
C10825
C10826
C10826
C10826
C10830
C10830
C10830
C10830
C10830
C10830
C10830
C10830
C10830
C10830
C10830
C10830
C10830
C10830
C10830
C10830
C10830
C10830
C10830
C10830
C10712
C10712
^C


➜  COBOL-Date-Interpreter git:(main) ✗ python3 COBOLDateInterp.py -s source.txt
August 12
August 20
August 21
August 21
August 21
August 21
August 21
August 21
August 22
August 22
August 23
August 23
August 23
August 23
August 27
September 3
September 3
September 3
September 3
September 3
September 4
September 4
September 5
September 5
September 11
September 11
September 24
September 24
September 24
September 25
September 26
September 26
September 26
September 30
September 30
September 30
September 30
September 30
September 30
September 30
September 30
September 30
September 30
September 30
September 30
September 30
September 30
September 30
September 30
September 30
September 30
September 30
September 30
August 12
August 12


➜  COBOL-Date-Interpreter git:(main) ✗ python3 COBOLDateInterp.py -s source.txt -n
7-12
7-20
7-21
7-21
7-21
7-21
7-21
7-21
7-22
7-22
7-23
7-23
7-23
7-23
7-27
8-3
8-3
8-3
8-3
8-3
8-4
8-4
8-5
8-5
8-11
8-11
8-24
8-24
8-24
8-25
8-26
8-26
8-26
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
7-12
7-12


➜  COBOL-Date-Interpreter git:(main) ✗ python3 COBOLDateInterp.py -s source.txt -n -d destination.txt


➜  COBOL-Date-Interpreter git:(main) ✗ cat destination.txt 
7-12
7-20
7-21
7-21
7-21
7-21
7-21
7-21
7-22
7-22
7-23
7-23
7-23
7-23
7-27
8-3
8-3
8-3
8-3
8-3
8-4
8-4
8-5
8-5
8-11
8-11
8-24
8-24
8-24
8-25
8-26
8-26
8-26
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
8-30
7-12
7-12```
