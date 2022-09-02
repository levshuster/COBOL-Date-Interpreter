# example_date ='C20531'
# example_output = 'June 31 2022'

import re

months = ['January','February','March','April','May','June','July','August','September','October','November','December']
deliminator = '-'

def convert_date(date, numbers):
    date = re.sub(r'[\s]', '', date)
    if len(date) < 4: return 
    decade_hex, year_number, month_number, day_number = str(date[0:1]), int(date[1:2]), int(date[-4:-2]), int(date[-2:])
    month_string = months[month_number-1]
    # convert hex to int
    decade_number = 190+int(decade_hex, 16)
    
    if numbers: return f'{month_number}{deliminator}{day_number}-{decade_number}{year_number}'
    else: return f'{month_string} {day_number} {decade_number}{year_number}'

def bulk_convert_date_new_line_deliminated(dates, numbers):
    return list(map(lambda date: convert_date(date, numbers), dates.split('\n')))

