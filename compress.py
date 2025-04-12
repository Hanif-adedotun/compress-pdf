import pymupdf 
import os

def compress_pdf(input_path, output_path, zoom_x=0.5, zoom_y=0.5):
    """
    Compress a PDF file by scaling down its content
    :param input_path: Path to input PDF file
    :param output_path: Path to save compressed PDF
    :param zoom_x: Horizontal scaling factor (0-1)
    :param zoom_y: Vertical scaling factor (0-1)
    """
    try:
        # Open the PDF
        document = pymupdf.open(input_path)
        
        # Create a new PDF for output
        new_document = pymupdf.open()
        
        # Iterate through pages
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            # Create a transformation matrix for scaling
            mat = pymupdf.Matrix(zoom_x, zoom_y)
            # Get the pixmap (scaled image) of the page
            pix = page.get_pixmap(matrix=mat, alpha=False, dpi=72)
            # Convert to JPEG with quality setting using the correct method
            img_bytes = pix.pil_tobytes(format="JPEG", quality=70)  # Use pil_tobytes instead
            # Create a new page in the output document
            new_page = new_document.new_page(width=pix.width, height=pix.height)
            # Insert the JPEG image instead of raw pixmap
            new_page.insert_image(new_page.rect, stream=img_bytes)
        
        # Save the compressed PDF
        new_document.save(output_path)
        new_document.close()
        document.close()
        
        print(f"Compressed PDF saved to {output_path}")
        print(f"Original size: {os.path.getsize(input_path)/1024:.2f} KB")
        print(f"Compressed size: {os.path.getsize(output_path)/1024:.2f} KB")
        
    except Exception as e:
        print(f"Error compressing PDF: {str(e)}")