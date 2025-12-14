#!/usr/bin/env python3
"""
Content Breakdown Script

Breaks down a single markdown or text file into multiple files based on keywords.
Each keyword creates a separate output file containing all content sections that match.
The output format automatically matches the input file format.
"""

import sys
import argparse
from pathlib import Path
import re
from collections import defaultdict
from unidecode import unidecode


def load_keywords_from_file(keywords_file):
    """
    Load keywords from a file (one keyword per line).
    
    Args:
        keywords_file (str): Path to the keywords file
        
    Returns:
        list: List of keywords (stripped and non-empty)
        
    Raises:
        FileNotFoundError: If the keywords file doesn't exist
    """
    keywords_path = Path(keywords_file)
    
    if not keywords_path.exists():
        raise FileNotFoundError(f"Error: Keywords file '{keywords_file}' not found.")
    
    try:
        with open(keywords_path, 'r', encoding='utf-8') as f:
            keywords = [line.strip() for line in f if line.strip()]
        
        if not keywords:
            raise ValueError(f"Error: Keywords file '{keywords_file}' is empty or contains no valid keywords.")
        
        return keywords
    except Exception as e:
        raise Exception(f"Error reading keywords file: {e}")


def parse_content_pages(content):
    """
    Parse content into sections based on format.
    
    Args:
        content (str): The input content
        
    Returns:
        tuple: (sections_list, total_pages)
            sections_list: List of tuples (section_title, section_content, page_number)
            number_of_total_pages: Total number of pages in the document
    """
    sections = []
    number_of_total_pages = 0
    
    # Extract total pages from any "Page X of Y" pattern in the content
    total_pages_pattern = r'.*Page \d+ of (\d+)\n'
    total_pages_matches = re.findall(total_pages_pattern, content, re.IGNORECASE)
    if total_pages_matches:
        number_of_total_pages = max(int(match) for match in total_pages_matches)

    print(f"Total pages is {number_of_total_pages}")
    
    # Parse text format with page separators
    page_pattern = r'.*Page (\d+) of \d+\n'
    pages = re.split(page_pattern, content)
    
    # First element is content before first page (usually empty)
    if pages[0].strip():
        sections.append(("Introduction", pages[0].strip(), 0))
    
    # Process page pairs (page_number, page_content)
    for i in range(1, len(pages), 2):
        if i + 1 < len(pages):
            page_num = int(pages[i])
            page_content = pages[i + 1].strip()
            if page_content:
                if number_of_total_pages > 0:
                    page_header = f"Page {page_num} of {number_of_total_pages}"
                else:
                    print("Error: could not detect total number of pages.")
                    sys.exit(1)
                    
                content_body = page_content
                
                sections.append((page_header, content_body, page_num))
    
    return sections, number_of_total_pages

def normalize_text(text):
    """Normalize text by replacing common character variations using unidecode."""

    # First apply unidecode to handle Unicode normalization
    # This converts Unicode characters to their ASCII equivalents
    text = unidecode(text)
    
    # Additional custom normalizations for common variations
    # Normalize ampersand variations
    text = re.sub(r'\s+&\s+', ' and ', text)  # " & " → " and "
    text = re.sub(r'&', 'and', text)  # remaining "&" → "and"
    
    # Normalize different types of quotes (in case unidecode didn't catch them)
    text = re.sub(r'[""''`]', '"', text)  # smart quotes → regular quotes
    
    # Normalize different types of dashes and hyphens
    text = re.sub(r'[—–−]', '-', text)  # em dash, en dash, minus → hyphen
    
    # Normalize ellipsis
    text = re.sub(r'…', '...', text)  # ellipsis character → three dots
    
    # Normalize bullet points and list markers
    text = re.sub(r'[•·‣⁃]', '*', text)  # various bullets → asterisk
    
    # Normalize copyright and trademark symbols
    text = re.sub(r'©', '(c)', text)
    text = re.sub(r'®', '(R)', text)
    text = re.sub(r'™', '(TM)', text)
    
    return text.strip()

