import unittest
from unittest.mock import patch, MagicMock
from streamlit import session_state
import streamlit as st
from compress import compress_pdf
import os
import tempfile

class TestStreamlitApp(unittest.TestCase):
    def setUp(self):
        self.uploaded_file = MagicMock()
        self.uploaded_file.name = 'test_pdf.pdf'
        self.uploaded_file.size = 1024
        self.uploaded_file.getvalue = lambda: b'pdf_content'
        session_state.generating = False
        session_state.loading = False

    @patch('streamlit.button')
    @patch('compress.compress_pdf')
    def test_compress_pdf(self, mock_compress_pdf, mock_button):
        mock_button.return_value = True
        st.file_uploader = lambda *args, **kwargs: self.uploaded_file
        exec(open('streamlit.py').read())
        self.assertTrue(session_state.generating)
        self.assertTrue(session_state.loading)
        mock_compress_pdf.assert_called_once()

    @patch('streamlit.button')
    @patch('compress.compress_pdf')
    def test_compress_pdf_failure(self, mock_compress_pdf, mock_button):
        mock_button.return_value = True
        mock_compress_pdf.side_effect = Exception('Test error')
        st.file_uploader = lambda *args, **kwargs: self.uploaded_file
        exec(open('streamlit.py').read())
        self.assertTrue(session_state.generating)
        self.assertTrue(session_state.loading)
        mock_compress_pdf.assert_called_once()
        self.assertEqual(session_state.generating, False)

    @patch('streamlit.file_uploader')
    def test_no_file_uploaded(self, mock_file_uploader):
        mock_file_uploader.return_value = None
        exec(open('streamlit.py').read())
        self.assertFalse(session_state.generating)
        self.assertFalse(session_state.loading)
