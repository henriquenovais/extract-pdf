# Code Breakdown: extract-as-text.py

## Overview

This script extracts all text content from a PDF file and saves it to a text file. It uses the PyPDF2 library to read PDF files and process each page to extract text content. The script includes an optional signature filter feature that can automatically detect and remove repetitive text patterns (like headers, footers, or signatures) that appear across multiple consecutive pages.

## Script Structure

The script is organized into several main functions:
1. `extract_pdf_text()` - Core PDF text extraction logic
2. `find_signature_patterns()` - Detects repetitive text patterns across pages
3. `apply_signature_filter()` - Removes detected signature patterns
4. `format_output()` - Formats extracted text with page separators
5. `main()` - Command-line interface and orchestration

---

## Line-by-Line Breakdown

### Shebang and Module Docstring (Lines 1-7)

```python
#!/usr/bin/env python3
"""
PDF Text Extraction Script

Extracts all text from a PDF file and saves it to a text file.
"""
```

- **Line 1**: The shebang (`#!/usr/bin/env python3`) allows the script to be executed directly on Unix-like systems. It ensures Python 3 is used.
- **Lines 2-7**: Module-level docstring providing a brief description of the script's purpose.

### Imports (Lines 9-18)

```python
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
```

**Standard Library Imports:**
- `sys`: Provides access to command-line arguments and exit codes (`sys.exit()`)
- `os`: Included for potential file operations (currently unused but available)
- `argparse`: Modern command-line argument parsing (replaces manual `sys.argv` handling)
- `pathlib.Path`: Modern, object-oriented file path handling
- `collections.Counter`: Used for counting occurrences (imported but not currently used)
- `re`: Regular expressions for pattern matching and text replacement

**Third-Party Import with Error Handling:**
- The `PyPDF2` import is wrapped in a try-except block to handle missing dependencies
- If `PyPDF2` cannot be imported, the script prints a helpful error message and exits with code 1
- This provides better user experience than letting Python raise an unclear `ImportError`

---

## Function: `extract_pdf_text()` (Lines 21-82)

### Function Signature and Docstring (Lines 21-35)

```python
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
```

- **Purpose**: Core function that handles the PDF text extraction
- **Parameters**: Takes a single string argument `pdf_path` containing the file path
- **Returns**: A tuple containing a list of page texts and the total page count (changed from original single string return)
- **Documentation**: Includes type hints in docstring and documents possible exceptions

### File Path Setup and Validation (Lines 36-44)

```python
pdf_file = Path(pdf_path)

# Validate file exists
if not pdf_file.exists():
    raise FileNotFoundError(f"Error: File '{pdf_path}' not found.")

# Validate it's a PDF file
if pdf_file.suffix.lower() != '.pdf':
    raise ValueError(f"Error: '{pdf_path}' is not a PDF file (expected .pdf extension).")
```

**Validation Steps:**
1. **Path Object Creation**: Converts string path to `Path` object for convenient methods
2. **Existence Check**: Verifies the file exists before attempting to read it
3. **File Type Check**: Ensures the file has a `.pdf` extension (case-insensitive)

### Text Extraction Setup (Lines 46-48)

```python
# Extract text from PDF
extracted_text = []
num_pages = 0
```

- Initializes a list to store text from each page separately (changed from joining immediately)
- Initializes page counter for return value

### PDF Reading and Processing (Lines 50-80)

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
                extracted_text.append("[Text extraction failed for this page]")
```

**Key Components:**

1. **File Opening**: Opens in binary read mode (`'rb'`) with context manager
2. **PDF Reader Creation**: Creates `PdfReader` object for page access
3. **Encryption Check**: Validates PDF is not password-protected
4. **Page Processing**: Extracts text from each page individually
5. **Error Handling**: Graceful handling of individual page failures with placeholder text

### Exception Handling and Return (Lines 77-82)

```python
except PyPDF2.errors.PdfReadError as e:
    raise PyPDF2.errors.PdfReadError(f"Error: Cannot read PDF file. {e}")
except Exception as e:
    raise Exception(f"Error reading PDF file: {e}")

