# Extract PDF

## Description

Small Python 3 script created to extract PDF contents as text. The script reads a PDF file and extracts all text content, saving it to a text file with the same name.

## Installation

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

This will install PyPDF2, which is used for PDF text extraction.

## Usage

Run the script with the PDF file path as an argument:

```bash
python3 extract-as-text.py <pdf_file>
```

### Example

```bash
python3 extract-as-text.py document.pdf
```

This will extract all text from `document.pdf` and save it to `document.txt` in the same directory.

### Notes

- The script will create a `.txt` file with the same name as the input PDF file
- The output file will be saved in the same directory as the input PDF
- Encrypted PDFs are not supported
- The script processes all pages in the PDF and extracts text from each page