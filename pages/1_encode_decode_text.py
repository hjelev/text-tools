import streamlit as st
from utils import tools

st.set_page_config(page_title="Text Tools - Encode or Decode", page_icon="📖")
st.title("Encode or Decode Text")
st.write("encode text to base64, decode base64 to text")

option = st.selectbox(
            'Choose Text Transformatino:',
            ( 'Encode Text to Base64',
            'Decode Base64 to Text'))
# input_text = st.text_area('Your text here')

text_area = st.empty()

input_text = text_area.text_area("Your text here:")
with st.expander("Upload a file"):
    file = st.file_uploader("")
submit = st.button('Process')

if file:
    input_text = text_area.text_area("Your text here:", file.read().decode("utf-8"))
if input_text:
    st.text('Result:')
    if option == 'Encode Text to Base64':
        transformed_text = tools.base64_encode(input_text)
    elif option == 'Decode Base64 to Text':
        transformed_text = tools.base64_decode(input_text)       
    st.code(transformed_text)