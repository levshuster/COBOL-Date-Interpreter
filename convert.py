from ast import main


example_date ='C20531'
example_output = '2022-05-31'

useShortMonth = False

months = ['January','February','March','April','May','June','July','August','September','October','November','December']

def convert_date(date):
    month_number, day_number = int(date[-4:-2]), int(date[-2:])
    month_string = months[month_number]
    if useShortMonth:
        month_string = month_string[:3]
    return f'{month_string} {day_number}'
    
# main
if __name__ == '__main__':
    print( convert_date(example_date))