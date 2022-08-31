import streamlit as st
from convert import bulk_convert_date

st.set_page_config(
    page_title="COBOL Date Converter", 
    page_icon="📅", 
    initial_sidebar_state="auto")
    
st.title("📅 COBOL Date Converter")
left, right = st.columns(2)

input = st.text_area("Enter a COBOL date", placeholder='EX C20531')
format = True if right.radio("Select a date format", ("MM-DD-YY", "Month DD YYYY")) == "MM-DD-YY" else False

result = ''
def list_to_multiline_string(list):
    if not list[0]: return
    global result 
    result = list
left.button("Convert", on_click=list_to_multiline_string(bulk_convert_date(input, format)))

if result: st.write(f"""---\n## Result\n""")
for line in result: st.write(line)

st.write("""
---

## How to Read COBOL Dates
""")