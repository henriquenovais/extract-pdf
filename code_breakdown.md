# Code Breakdown: extract-as-text.py

## Overview

This script extracts all text content from a PDF file and saves it to a text file. It uses the PyPDF2 library to read PDF files and process each page to extract text content.

## Script Structure

The script is organized into two main functions:
1. `extract_pdf_text()` - Core extraction logic
2. `main()` - Command-line interface and orchestration

---

## Line-by-Line Breakdown

### Shebang and Module Docstring (Lines 1-6)

```python
#!/usr/bin/env python3
"""
PDF Text Extraction Script

Extracts all text from a PDF file and saves it to a text file.
"""
```

- **Line 1**: The shebang (`#!/usr/bin/env python3`) allows the script to be executed directly on Unix-like systems. It ensures Python 3 is used.
- **Lines 2-6**: Module-level docstring providing a brief description of the script's purpose.

### Imports (Lines 8-16)

```python
import sys
import os
from pathlib import Path

try:
    import PyPDF2
except ImportError:
    print("Error: PyPDF2 is not installed. Please run: pip install -r requirements.txt")
    sys.exit(1)
```

**Standard Library Imports:**
- `sys`: Provides access to command-line arguments (`sys.argv`) and exit codes (`sys.exit()`)
- `os`: Included but not actively used (could be removed if not needed)
- `pathlib.Path`: Modern, object-oriented file path handling (more intuitive than `os.path`)

**Third-Party Import with Error Handling:**
- The `PyPDF2` import is wrapped in a try-except block to handle the case where the library is not installed
- If `PyPDF2` cannot be imported, the script prints a helpful error message and exits with code 1 (indicating failure)
- This provides better user experience than letting Python raise an unclear `ImportError`

---

## Function: `extract_pdf_text()` (Lines 19-71)

### Function Signature and Docstring (Lines 19-32)

```python
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
```

- **Purpose**: Core function that handles the PDF text extraction
- **Parameters**: Takes a single string argument `pdf_path` containing the file path
- **Returns**: A single string containing all extracted text from all pages
- **Documentation**: Includes type hints in docstring and documents possible exceptions

### File Path Setup (Lines 33-34)

```python
pdf_file = Path(pdf_path)
```

- Converts the string path to a `Path` object, which provides convenient methods for path manipulation
- Enables use of `.exists()`, `.suffix`, and `.with_suffix()` methods

### File Validation (Lines 35-41)

```python
# Validate file exists
if not pdf_file.exists():
    raise FileNotFoundError(f"Error: File '{pdf_path}' not found.")

# Validate it's a PDF file
if pdf_file.suffix.lower() != '.pdf':
    raise ValueError(f"Error: '{pdf_path}' is not a PDF file (expected .pdf extension).")
```

**Validation Steps:**
1. **Existence Check**: Verifies the file exists before attempting to read it
   - Uses `Path.exists()` method
   - Raises `FileNotFoundError` with a descriptive message if file doesn't exist

2. **File Type Check**: Ensures the file has a `.pdf` extension
   - Uses `Path.suffix` to get the file extension
   - Converts to lowercase for case-insensitive comparison
   - Raises `ValueError` if not a PDF file
   - This is a basic validation - doesn't check actual file content, just extension

### Text Extraction Setup (Lines 43-44)

```python
# Extract text from PDF
extracted_text = []
```

- Initializes a list to store text from each page
- Each page's text will be appended to this list and joined later

### PDF Reading and Processing (Lines 46-64)

```python
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
                extracted_text.append("")
```

**Key Components:**

1. **File Opening** (`with open(pdf_file, 'rb') as file:`):
   - Opens file in binary read mode (`'rb'`) - required for PDF files
   - Uses context manager (`with`) to ensure proper file closure even if errors occur

2. **PDF Reader Creation** (`PyPDF2.PdfReader(file)`):
   - Creates a `PdfReader` object from the file
   - This object provides access to all pages and PDF metadata

3. **Encryption Check** (`if pdf_reader.is_encrypted:`):
   - Checks if PDF requires a password
   - Encrypted PDFs cannot be read without the password
   - Raises `ValueError` with clear error message if encrypted
   - This check happens before processing to fail fast

4. **Page Counting** (`len(pdf_reader.pages)`):
   - Gets the total number of pages
   - Used for user feedback and progress indication

5. **Page Processing Loop** (`for page_num, page in enumerate(...)`):
   - Iterates through each page in the PDF
   - `enumerate(..., start=1)` provides 1-based page numbering for user-friendly output
   - Each page is processed individually with its own error handling

6. **Text Extraction per Page** (`page.extract_text()`):
   - Extracts all text from the current page
   - Returns a string containing the page's text content
   - Appends to `extracted_text` list

7. **Per-Page Error Handling**:
   - Wrapped in try-except to handle individual page failures
   - If a page fails, prints a warning but continues processing other pages
   - Appends empty string to maintain page order in output
   - This ensures the script doesn't crash on a single problematic page

### Exception Handling (Lines 66-69)

