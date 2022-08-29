example_date ='C20531'
example_output = '2022-05-31'

months = ['January','February','March','April','May','June','July','August','September','October','November','December']

def convert_date(date):
    if len(date) != 6: return 
    month_number, day_number = int(date[-4:-2]), int(date[-2:])
    month_string = months[month_number]
    return f'{month_string} {day_number}'