def find_matching_sections(content_by_pages, keywords, case_sensitive=False):
    """
    Find sections that match exactly one keyword with no other significant content.
    
    Args:
        content_by_pages (list): List of (title, content, page_number) tuples
        keywords (list): List of keywords to search for
        case_sensitive (bool): Whether to perform case-sensitive matching
        
    Returns:
        dict: Dictionary mapping keywords to lists of matching sections
    """
    matches = defaultdict(list)
    
    # Prepare keywords for matching
    search_keywords = []
    for keyword in keywords:
        search_keywords.append(keyword if case_sensitive else keyword.lower())
    
    for page_header, content, page_num in content_by_pages:
        search_content = content if case_sensitive else content.lower()
        
        # Clean the content for analysis - remove extra whitespace and common formatting
        cleaned_content = re.sub(r'\s+', ' ', search_content.strip())
        
        # Find which keywords appear in this page
        found_keywords = []
        for i, search_keyword in enumerate(search_keywords):
            if search_keyword in cleaned_content:
                found_keywords.append((keywords[i], search_keyword))
        
        # Only proceed if exactly one keyword is found
        if len(found_keywords) == 1:
            original_keyword, search_keyword = found_keywords[0]
            
            # Check if the page contains essentially only this keyword
            # Remove the keyword from content and check what remains
            remaining_content = cleaned_content
            
            # Remove all occurrences of the keyword
            if case_sensitive:
                remaining_content = remaining_content.replace(original_keyword, '')
            else:
                # Case-insensitive replacement
                remaining_content = re.sub(re.escape(search_keyword), '', remaining_content, flags=re.IGNORECASE)
            
            # Clean up remaining content - remove extra whitespace
            remaining_content = re.sub(r'\s+', ' ', remaining_content.strip())
            
            # Check if remaining content is minimal (only whitespace, punctuation, or very short)
            # Allow for minor formatting characters, page numbers, etc.
            minimal_content_pattern = r'^[\s\-_=\.\,\;\:\!\?\(\)\[\]\{\}]*$'
            
            # Also allow very short remaining content (less than 10 characters of actual text)
            actual_text = re.sub(r'[^\w]', '', remaining_content)
            
            if (re.match(minimal_content_pattern, remaining_content) or 
                len(actual_text) <= 3):  # Allow up to 3 characters of remaining text
                matches[original_keyword].append((page_header, content, page_num))
    
    return matches


