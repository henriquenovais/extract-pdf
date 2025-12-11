"""
PDF Text Extraction Script

Extracts all text from a PDF file and saves it to a text or markdown file.
"""

import sys
import os
import argparse
from pathlib import Path
from collections import Counter
import re

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


def find_signature_patterns(page_texts, min_consecutive_pages=20, min_length=20):
    """
    Find text patterns that appear in consecutive pages (likely signatures/headers/footers).
    
    Args:
        page_texts (list): List of page text strings
        min_consecutive_pages (int): Minimum number of consecutive pages a pattern must appear on to be considered a signature
        min_length (int): Minimum length of text to be considered a signature pattern
        
    Returns:
        list: List of signature patterns to remove
    """
    if len(page_texts) < min_consecutive_pages:
        return []
    
    # Extract all potential signature lines from all pages
    all_lines = set()
    for page_text in page_texts:
        if page_text and page_text != "[Text extraction failed for this page]":
            lines = [line.strip() for line in page_text.split('\n') if line.strip()]
            for line in lines:
                if len(line) >= min_length:
                    all_lines.add(line)
    
    signature_patterns = []
    
    # Check each potential signature line
    for line in all_lines:
        # Find all pages where this line appears (check if line is contained in page text)
        pages_with_line = []
        for page_idx, page_text in enumerate(page_texts):
            if page_text and page_text != "[Text extraction failed for this page]":
                # Check if the line appears anywhere in the page text
                if line in page_text:
                    pages_with_line.append(page_idx)
        
        if not pages_with_line:
            continue
        
        # Find the longest consecutive sequence
        max_consecutive = 1
        current_consecutive = 1
        
        for i in range(1, len(pages_with_line)):
            if pages_with_line[i] == pages_with_line[i-1] + 1:
                # Consecutive pages
                current_consecutive += 1
                max_consecutive = max(max_consecutive, current_consecutive)
            else:
                # Gap found, reset counter
                current_consecutive = 1
        
        # If this line appears in enough consecutive pages, it's a signature
        if max_consecutive >= min_consecutive_pages:
            signature_patterns.append(line)
    
    # Sort by length (longest first) to remove longer patterns first
    signature_patterns.sort(key=len, reverse=True)
    
    return signature_patterns

def apply_signature_filter(page_texts, min_consecutive_pages=20, min_length=20):
    """
    Remove signature patterns that appear in consecutive pages.
    
    Args:
        page_texts (list): List of page text strings
        min_consecutive_pages (int): Minimum number of consecutive pages a pattern must appear on to be considered a signature
        min_length (int): Minimum length of text to be considered a signature pattern
        
    Returns:
        list: Filtered page texts with signatures removed
    """
    if len(page_texts) < min_consecutive_pages:
        return page_texts
    
    # Find signature patterns
    signature_patterns = find_signature_patterns(page_texts, min_consecutive_pages, min_length)
    
    if not signature_patterns:
        print("No signature patterns detected.")
        return page_texts
    
    print(f"Detected {len(signature_patterns)} signature pattern(s):")
    for i, pattern in enumerate(signature_patterns, 1):
        # Truncate long patterns for display
        display_pattern = pattern[:100] + "..." if len(pattern) > 100 else pattern
        print(f"  {i}. \"{display_pattern}\"")
    
    # Remove signature patterns from all pages
    filtered_texts = []
    total_removals = 0
    
    for page_num, page_text in enumerate(page_texts, start=1):
        if not page_text or page_text == "[Text extraction failed for this page]":
            filtered_texts.append(page_text)
            continue
        
        filtered_text = page_text
        page_removals = 0
        
        # Remove each signature pattern
        for pattern in signature_patterns:
            # Use regex to remove the pattern (case-sensitive, exact match)
            pattern_escaped = re.escape(pattern)
            old_text = filtered_text
            filtered_text = re.sub(pattern_escaped, '', filtered_text)
            
            # Count how many times the pattern was removed from this page
            removals = old_text.count(pattern) - filtered_text.count(pattern)
            page_removals += removals
        
        # Clean up extra whitespace and empty lines
        lines = [line.strip() for line in filtered_text.split('\n')]
        lines = [line for line in lines if line]  # Remove empty lines
        filtered_text = '\n'.join(lines)
        
        filtered_texts.append(filtered_text)
        total_removals += page_removals
    
    print(f"Removed {total_removals} signature occurrences across all pages.")
    return filtered_texts


