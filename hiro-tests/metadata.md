This code tests the '.env' file to ensure that the 'FILE_LOCATION' and 'FILE_NAMES' environment variables are correctly set. The `load_dotenv` function from the `dotenv` library is used to load the environment variables from the '.env' file. The `unittest` framework is used to write and run the tests.

## Required Packages
- unittest
- dotenv
This test case checks if the maxUploadSize is set to 800 as defined in the config.toml file. The test case uses the unittest framework and asserts that the maxUploadSize is equal to 800.

## Required Packages
- unittest
### Test Cases for `compress.py` File
*   `test_compress_pdf`: Test the core functionality of `compress_pdf` function.
*   `test_compress_pdf_invalid_input`: Test the error handling of `compress_pdf` function when the input file does not exist.
*   `test_compress_pdf_invalid_zoom`: Test the error handling of `compress_pdf` function when the zoom factors are invalid.

## Required Packages
- unittest
- tempfile
- fitz
### Test Cases for `compress_from_file.py`

The following test cases cover the main functionality of the `compress_from_file.py` script.

* `test_compress_from_file`: Tests the main function of the script, which compresses PDF files specified in the `.env` file.
* `test_compress_from_file_empty_file_names`: Tests that a `ValueError` is raised when the `FILE_NAMES` environment variable is empty.
* `test_compress_from_file_non_pdf_file`: Tests that non-PDF files are skipped and a message is printed to the console.

## Required Packages
- unittest
- mock
## Test Cases for Streamlit App
The following tests are designed to verify the correctness of the Streamlit app.
### Test 1: File Uploader
*   Test that the file uploader returns the uploaded file.
### Test 2: Compress PDF
*   Test that the compress_pdf function is called with the correct parameters.
### Test 3: File Path
*   Test that the file path is correctly constructed using os.path.join.


## Required Packages
- unittest
- unittest.mock
- os
- pandas
- streamlit
- tempfile
- compress
```markdown
## Test Cases for Streamlit App
The following test cases cover the main functionality of the Streamlit app.
### Test 1: Compress PDF
*   Test that the `compress_pdf` function is called when the button is clicked.
*   Test that the `session_state.generating` and `session_state.loading` flags are set to True.
### Test 2: Compress PDF Failure
*   Test that the `compress_pdf` function is called when the button is clicked.
*   Test that the `session_state.generating` and `session_state.loading` flags are set to True.
*   Test that an error message is displayed when the compression fails.
### Test 3: No File Uploaded
*   Test that the `session_state.generating` and `session_state.loading` flags are not set when no file is uploaded.
```


## Required Packages
- unittest
- streamlit
- compress