return extracted_text, num_pages
```

- Catches and re-raises PDF-specific and general exceptions with enhanced messages
- Returns tuple of page texts list and page count for further processing

---

## Function: `find_signature_patterns()` (Lines 85-142)

### Function Signature and Docstring (Lines 85-97)

```python
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
```

- **Purpose**: Identifies repetitive text patterns that appear across multiple consecutive pages
- **Parameters**: 
  - `page_texts`: List of extracted text from each page
  - `min_consecutive_pages`: Threshold for considering a pattern as signature (default 20)
  - `min_length`: Minimum character length for potential signatures (default 20)
- **Returns**: List of detected signature patterns

### Early Exit Check (Lines 98-100)

```python
if len(page_texts) < min_consecutive_pages:
    return []
```

- Returns empty list if document has fewer pages than the minimum threshold
- Prevents unnecessary processing on short documents

### Line Extraction (Lines 102-110)

```python
# Extract all potential signature lines from all pages
all_lines = set()
for page_text in page_texts:
    if page_text and page_text != "[Text extraction failed for this page]":
        lines = [line.strip() for line in page_text.split('\n') if line.strip()]
        for line in lines:
            if len(line) >= min_length:
                all_lines.add(line)
```

**Process:**
1. **Set Creation**: Uses set to automatically deduplicate lines
2. **Page Iteration**: Processes each page's text
3. **Skip Failed Pages**: Ignores pages where extraction failed
4. **Line Splitting**: Splits page text into individual lines
5. **Line Cleaning**: Strips whitespace and filters empty lines
6. **Length Filtering**: Only considers lines meeting minimum length requirement

### Pattern Detection Loop (Lines 112-140)

```python
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
```

**Algorithm:**
1. **Page Mapping**: For each unique line, finds all pages where it appears
2. **Consecutive Detection**: Analyzes page indices to find longest consecutive sequence
3. **Threshold Check**: Only patterns appearing on enough consecutive pages are considered signatures
4. **Pattern Collection**: Qualifying patterns are added to the results list

### Pattern Sorting and Return (Lines 141-142)

```python
# Sort by length (longest first) to remove longer patterns first
signature_patterns.sort(key=len, reverse=True)

return signature_patterns
```

- Sorts patterns by length (descending) to prioritize removal of longer, more specific patterns
- This prevents shorter patterns from interfering with longer pattern removal

---

## Function: `apply_signature_filter()` (Lines 144-200)

### Function Signature and Docstring (Lines 144-156)

```python
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
```

- **Purpose**: Applies signature detection and removal to clean up extracted text
- **Parameters**: Same as `find_signature_patterns()` for consistency
- **Returns**: List of page texts with signature patterns removed

### Early Exit and Pattern Detection (Lines 157-167)

```python
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
```

**Process:**
1. **Early Exit**: Returns original text if document too short
2. **Pattern Detection**: Calls `find_signature_patterns()` to identify patterns
3. **No Patterns**: Returns original text if no patterns found
4. **User Feedback**: Displays detected patterns with truncation for readability

### Pattern Removal Loop (Lines 169-200)

```python
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
```

**Removal Process:**
1. **Page Iteration**: Processes each page individually
2. **Skip Failed Pages**: Preserves pages where extraction failed
3. **Pattern Removal**: Uses regex to remove each signature pattern
4. **Counting**: Tracks removal statistics for user feedback
5. **Cleanup**: Removes extra whitespace and empty lines created by removals
6. **Statistics**: Reports total removals across all pages

---

## Function: `format_output()` (Lines 203-220)

### Function Signature and Implementation (Lines 203-220)

```python
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
```

**Formatting Process:**
1. **Separator Creation**: Creates visual separator using 60 equal signs
2. **Page Headers**: Adds "Page X of Y" headers for each page
3. **Page Assembly**: Combines separator, header, and content for each page
4. **Final Join**: Joins all formatted pages into single string

---

## Function: `main()` (Lines 223-268)

### Argument Parser Setup (Lines 224-242)

```python
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
    help='Enable signature filter: removes text patterns that appear on 20+ consecutive pages (like headers/footers/signatures)'
)

