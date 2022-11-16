import streamlit as st
from utils import tools

st.set_page_config(page_title="Text Tools", page_icon="📖")
st.image('logo.png', width=300)
# st.title("Text Tools")
st.write("remove empty lines, remove duplicate lines, base64 encode text, base64 decode text, sort lines, sort lines reversed")

# option = st.selectbox(
#             'Choose Text Transformatino?',
#             ( 'Remove Empty Lines', 
#             'Remove Duplicate Lines',
#             'Base64 Encode Text',
#             'Base64 Decode Text',
#             'Sort Lines', 
#             'Sort Lines Reversed'))

# text_area = st.empty()

# input_text = text_area.text_area("Your text here:")

# with st.expander("Upload a file"):
#     file = st.file_uploader("")
# submit = st.button('Process Text')

# if file:
#     input_text = text_area.text_area("Your text here:", file.read().decode("utf-8"))

# if input_text:
#     st.text('Result:')
#     if option == 'Remove Empty Lines':
#         transformed_text = tools.remove_empty_lines(input_text)
#     elif option == 'Remove Duplicate Lines':
#         transformed_text = tools.remove_duplicate_lines(input_text)
#     elif option == 'Sort Lines Reversed':
#         transformed_text = tools.sort_reversed(input_text)
#     elif option == 'Sort Lines':
#         transformed_text = tools.sort(input_text)
#     elif option == 'Base64 Encode Text':
#         transformed_text = tools.base64_encode(input_text)
#     elif option == 'Base64 Decode Text':
#         transformed_text = tools.base64_decode(input_text)       
#     st.code(transformed_text)