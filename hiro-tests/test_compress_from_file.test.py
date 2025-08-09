import os
from compress import compress_pdf
from dotenv import load_dotenv
from unittest.mock import patch, MagicMock
import unittest

class TestCompressFromFilePath(unittest.TestCase):
    @patch('dotenv.load_dotenv')
    @patch('os.getenv')
    def test_compress_from_file(self, mock_getenv, mock_load_dotenv):
        mock_getenv.side_effect = ['Folder Location', 'File.pdf, File-2.pdf, File-3.pdf']
        mock_load_dotenv.return_value = None
        with patch('builtins.print') as mock_print:
            with patch('compress.compress_pdf') as mock_compress_pdf:
                from compress_from_file import main
                main()
                mock_compress_pdf.assert_called()
                self.assertEqual(mock_print.call_count, 6)

    @patch('dotenv.load_dotenv')
    @patch('os.getenv')
    def test_compress_from_file_empty_file_names(self, mock_getenv, mock_load_dotenv):
        mock_getenv.side_effect = ['Folder Location', '']
        mock_load_dotenv.return_value = None
        with self.assertRaises(ValueError):
            from compress_from_file import main
            main()

    @patch('dotenv.load_dotenv')
    @patch('os.getenv')
    def test_compress_from_file_non_pdf_file(self, mock_getenv, mock_load_dotenv):
        mock_getenv.side_effect = ['Folder Location', 'File.pdf, File-2.txt']
        mock_load_dotenv.return_value = None
        with patch('builtins.print') as mock_print:
            with patch('compress.compress_pdf') as mock_compress_pdf:
                from compress_from_file import main
                main()
                mock_compress_pdf.assert_called_once()
                self.assertEqual(mock_print.call_count, 2)

if __name__ == '__main__':
    unittest.main()