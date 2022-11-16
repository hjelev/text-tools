import streamlit as st
from utils import tools

st.set_page_config(page_title="Text Tools", page_icon="📖")
st.title("Text Tools")
st.write("remove empty lines, remove duplicate lines, remove whitespace")

option = st.selectbox(
            'Choose Text Transformatino?',
            ( 'Remove Empty Lines', 
            'Remove Duplicate Lines',
            'Remove Whitespace',
            ))

text_area = st.empty()

input_text = text_area.text_area("Your text here:")

with st.expander("Upload a file"):
    file = st.file_uploader("")
submit = st.button('Process Text')

if file:
    input_text = text_area.text_area("Your text here:", file.read().decode("utf-8"))

if input_text:
    st.text('Result:')
    if option == 'Remove Empty Lines':
        transformed_text = tools.remove_empty_lines(input_text)
    elif option == 'Remove Duplicate Lines':
        transformed_text = tools.remove_duplicate_lines(input_text)
    elif option == 'Remove Whitespace':
        transformed_text = tools.strip_text(input_text)   
    st.code(transformed_text)