args = parser.parse_args()
pdf_path = args.pdf_file
```

**Argument Configuration:**
1. **Parser Creation**: Uses `argparse` for professional command-line interface
2. **Description**: Provides clear description of script purpose
3. **Positional Argument**: `pdf_file` is required argument for input file
4. **Optional Flag**: `--signature-filter` enables signature removal feature
5. **Help Text**: Detailed help messages for user guidance

### Extraction Execution (Lines 245-268)

```python
try:
    # Extract text from PDF
    print(f"Extracting text from '{pdf_path}'...")
    page_texts, num_pages = extract_pdf_text(pdf_path)
    
    # Apply signature filter if enabled
    if args.signature_filter:
        print("Applying signature filter...")
        page_texts = apply_signature_filter(page_texts, min_consecutive_pages=20, min_length=20)
    
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
```

**Execution Flow:**
1. **Text Extraction**: Calls core extraction function
2. **Conditional Filtering**: Applies signature filter if requested
3. **Output Formatting**: Formats text with page separators
4. **File Generation**: Creates output filename by changing extension
5. **File Writing**: Saves formatted text with UTF-8 encoding
6. **User Feedback**: Provides success confirmation and statistics
7. **Error Handling**: Comprehensive exception handling with appropriate exit codes

---

## Script Entry Point (Lines 271-272)

```python
if __name__ == "__main__":
    main()
```

- Standard Python idiom for script execution
- Allows module import without automatic execution

---

## Key Design Improvements

### 1. **Enhanced Command-Line Interface**
- **Modern Argument Parsing**: Uses `argparse` instead of manual `sys.argv` handling
- **Optional Features**: Signature filter is optional via command-line flag
- **Professional Help**: Automatic help generation with usage examples

### 2. **Signature Detection Algorithm**
- **Pattern Recognition**: Automatically detects repetitive text across pages
- **Configurable Thresholds**: Adjustable parameters for different document types
- **Smart Removal**: Uses regex for precise pattern removal
- **User Feedback**: Shows detected patterns and removal statistics

### 3. **Improved Output Format**
- **Page Separation**: Clear visual separation between pages
- **Page Numbering**: Each page labeled with position information
- **Clean Formatting**: Removes extra whitespace created by signature removal

### 4. **Robust Error Handling**
- **Graceful Degradation**: Continues processing despite individual page failures
- **Comprehensive Coverage**: Handles all expected exception types
- **Clear Messages**: Descriptive error messages for troubleshooting

### 5. **Modular Design**
- **Separation of Concerns**: Each function has a single, clear responsibility
- **Reusable Components**: Functions can be used independently
- **Testable Code**: Modular structure facilitates unit testing

---

## Algorithm Details: Signature Detection

The signature detection algorithm works in several phases:

### Phase 1: Line Collection
- Extracts all unique lines from all pages
- Filters by minimum length to avoid noise
- Uses set for automatic deduplication

### Phase 2: Page Mapping
- For each unique line, identifies all pages where it appears
- Handles failed extraction pages gracefully
- Creates mapping of line → page indices

### Phase 3: Consecutive Analysis
- Analyzes page indices to find longest consecutive sequences
- Uses sliding window approach to detect gaps
- Tracks maximum consecutive count per pattern

### Phase 4: Pattern Qualification
- Only patterns appearing on sufficient consecutive pages qualify
- Configurable threshold allows adaptation to different document types
- Sorts by length to prioritize specific patterns over general ones

### Phase 5: Pattern Removal
- Uses regex for precise, case-sensitive removal
- Processes each page individually to maintain structure
- Cleans up whitespace artifacts from removal
- Tracks statistics for user feedback

---

## Usage Examples

### Basic Extraction
```bash
python3 extract-as-text.py document.pdf
```

### With Signature Filter
```bash
python3 extract-as-text.py document.pdf --signature-filter
```

### Short Form Flag
```bash
python3 extract-as-text.py document.pdf -sf
```

---

## Summary

This enhanced script demonstrates advanced Python practices:

- **Professional CLI**: Modern argument parsing with help system
- **Advanced Algorithms**: Sophisticated pattern detection and removal
- **Robust Processing**: Comprehensive error handling and graceful degradation
- **User Experience**: Clear feedback, progress indication, and statistics
- **Modular Architecture**: Clean separation of concerns and reusable components
- **Production Ready**: Handles edge cases, provides diagnostics, and maintains data integrity

The signature filter feature makes this script particularly valuable for processing documents with repetitive elements like legal documents, academic papers, or corporate reports where headers, footers, and signature blocks can clutter the extracted text.