def format_output_content(sections, keyword, output_format, original_filename, content_by_pages, all_matches):
    """
    Format the matching sections for output with section-based content extraction.
    
    Args:
        sections (list): List of (title, content, page_number) tuples for keyword matches
        keyword (str): The keyword that matched these sections
        output_format (str): Output format ('text' or 'markdown')
        original_filename (str): Original filename for reference
        content_by_pages (list): Complete list of all (title, content, page_number) tuples
        all_matches (dict): Dictionary of all keyword matches to determine section boundaries
        
    Returns:
        str: Formatted content including all pages in section ranges
    """
    if not sections:
        return ""
    
    # Create a mapping of page numbers to content for easy lookup
    page_content_map = {page_num: (title, content) for title, content, page_num in content_by_pages}
    
    # Get all page numbers sorted
    all_page_numbers = sorted([page_num for _, _, page_num in content_by_pages if page_num > 0])
    
    if not all_page_numbers:
        return ""
    
    max_page = max(all_page_numbers)
    
    # Collect all section start pages from all keywords to determine boundaries
    all_section_starts = []
    for kw, kw_sections in all_matches.items():
        for _, _, page_num in kw_sections:
            if page_num > 0:
                all_section_starts.append(page_num)
    
    all_section_starts = sorted(set(all_section_starts))
    
    # Determine section ranges for this keyword
    section_ranges = []
    
    # Get the starting pages for this keyword's sections
    keyword_start_pages = sorted([page_num for _, _, page_num in sections if page_num > 0])
    
    for start_page in keyword_start_pages:
        # Find the next section start page that comes after this one
        section_end = max_page  # Default to end of document
        
        for next_start in all_section_starts:
            if next_start > start_page:
                section_end = next_start - 1
                break
        
        section_ranges.append((start_page, section_end))
    
    # Merge overlapping or adjacent ranges
    if section_ranges:
        section_ranges.sort()
        merged_ranges = [section_ranges[0]]
        
        for start, end in section_ranges[1:]:
            last_start, last_end = merged_ranges[-1]
            if start <= last_end + 1:  # Overlapping or adjacent
                merged_ranges[-1] = (last_start, max(last_end, end))
            else:
                merged_ranges.append((start, end))
        
        section_ranges = merged_ranges
    
    # Collect all pages in the section ranges
    all_section_pages = []
    total_pages_included = 0
    
    for start_page, end_page in section_ranges:
        for page_num in range(start_page, end_page + 1):
            if page_num in page_content_map:
                title, content = page_content_map[page_num]
                all_section_pages.append((title, content, page_num))
                total_pages_included += 1
    
    # Sort by page number to maintain order
    all_section_pages.sort(key=lambda x: x[2])
    
    if output_format == 'markdown':
        # Markdown format
        result = [f"# {keyword.title()} - Content Breakdown\n"]
        result.append(f"*Extracted from: {original_filename}*\n")
        result.append(f"*Keyword: {keyword}*\n")
        result.append(f"*Matching sections: {len(sections)}*\n")
        result.append(f"*Total pages included: {total_pages_included}*\n")
        if section_ranges:
            range_str = ", ".join([f"{start}-{end}" for start, end in section_ranges])
            result.append(f"*Page ranges: {range_str}*\n")
        result.append("---\n")
        
        for i, (title, content, page_num) in enumerate(all_section_pages, 1):
            if i > 1:
                result.append("\n---\n")
            
            result.append(f"## {title}")
            if page_num > 0:
                result.append(f"*Page {page_num}*\n")
            else:
                result.append("")
            
            result.append(content)
            result.append("\n")
    
    else:
        # Text format
        separator = "=" * 60
        result = [f"{separator}"]
        result.append(f"CONTENT BREAKDOWN FOR KEYWORD: {keyword.upper()}")
        result.append(f"Source: {original_filename}")
        result.append(f"Matching sections: {len(sections)}")
        result.append(f"Total pages included: {total_pages_included}")
        if section_ranges:
            range_str = ", ".join([f"{start}-{end}" for start, end in section_ranges])
            result.append(f"Page ranges: {range_str}")
        result.append(f"{separator}\n")
        
        for i, (title, content, page_num) in enumerate(all_section_pages, 1):
            if i > 1:
                result.append(f"\n{'-' * 40}\n")
            
            page_info = f" (Page {page_num})" if page_num > 0 else ""
            result.append(f"{title}{page_info}")
            result.append("-" * len(f"{title}{page_info}"))
            result.append(content)
            result.append("")
    
    return "\n".join(result)

def sanitize_filename(keyword):
    """
    Sanitize a keyword to be used as a filename.
    
    Args:
        keyword (str): The keyword to sanitize
        
    Returns:
        str: Sanitized filename
    """
    # Replace spaces and special characters with underscores
    sanitized = re.sub(r'[^\w\-_.]', '_', keyword)
    # Remove multiple consecutive underscores
    sanitized = re.sub(r'_+', '_', sanitized)
    # Remove leading/trailing underscores
    sanitized = sanitized.strip('_')
    # Ensure it's not empty
    if not sanitized:
        sanitized = "keyword"
    
    return sanitized.lower()


def detect_file_format(file_path):
    """
    Detect file format based on file extension.
    
    Args:
        file_path (Path): Path to the input file
        
    Returns:
        tuple: (input_format, output_format, file_extension)
    """
    extension = file_path.suffix.lower()
    
    if extension in ['.md', '.markdown']:
        return 'markdown', 'markdown', '.md'
    else:
        # Default to text format for all other extensions (.txt, .text, or no extension)
        return 'text', 'text', '.txt'


