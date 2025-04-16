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

# Define these at the top level as Streamlit session state
if 'generating' not in st.session_state:
    st.session_state.generating = False
if 'loading' not in st.session_state:
    st.session_state.loading = False

uploaded_file = st.file_uploader("Choose a file", type=["pdf"])


# Main container
container = st.container(border=True)

st.caption("<p>Built by <a href='https://www.hanif.one'>Hanif</a> and <a href='https://www.analyticsvidhya.com/blog/author/maigari74807/'>Maigari David</a></p>", unsafe_allow_html=True,)

def start_generating():
    """
    Sets the generating flag to True to initiate PDF compression.
    This triggers the compression process when the user clicks the button.
    """
    st.session_state.generating = True
    st.session_state.loading = True


if uploaded_file is not None:
     if st.session_state.loading:
          st.spinner("Processing file...")
          
     col1, col2 = container.columns(2)
     
     with col1:
          # add slider to set Zoom in x direction
          zoom_x = st.slider("Zoom percentage x", min_value=0, max_value=100, value=75)
     
     with col2:
          # add slider to set Zoom in y direction
          zoom_y = st.slider("Zoom percentage y", min_value=0, max_value=100, value=75)
     
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     
     file_name : str = uploaded_file.name
     file_size : str = f"{uploaded_file.size / 1024:.2f} KB"  
     
     # left, middle, right = st.columns(3)
     container.button(
          "Compress PDF", 
          disabled=False, 
          type="primary", 
          on_click=start_generating,
          use_container_width=True
     )
    
     if st.session_state.generating:
          with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
               tmp_file.write(bytes_data)
               input_temp_path = tmp_file.name
          
          output_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=f'{file_name}-compressed.pdf').name
                    

          try:
               compress_pdf(input_temp_path, output_pdf, zoom_x= zoom_x if zoom_x else 0.75, zoom_y=zoom_y if zoom_y else 0.75)
               
               if os.path.getsize(output_pdf) >= uploaded_file.size:
                    raise Exception("Compression failed - Output file is larger than input file, tweak the parameters and try again")
               
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
               message = str(e) if str(e) else "Could not Compress this file, please try again with another file."
               container.error(message, icon=":material/error:")
               print(f"Error processing {input_temp_path}: {message}")