def clean_text_for_markdown(text):
    """
    Clean text for markdown output without adding headers.
    
    Args:
        text (str): Raw text to clean
        
    Returns:
        str: Cleaned text
    """
    if not text or text == "[Text extraction failed for this page]":
        return text
    
    lines = text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        # Strip whitespace but preserve the line structure
        cleaned_line = line.rstrip()
        cleaned_lines.append(cleaned_line)
    
    # Join lines and clean up excessive empty lines
    result = '\n'.join(cleaned_lines)
    
    # Replace multiple consecutive empty lines with just two (for paragraph separation)
    result = re.sub(r'\n\s*\n\s*\n+', '\n\n', result)
    
    return result.strip()


def format_output_text(page_texts, num_pages):
    """
    Format page texts with separators for text output.
    
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


def format_output_markdown(page_texts, num_pages, pdf_filename):
    """
    Format page texts as markdown with simple structure.
    
    Args:
        page_texts (list): List of page text strings
        num_pages (int): Total number of pages
        pdf_filename (str): Original PDF filename for the title
        
    Returns:
        str: Formatted markdown text
    """
    # Create document title
    title = Path(pdf_filename).stem.replace('_', ' ').replace('-', ' ').title()
    result = [f"# {title}\n"]
    result.append(f"*Extracted from PDF: {pdf_filename}*\n")
    result.append(f"*Total pages: {num_pages}*\n")
    result.append("---\n")
    
    for page_num, page_text in enumerate(page_texts, start=1):
        # Add page break for pages after the first
        if page_num > 1:
            result.append("\n---\n")
        
        # Add page header as h2
        result.append(f"## Page {page_num}\n")
        
        # Clean text without adding automatic headers
        if page_text and page_text != "[Text extraction failed for this page]":
            cleaned_text = clean_text_for_markdown(page_text)
            result.append(cleaned_text)
        else:
            result.append("*[Text extraction failed for this page]*")
        
        result.append("\n")
    
    return "\n".join(result)


def main():
    """Main function to handle command-line arguments and execute extraction."""
    parser = argparse.ArgumentParser(
        description="Extract text from a PDF file and save it to a text or markdown file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=
        """Examples:
        python3 extract-contents.py document.pdf
        python3 extract-contents.py document.pdf --format markdown
        python3 extract-contents.py document.pdf --signature-filter --format md
        python3 extract-contents.py document.pdf --signature-filter --min-length 30 --format text
        python3 extract-contents.py document.pdf -sf -ml 25 -mp 10 -f md
        """
    )
    parser.add_argument(
        'pdf_file',
        help='Path to the PDF file to extract text from'
    )
    parser.add_argument(
        '--format',
        '-f',
        choices=['text', 'txt', 'markdown', 'md'],
        default='text',
        help='Output format: text/txt for plain text, markdown/md for markdown format (default: text)'
    )
    parser.add_argument(
        '--signature-filter',
        '-sf',
        action='store_true',
        help='Enable signature filter: removes text patterns that appear on consecutive pages (like headers/footers/signatures)'
    )
    parser.add_argument(
        '--min-length',
        '-ml',
        type=int,
        default=20,
        help='Minimum length of text to be considered a signature pattern (default: 20)'
    )
    parser.add_argument(
        '--min-pages',
        '-mp',
        type=int,
        default=20,
        help='Minimum number of consecutive pages a pattern must appear on to be considered a signature (default: 20)'
    )
    
    args = parser.parse_args()
    pdf_path = args.pdf_file
    output_format = args.format.lower()
    min_length = args.min_length
    min_pages = args.min_pages
    
    # Normalize format aliases
    if output_format in ['md', 'markdown']:
        output_format = 'markdown'
        file_extension = '.md'
    else:  # text, txt, or default
        output_format = 'text'
        file_extension = '.txt'
    
    # Validate arguments
    if min_length < 1:
        print("Error: Minimum length must be at least 1.")
        sys.exit(1)
    
    if min_pages < 1:
        print("Error: Minimum pages must be at least 1.")
        sys.exit(1)
    
    try:
        # Extract text from PDF
        print(f"Extracting text from '{pdf_path}'...")
        page_texts, num_pages = extract_pdf_text(pdf_path)
        
        # Apply signature filter if enabled
        if args.signature_filter:
            print(f"Applying signature filter (min length: {min_length}, min consecutive pages: {min_pages})...")
            page_texts = apply_signature_filter(page_texts, min_consecutive_pages=min_pages, min_length=min_length)
        
        # Format output based on chosen format
        print(f"Formatting output as {output_format}...")
        if output_format == 'markdown':
            formatted_text = format_output_markdown(page_texts, num_pages, Path(pdf_path).name)
        else:
            formatted_text = format_output_text(page_texts, num_pages)
        
        # Generate output filename
        pdf_file = Path(pdf_path)
        output_file = pdf_file.with_suffix(file_extension)
        
        # Save extracted text to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(formatted_text)
        
        print(f"Successfully extracted text to '{output_file}' ({output_format} format)")
        print(f"Extracted {len(formatted_text)} characters from the PDF.")
        
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