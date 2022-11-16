import streamlit as st
from utils import tools

st.set_page_config(page_title="Text Tools - Convert Case", page_icon="📖")
st.image('logo.png', width=300)
st.title("Convert Case")
st.write("convert text to upper, lower or title case")

option = st.selectbox(
            'Choose Text Transformatino?',
            ('To Upper Case', 
            'To Lower Case',
            'To Title Case'))

text_area = st.empty()

input_text = text_area.text_area("Your text here:")

with st.expander("Upload a file"):
    file = st.file_uploader("")
submit = st.button('Process Text')

if file:
    input_text = text_area.text_area("Text to analyze", file.read().decode("utf-8"))

if input_text:
    st.text('Result:')

    if option == 'To Upper Case':
        transformed_text = input_text.upper()
    elif option == 'To Lower Case':
        transformed_text = input_text.lower()
    elif option == 'To Title Case':
        transformed_text = input_text.title()
    st.code(transformed_text)