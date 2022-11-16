import streamlit as st
from utils import tools

st.set_page_config(page_title="Text Tools", page_icon="📖")
st.title("Encode or Decode Text")
st.write("base64 encode text, base64 decode text")

option = st.selectbox(
            'Choose Text Transformatino:',
            ( 'Base64 Encode Text',
            'Base64 Decode Text'))
# input_text = st.text_area('Your text here')

text_area = st.empty()

input_text = text_area.text_area("Your text here:")
with st.expander("Upload a file"):
    file = st.file_uploader("")
submit = st.button('Process Text')

if file:
    input_text = text_area.text_area("Your text here:", file.read().decode("utf-8"))
if input_text:
    st.text('Result:')
    if option == 'Base64 Encode Text':
        transformed_text = tools.base64_encode(input_text)
    elif option == 'Base64 Decode Text':
        transformed_text = tools.base64_decode(input_text)       
    st.code(transformed_text)