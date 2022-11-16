import streamlit as st
from utils import tools

st.set_page_config(page_title="Text Tools - Cyrillic to Latin", page_icon="📖")
st.image('logo.png', width=300)
st.title("Cyrillic to Latin and Latin to Cyrillic")
st.write("cyrillic to latin & latin to cyrillic")

option = st.selectbox(
            'Choose Text Transformatino?',
            ('Cyrillic to Latin',
            'Latin to Cyrillic'))

text_area = st.empty()

input_text = text_area.text_area("Your text here:")

with st.expander("Upload a file"):
    file = st.file_uploader("")
submit = st.button('Process Text')

if file:
    input_text = text_area.text_area("Text to analyze", file.read().decode("utf-8"))

if input_text:
    st.text('Result:')

    if option == 'Cyrillic to Latin':
        transformed_text = tools.cyr_to_latin(input_text)
    elif option == 'Latin to Cyrillic':
        transformed_text = tools.latin_to_cyr(input_text)

    
    st.code(transformed_text)