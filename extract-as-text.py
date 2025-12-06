#!/usr/bin/env python3
"""
PDF Text Extraction Script

Extracts all text from a PDF file and saves it to a text file.
"""

import sys
import os
import argparse
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
        tuple: (list of page texts, total number of pages)
        
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
    
    return extracted_text, num_pages


def apply_signature_filter(page_texts, consecutive_threshold=10):
    """
    Remove content that appears identically in consecutive pages (likely signatures).
    
    Args:
        page_texts (list): List of page text strings
        consecutive_threshold (int): Number of consecutive pages with identical content to trigger filtering
        
    Returns:
        list: Filtered page texts with signatures removed
    """
    if len(page_texts) < consecutive_threshold:
        return page_texts
    
    filtered_texts = page_texts.copy()
    
    # Find sequences of identical content
    i = 0
    while i < len(filtered_texts) - consecutive_threshold + 1:
        # Check if the next 'consecutive_threshold' pages have identical content
        current_text = filtered_texts[i].strip()
        
        # Skip if this page is empty or is an error message
        if not current_text or current_text == "[Text extraction failed for this page]":
            i += 1
            continue
        
        # Check if the next consecutive_threshold-1 pages match
        all_match = True
        for j in range(1, consecutive_threshold):
            if i + j >= len(filtered_texts):
                all_match = False
                break
            if filtered_texts[i + j].strip() != current_text:
                all_match = False
                break
        
        if all_match:
            # This content appears in at least consecutive_threshold pages - likely a signature
            # Find the full extent of the matching sequence
            end_index = i + consecutive_threshold
            while end_index < len(filtered_texts):
                if filtered_texts[end_index].strip() == current_text:
                    end_index += 1
                else:
                    break
            
            # Remove the signature content from all matching pages
            start_page = i + 1
            end_page = end_index
            print(f"signature detected: Removing identical content found in pages {start_page} to {end_page}")
            
            for j in range(i, end_index):
                filtered_texts[j] = ""  # Clear the signature content
            
            # Skip ahead past the matched pages
            i = end_index
        else:
            i += 1
    
    return filtered_texts


def format_output(page_texts, num_pages):
    """
    Format page texts with separators for output.
    
    Args:
        page_texts (list): List of page text strings
        num_pages (int): Total number of pages
        
    Returns:
        str: Formatted text with page separators
    """
    separator = "\n" + "=" * 60 + "\n"
    result_pages = []
    
    for page_num, page_text in enumerate(page_texts, start=1):
        page_header = f"Page {page_num} of {num_pages}"
        result_pages.append(f"{separator}{page_header}{separator}\n{page_text}")
    
    return "\n".join(result_pages)


def main():
    """Main function to handle command-line arguments and execute extraction."""
    parser = argparse.ArgumentParser(
        description="Extract text from a PDF file and save it to a text file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Example: python3 extract-as-text.py document.pdf --signature-filter"
    )
    parser.add_argument(
        'pdf_file',
        help='Path to the PDF file to extract text from'
    )
    parser.add_argument(
        '--signature-filter',
        '-sf',
        action='store_true',
        help='Enable signature filter: removes content that appears identically in 10 consecutive pages'
    )
    
    args = parser.parse_args()
    pdf_path = args.pdf_file
    
    try:
        # Extract text from PDF
        print(f"Extracting text from '{pdf_path}'...")
        page_texts, num_pages = extract_pdf_text(pdf_path)
        
        # Apply signature filter if enabled
        if args.signature_filter:
            print("Applying signature filter...")
            page_texts = apply_signature_filter(page_texts, consecutive_threshold=10)
        
        # Format output with page separators
        text = format_output(page_texts, num_pages)
        
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

