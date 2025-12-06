# Extract PDF

## Installation

1. Install the required dependencies:

```bash
python3 -m venv <virtual_environment_name>
source <virtual_environment_name>/bin/activate
pip install -r requirements.txt
```

This will install PyPDF2, which is used for PDF text extraction.

## Extract PDF into txt script

### Description

Small Python 3 script created to extract PDF contents as text. The script reads a PDF file and extracts all text content, saving it to a text file with the same name. Each page is clearly separated in the output file with page headers and separators.

## Usage

Run the script with the PDF file path as an argument:

```bash
python3 extract-as-text.py <pdf_file> [--signature-filter]
```

### Basic Usage (without signature filter)

```bash
python3 extract-as-text.py document.pdf
```

This will extract all text from `document.pdf` and save it to `document.txt` in the same directory. Each page will be clearly separated with headers showing the page number.

### Usage with signature Filter

To automatically remove content that appears identically in 10 or more consecutive pages (likely signatures):

```bash
python3 extract-as-text.py document.pdf --signature-filter
```

Or use the short form:

```bash
python3 extract-as-text.py document.pdf -sf
```

The signature filter detects and removes content that appears exactly the same across 10 or more consecutive pages, which is typically indicative of signatures, headers, or footers that repeat across multiple pages.

### Notes

- The script will create a `.txt` file with the same name as the input PDF file
- The output file will be saved in the same directory as the input PDF
- Encrypted PDFs are not supported
- The script processes all pages in the PDF and extracts text from each page
- Each page in the output file is clearly separated with visual separators and page numbers
- The signature filter is optional and disabled by default