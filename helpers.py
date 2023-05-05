get_row_letter = lambda number: chr(ord('A') + number)

get_list_of_row_letters = lambda number: [
	(get_row_letter(int((i-26)/26)) if i>=26 else '')
	+ get_row_letter(i%26) for i in range(number)]
