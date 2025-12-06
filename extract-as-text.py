#!/usr/bin/env python3
"""
PDF Text Extraction Script

Extracts all text from a PDF file and saves it to a text file.
"""

import sys
import os
from pathlib import Path

try:
    import PyPDF2
except ImportError:
    print("Error: PyPDF2 is not installed. Please run: pip install -r requirements.txt")
    sys.exit(1)


def extract_pdf_text(pdf_path):
    """
    Extract text from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        str: Extracted text from all pages
        
    Raises:
        FileNotFoundError: If the PDF file doesn't exist
        PyPDF2.errors.PdfReadError: If the PDF cannot be read
    """
    pdf_file = Path(pdf_path)
    
    # Validate file exists
    if not pdf_file.exists():
        raise FileNotFoundError(f"Error: File '{pdf_path}' not found.")
    
    # Validate it's a PDF file
    if pdf_file.suffix.lower() != '.pdf':
        raise ValueError(f"Error: '{pdf_path}' is not a PDF file (expected .pdf extension).")
    
    # Extract text from PDF
    extracted_text = []
    num_pages = 0
    
    try:
        with open(pdf_file, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Check if PDF is encrypted
            if pdf_reader.is_encrypted:
                raise ValueError("Error: PDF is encrypted and cannot be read.")
            
            # Extract text from each page
            num_pages = len(pdf_reader.pages)
            print(f"Processing {num_pages} page(s)...")
            
            for page_num, page in enumerate(pdf_reader.pages, start=1):
                try:
                    page_text = page.extract_text()
                    extracted_text.append(page_text)
                except Exception as e:
                    print(f"Warning: Could not extract text from page {page_num}: {e}")
                    extracted_text.append("[Text extraction failed for this page]")
    
    except PyPDF2.errors.PdfReadError as e:
        raise PyPDF2.errors.PdfReadError(f"Error: Cannot read PDF file. {e}")
    except Exception as e:
        raise Exception(f"Error reading PDF file: {e}")
    
    # Join pages with clear separators
    separator = "\n" + "=" * 60 + "\n"
    result_pages = []
    
    for page_num, page_text in enumerate(extracted_text, start=1):
        page_header = f"Page {page_num} of {num_pages}"
        result_pages.append(f"{separator}{page_header}{separator}\n{page_text}")
    
    return "\n".join(result_pages)


def main():
    """Main function to handle command-line arguments and execute extraction."""
    # Check for command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 extract-as-text.py <pdf_file>")
        print("Example: python3 extract-as-text.py document.pdf")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    
    try:
        # Extract text from PDF
        print(f"Extracting text from '{pdf_path}'...")
        text = extract_pdf_text(pdf_path)
        
        # Generate output filename
        pdf_file = Path(pdf_path)
        output_file = pdf_file.with_suffix('.txt')
        
        # Save extracted text to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        
        print(f"Successfully extracted text to '{output_file}'")
        print(f"Extracted {len(text)} characters from the PDF.")
        
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)
    except PyPDF2.errors.PdfReadError as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

