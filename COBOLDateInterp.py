import argparse

from convert import convert_date

parser = argparse.ArgumentParser(description='Convert a COBOL date to a human readable date')

parser.add_argument('-S', '--dateAsString', type=str, help='The date to convert, EX: C20531')
parser.add_argument('-s', '--source', type=str, help='Location of a new line delimited file of dates to convert')
parser.add_argument('-d', '--destination', type=str, help='destination for converted dates')


args = parser.parse_args()
result = []
if args.dateAsString:
    result.append(convert_date(args.dateAsString))


if args.source:
    with open(args.source, 'r') as f:
        for line in f:
            result.append(convert_date(line.strip()))

if args.destination:
    with open(args.destination, 'w') as f:
        for line in result:
            f.write(str(line)+'\n')
else: print(result)