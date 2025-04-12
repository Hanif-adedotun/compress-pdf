import os
from compress import compress_pdf
# Load environment variables
# Get file paths from .env
from dotenv import load_dotenv
load_dotenv('.env')

if __name__ == "__main__":

    file_location = os.getenv("FILE_LOCATION")
    file_names = os.getenv("FILE_NAMES")
    
    if not file_names:
        raise ValueError("FILE_NAMES must be specified in .env file")
    
    # Split file names by comma and strip whitespace
    files = [f.strip() for f in file_names.split(",")]
    
    # Process each file
    for file_name in files:
        if not file_name.endswith(".pdf"):
            print(f"Skipping non-PDF file: {file_name}")
            continue
            
        input_pdf = os.path.join(file_location, file_name)
        output_pdf = os.path.join(file_location, file_name.replace(".pdf", "-compressed.pdf"))
        
        try:
            # Adjust zoom factors to control compression (0.5 = 50% size)
            compress_pdf(input_pdf, output_pdf, zoom_x=0.75, zoom_y=0.75)
        except Exception as e:
            print(f"Error processing {file_name}: {str(e)}")