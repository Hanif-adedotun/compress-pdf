"""
# Streamlit file compression app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import tempfile
from compress import compress_pdf

st.title("Compress your PDF files lightining fast")

# Set loading variable
loading = False;

# with st.spinner("Wait for it...", show_time=True):
#     time.sleep(5)
# st.success("Done!")

uploaded_file = st.file_uploader("Choose a file", type="pdf")
if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     # st.write(bytes_data)
    
     with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
          tmp_file.write(bytes_data)
          temp_path = tmp_file.name
    
     st.write(f"Temporary file path: {temp_path}")
     
     
    
    
#     temp_path = uploaded_file.

