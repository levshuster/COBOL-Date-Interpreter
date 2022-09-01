import streamlit as st
import pandas as pd

from convert import bulk_convert_date, convert_date

# SETUP

icon = '📅'
title = "COBOL Date Converter"
st.set_page_config(page_title=title, page_icon=icon)
st.title(f'{icon} {title}')


# INPUT
text_input = st.text_area("Enter a COBOL date", placeholder='EX C20531')
uploaded_file = st.file_uploader("Or upload a excel/csv file", type=["csv", "xlsx"])


# PASTE OPTION

left, right = st.columns(2)
format = True if right.radio("Select a date format", ("MM-DD-YY", "Month DD YYYY")) == "MM-DD-YY" else False
result = ''
def list_to_multiline_string(list):
    if not list[0]: return
    global result 
    result = list
left.button("Convert", on_click=list_to_multiline_string(bulk_convert_date(text_input, format)))

# UPLOAD OPTION

# if uploaded_file: uploaded_file.getvalue()
# if uploaded_file: T1 = pd.read_excel(uploaded_file).to_numpy().tolist() if uploaded_file.name.endswith('xlsx') else pd.read_csv(uploaded_file).to_numpy().tolist()
# T2 = []
# for row in T1:
#     T2.append([convert_date(date, format) for date in row])
# df = pd.DataFrame(T2)
# st.write(df)


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