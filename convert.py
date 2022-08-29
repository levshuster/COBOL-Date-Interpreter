# example_date ='C20531'
# example_output = 'June 31'

months = ['January','February','March','April','May','June','July','August','September','October','November','December']
deliminator = '-'

def convert_date(date, numbers):
    if len(date) < 4: return 
    month_number, day_number = int(date[-4:-2]), int(date[-2:])
    month_string = months[month_number]
    if numbers: return f'{month_number}{deliminator}{day_number}'
    else: return f'{month_string} {day_number}'
