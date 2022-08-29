import argparse

from convert import convert_date

parser = argparse.ArgumentParser(description='Convert a COBOL date to a human readable date')

parser.add_argument('-S', '--dateAsString', type=str, help='The date to convert, EX: C20531')
parser.add_argument('-s', '--source', type=str, help='Location of a new line delimited file of dates to convert')
parser.add_argument('-d', '--destination', type=str, help='Destination for converted dates')
parser.add_argument('-n', '--numbers', action='store_true', help='Results will be in digits instead of words EX: 6/31 instead of June 31')


args = parser.parse_args()
result = []

if args.dateAsString:
    result.append(convert_date(args.dateAsString, args.numbers))

if args.source:
    with open(args.source, 'r') as f:
        for line in f:
            result.append(convert_date(line.strip(), args.numbers))

if args.destination:
    with open(args.destination, 'w') as f:
        for line in result:
            f.write(str(line)+'\n')

else: 
    for line in result: print(line)
