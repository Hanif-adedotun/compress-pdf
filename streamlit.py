"""
# Streamlit file compression app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import tempfile
from compress import compress_pdf
import os 

st.markdown("<h1 style='text-align: center;'>Compress your PDF files lightning fast ⚡ </h1>", unsafe_allow_html=True)

# Set loading variable
loading = False;

uploaded_file = st.file_uploader("Choose a file", type="pdf")
loading = True;

# Main container
container = st.container(border=True)

st.caption("<p>Built by <a href='https://www.hanif.one'>Hanif</a> and <a href='https://www.analyticsvidhya.com/blog/author/maigari74807/'>Maigari David</a></p>", unsafe_allow_html=True,)

if uploaded_file is not None:
     if loading:
          st.spinner("Processing file...")
     
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     
     file_name : str = uploaded_file.name
     file_size : str = f"{uploaded_file.size / 1024:.2f} KB"  
    
     with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
          tmp_file.write(bytes_data)
          input_temp_path = tmp_file.name
     
     output_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=f'{file_name}-compressed.pdf').name
     
     try:
          compress_pdf(input_temp_path, output_pdf, zoom_x=0.75, zoom_y=0.75)
          # loading = False;
          
          output_file_size = f"{os.path.getsize(output_pdf)/1024:.2f} KB"
          
          container.info(f"Input file Size: {file_size}")
          container.info(f"Output file Size: {output_file_size}")
          
          # Add download button for the compressed file
          with open(output_pdf, "rb") as file:
               container.download_button(
                    label="Download Compressed Pdf",
                    data=file,
                    file_name=f"{file_name}-compressed.pdf",
                    mime="application/pdf",
                    icon=":material/download:"
               )
               
     except Exception as e:
          container.error("Could not Compress this file, please try again with another file.", icon=":material/error:")
          print(f"Error processing {input_temp_path}: {str(e)}")


