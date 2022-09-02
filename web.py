import streamlit as st
import pandas as pd


from convert import bulk_convert_date_new_line_deliminated, convert_date
from helpers import get_list_of_row_letters, get_row_letter

# SETUP

icon = '📅'
result = ''
title = "COBOL Date Converter"
st.set_page_config(page_title=title, page_icon=icon)
st.title(f'{icon} {title}')


# INPUT

file_selected = False
text_input = st.text_area("Enter a COBOL date", placeholder='EX C20531')
uploaded_file = st.file_uploader("Or upload a file", type=["csv", "xlsx"])

# UPLOAD OPTION

if uploaded_file and not text_input:
    st.write("""
    
    ---
    
    ## Select a Row or Column to Convert""")
    headers, page = st.columns(2)

    if uploaded_file.name.endswith('.csv'): df = pd.read_csv(uploaded_file)
    else: 
        df = pd.ExcelFile(uploaded_file.read()).parse()#.fillna('')
        # todo add support for multiple sheets
    useExcelHeader = headers.checkbox('Use Excel Headers', value=False)
    if useExcelHeader: df.columns = get_list_of_row_letters(df.shape[1])
    st.write(df)
    
    x, y = st.columns(2)
    xSelection = x.selectbox("Column", df.keys())
    ySelection:int = y.selectbox("Row", range(df.shape[0]))
    selectionAxes = "Row" if x.radio("Select a portion of a ", ("Column", "Row")) == "Column" else "Column"
    thirdVar = y.selectbox(f"Ending {selectionAxes}", df.keys() if selectionAxes == "Column" else range(df.shape[0]), key = selectionAxes)
    
    if selectionAxes == "Row": result = df[xSelection].tolist()[ySelection : thirdVar+1]
    else: result = df[[xSelection, thirdVar] if xSelection != thirdVar else xSelection].tolist()[ySelection]
    if type(result) is not list: result = [result]


# CONVERT

st.write("""---""")
left, right = st.columns(2)
format = True if right.radio("Select a date format", ("MM-DD-YY", "Month DD YYYY")) == "MM-DD-YY" else False

def list_to_multiline_string(list):
    if type(list) == list and not list[0]: return
    global result
    result = list

if uploaded_file and text_input: st.write("### Error: Please enter EITHER a date or upload a file")
elif uploaded_file: left.button("Convert", on_click=list_to_multiline_string(convert_date(cell, format) for cell in result))
else: left.button("Convert", on_click=list_to_multiline_string(bulk_convert_date_new_line_deliminated(text_input, format)))


# RESULT

if result: st.write(f"""---\n## Result\n""")
for line in result: st.write(line)

# EXPLANATION

st.write(f"""---

## How to Read COBOL Dates

Given a date like `C20531`, the first character is the decade, the second character is the year, the third and fourth characters are the month, and the last two characters are the day.

for example `C20531` is `{convert_date('C20531', format)}` because
- `C` represents the 12th decade after start of the 9th century (1900+120=2020)
- `2` represents the 2nd year of the decade (2020+2=2022)
- `05` represents the 5th month of the year (May)
- `31` represents the 31st day of the month""")