def main():
    """Main function to handle command-line arguments and execute breakdown."""
    parser = argparse.ArgumentParser(
        description="Break down a single markdown or text file into multiple files based on keywords. Output format automatically matches input format.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
        Examples:
        python3 file-slicer.py slides.md --keywords "AWS,EC2,IAM"
        python3 file-slicer.py slides.txt --keywords-file keywords.txt
        python3 file-slicer.py slides.md -k "S3,Lambda" --case-sensitive
        python3 file-slicer.py slides.txt -kf keywords.txt --output-dir output/
        python3 file-slicer.py slides.txt -kf keywords.txt -o output/
        
        Note: Output format is automatically determined by input file extension:
        - .md/.markdown files → .md output files
        - .txt/.text files or other extensions → .txt output files
        """
    )
    
    parser.add_argument(
        'input_file',
        help='Path to the input file (markdown or text)'
    )
    
    # Keywords input (mutually exclusive)
    keywords_group = parser.add_mutually_exclusive_group(required=True)
    keywords_group.add_argument(
        '--keywords',
        '-k',
        help='Comma-separated list of keywords to search for'
    )
    keywords_group.add_argument(
        '--keywords-file',
        '-kf',
        help='Path to file containing keywords (one per line)'
    )
    
    parser.add_argument(
        '--case-sensitive',
        '-cs',
        action='store_true',
        help='Perform case-sensitive keyword matching (default: case-insensitive)'
    )
    
    parser.add_argument(
        '--output-dir',
        '-o',
        default='.',
        help='Output directory for generated files (default: current directory)'
    )
    
    parser.add_argument(
        '--min-matches',
        '-mm',
        type=int,
        default=1,
        help='Minimum number of matching sections required to create output file (default: 1)'
    )
    
    args = parser.parse_args()
    
    input_path = Path(args.input_file)
    output_dir = Path(args.output_dir)
    
    # Validate input file
    if not input_path.exists():
        print(f"Error: Input file '{args.input_file}' not found.")
        sys.exit(1)
    
    # Detect file format based on extension
    input_format, output_format, file_extension = detect_file_format(input_path)
    
    print(f"Detected file format: {input_format} → output format: {output_format}")
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Validate minimum matches
    if args.min_matches < 1:
        print("Error: Minimum matches must be at least 1.")
        sys.exit(1)
    
    try:
        # Load keywords
        if args.keywords:
            keywords = [normalize_text(k.strip()) for k in args.keywords.split(',') if k.strip()]
            if not keywords:
                print("Error: No valid keywords provided.")
                sys.exit(1)
        else:
            raw_keywords = load_keywords_from_file(args.keywords_file)
            keywords = [normalize_text(keyword) for keyword in raw_keywords]
        
        print(f"Loaded {len(keywords)} keyword(s): {', '.join(keywords)}")
        
        # Read input file
        print(f"Reading input file '{args.input_file}'...")
        with open(input_path, 'r', encoding='utf-8') as f:
            raw_content = f.read()
        
        if not raw_content.strip():
            print("Error: Input file is empty.")
            sys.exit(1)
        
        # Normalize content before processing
        print("Normalizing raw content...")
        content = normalize_text(raw_content)
        
        # Parse content into sections
        print(f"Parsing content into pages ...")
        parsed_content_by_pages = parse_content_pages(content)
        content_by_pages = parsed_content_by_pages[0]
        number_of_total_pages = parsed_content_by_pages[1] # total number of pages, not used yet
        print(f"Found {number_of_total_pages} pages.")
        
        if not content_by_pages:
            print("Warning: No content sections found in input file.")
            sys.exit(0)
        
        # Find matching sections for each keyword
        print(f"Searching for keyword matches (case-{'sensitive' if args.case_sensitive else 'insensitive'})...")
        matches = find_matching_sections(content_by_pages, keywords, args.case_sensitive)
        
        # Generate output files
        files_created = 0
        total_matches = 0
        
        for keyword in keywords:
            matching_sections = matches[keyword]
            
            if len(matching_sections) < args.min_matches:
                print(f"Skipping '{keyword}': only {len(matching_sections)} match(es) found (minimum: {args.min_matches})")
                continue
            
            # Format content - now passing all_matches for section boundary calculation
            formatted_content = format_output_content(
                matching_sections, keyword, output_format, input_path.name, content_by_pages, matches
            )
            
            if not formatted_content.strip():
                continue
            
            # Generate output filename
            safe_keyword = sanitize_filename(keyword)
            output_filename = f"{files_created + 1}_{input_path.stem}_{safe_keyword}{file_extension}"
            output_path = output_dir / output_filename
            
            # Write output file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(formatted_content)
            
            print(f"Created '{output_path}' with {len(matching_sections)} matching section(s)")
            files_created += 1
            total_matches += len(matching_sections)
        
        # Summary
        if files_created > 0:
            print(f"\nSuccessfully created {files_created} file(s) with {total_matches} total matching sections.")
            print(f"Output directory: {output_dir.absolute()}")
            print(f"Output format: {output_format} ({file_extension} files)")
        else:
            print("\nNo output files created. No keywords had sufficient matches.")
    
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()