```python
except PyPDF2.errors.PdfReadError as e:
    raise PyPDF2.errors.PdfReadError(f"Error: Cannot read PDF file. {e}")
except Exception as e:
    raise Exception(f"Error reading PDF file: {e}")
```

- Catches specific `PdfReadError` from PyPDF2 (e.g., corrupted PDF)
- Catches any other unexpected exceptions during file reading
- Re-raises with enhanced error messages for clarity
- Allows calling code to handle these exceptions appropriately

### Return Statement (Line 71)

```python
return "\n".join(extracted_text)
```

- Joins all page texts with newline characters (`\n`)
- Creates a single string with pages separated by blank lines
- Returns the complete extracted text

---

## Function: `main()` (Lines 74-111)

### Function Docstring (Line 75)

```python
"""Main function to handle command-line arguments and execute extraction."""
```

- Describes the function's role as the entry point for command-line usage

### Command-Line Argument Validation (Lines 76-80)

```python
# Check for command-line argument
if len(sys.argv) != 2:
    print("Usage: python3 extract-as-text.py <pdf_file>")
    print("Example: python3 extract-as-text.py document.pdf")
    sys.exit(1)

pdf_path = sys.argv[1]
```

**Validation Logic:**
- `sys.argv` is a list containing:
  - `sys.argv[0]`: Script name
  - `sys.argv[1]`: First argument (PDF file path)
- Checks if exactly 2 arguments exist (script name + 1 argument)
- If not, prints usage instructions and exits with code 1
- Extracts the PDF path from `sys.argv[1]`

### Extraction Execution (Lines 84-98)

```python
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
```

**Execution Flow:**

1. **User Feedback**: Prints progress message before starting extraction

2. **Text Extraction**: Calls `extract_pdf_text()` function with the provided path

3. **Output File Generation**:
   - Creates a `Path` object from the input PDF path
   - Uses `.with_suffix('.txt')` to replace `.pdf` extension with `.txt`
   - Example: `document.pdf` → `document.txt`
   - Preserves the original filename

4. **File Writing**:
   - Opens output file in write mode (`'w'`)
   - Specifies UTF-8 encoding to handle international characters correctly
   - Writes all extracted text to the file
   - Context manager ensures file is properly closed

5. **Success Messages**:
   - Prints confirmation with output filename
   - Shows character count for user information

### Error Handling (Lines 100-111)

```python
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
```

**Exception Hierarchy:**
1. **`FileNotFoundError`**: File doesn't exist (from validation)
2. **`ValueError`**: Invalid file type or encrypted PDF
3. **`PdfReadError`**: PDF reading/corruption issues
4. **`Exception`**: Catches any other unexpected errors

**Error Handling Strategy:**
- Each exception type is caught separately for specific handling
- Error messages from lower-level functions are preserved and displayed
- All errors result in exit code 1 (failure)
- Final catch-all ensures the script never crashes with unhandled exceptions

---

## Script Entry Point (Lines 114-115)

```python
if __name__ == "__main__":
    main()
```

- **Standard Python idiom**: Only executes `main()` when script is run directly
- Allows the script to be imported as a module without executing
- Makes the code reusable in other scripts if needed

---

## Design Decisions and Features

### 1. **Error Handling Philosophy**
- **Fail Fast**: Validates input early (file existence, extension)
- **Graceful Degradation**: Continues processing if individual pages fail
- **Clear Messages**: All errors include descriptive, actionable messages
- **Proper Exit Codes**: Uses `sys.exit(1)` for failures, allowing script chaining

### 2. **User Experience**
- Progress messages inform users what's happening
- Character count provides feedback on extraction success
- Usage instructions appear when arguments are incorrect

### 3. **Code Quality**
- Separation of concerns: extraction logic separate from CLI handling
- Path handling uses modern `pathlib` instead of `os.path`
- Type hints in docstrings improve code documentation
- Comprehensive error handling for robustness

### 4. **File Handling**
- Binary mode for reading PDFs (required format)
- Text mode with UTF-8 encoding for output (handles international characters)
- Context managers ensure proper resource cleanup

### 5. **Output Strategy**
- Creates `.txt` file with same name as input
- Preserves original filename for easy identification
- Output in same directory as input file

---

## Potential Improvements

While the current implementation is solid, here are areas that could be enhanced:

1. **Command-line Options**: Add flags for output directory, output filename, verbose mode
2. **Progress Indicators**: Show progress percentage for large PDFs
3. **OCR Support**: Handle scanned PDFs using OCR libraries
4. **Batch Processing**: Support multiple PDF files at once
5. **Format Options**: Support different output formats (JSON, CSV, etc.)
6. **Metadata Extraction**: Extract PDF metadata (author, title, creation date)

---

## Summary

This script demonstrates solid Python practices:
- Clear separation of logic and interface
- Comprehensive error handling
- User-friendly output and error messages
- Modern Python path handling
- Proper resource management

The code is well-structured, maintainable, and ready for production use while remaining simple and easy to understand.

