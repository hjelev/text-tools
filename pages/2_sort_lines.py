import streamlit as st
from utils import tools

st.set_page_config(page_title="Text Tools - Sort Lines", page_icon="📖")
st.title("Sort Lines")
st.write("sort lines, sort lines reversed")

option = st.selectbox(
            'Choose Text Transformatino?',
            ('Sort Lines', 
            'Sort Lines Reversed'))

text_area = st.empty()

input_text = text_area.text_area("Your text here:")

with st.expander("Upload a file"):
    file = st.file_uploader("")
submit = st.button('Sort Lines')

if file:
    input_text = text_area.text_area("Text to analyze", file.read().decode("utf-8"))

if input_text:
    st.text('Result:')

    if option == 'Sort Lines Reversed':
        transformed_text = tools.sort_reversed(input_text)
    elif option == 'Sort Lines':
        transformed_text = tools.sort(input_text)
    
    st.code(transformed_text)