import pandas as pd
def get_row_letter(number):
    return chr(ord('A') + number)

def get_list_of_row_letters(number):
    return [(get_row_letter(int((i-26)/26)) if i>=26 else '')+get_row_letter(i%26) for i in range(number)]
