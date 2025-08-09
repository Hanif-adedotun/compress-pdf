import unittest
from compress import compress_pdf
import os
import fitz
import tempfile

class TestCompressPDF(unittest.TestCase):
    def test_compress_pdf(self):
        # Arrange
        input_path = 'test.pdf'
        output_path = 'test-compressed.pdf'
        zoom_x = 0.5
        zoom_y = 0.5
        
        # Create a test PDF file
        with tempfile.TemporaryDirectory() as tmpdirname:
            test_pdf_path = os.path.join(tmpdirname, input_path)
            with open(test_pdf_path, 'wb') as f:
                # Create a simple PDF using fitz
                doc = fitz.open()
                page = doc.new_page()
                doc.save(f)
                doc.close()
            
            # Act
            compress_pdf(test_pdf_path, output_path, zoom_x, zoom_y)
            
            # Assert
            self.assertTrue(os.path.exists(output_path))
            self.assertGreater(os.path.getsize(test_pdf_path), os.path.getsize(output_path))
        
    def test_compress_pdf_invalid_input(self):
        # Arrange
        input_path = 'invalid.pdf'
        output_path = 'test-compressed.pdf'
        zoom_x = 0.5
        zoom_y = 0.5
        
        # Act and Assert
        with self.assertRaises(Exception):
            compress_pdf(input_path, output_path, zoom_x, zoom_y)
        
    def test_compress_pdf_invalid_zoom(self):
        # Arrange
        input_path = 'test.pdf'
        output_path = 'test-compressed.pdf'
        zoom_x = 2
        zoom_y = 2
        
        # Create a test PDF file
        with tempfile.TemporaryDirectory() as tmpdirname:
            test_pdf_path = os.path.join(tmpdirname, input_path)
            with open(test_pdf_path, 'wb') as f:
                # Create a simple PDF using fitz
                doc = fitz.open()
                page = doc.new_page()
                doc.save(f)
                doc.close()
            
            # Act and Assert
            with self.assertRaises(Exception):
                compress_pdf(test_pdf_path, output_path, zoom_x, zoom_y)
        
if __name__ == '__main__':
    unittest.main()