# PDF Compression Tool

<img width="641" alt="image" src="https://github.com/user-attachments/assets/81516247-465c-4fec-b044-07aae689a414" />


A lightweight Python tool to compress PDF files while maintaining readability. Reduce PDF file sizes by up to 70% or more!

## Features

- Reduces PDF file size while preserving content
- Adjustable compression levels
- Simple command-line interface
- Preserves text readability
- Fast processing of multi-page documents

## Installation

1. **Install Python** (version 3.7 or higher)

   - Download from [python.org](https://www.python.org/downloads/)
   - Verify installation: `python --version`

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**

   - Create a `.env` file in the project root
   - Add your file paths:
     ```
     FILE_LOCATION="/path/to/your/files/"
     FILE_NAMES="file1.pdf,file2.pdf,file3.pdf"
     ```
     ```

     ```

4. **Run the compression tool**
   ```bash
   python compress.py
   ```

## Usage

Edit the `.env` file to specify your input and output paths, then run the script. The compressed PDF will be saved at your specified output location.

> Note: For best results, start with default compression settings (50%) and adjust as needed.
