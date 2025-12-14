#!/usr/bin/env python3
"""
Content Breakdown Script

Breaks down a single markdown or text file into multiple files based on keywords.
Each keyword creates a separate output file containing all content sections that match.
The output format automatically matches the input file format.
"""

import sys
import os
import argparse
from pathlib import Path
import re
from collections import defaultdict


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
        input_format (str): Format of the input ('text' or 'markdown')
        
    Returns:
        list: List of tuples (section_title, section_content, page_number)
    """
    sections = []
    
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
                page_header = f"Page {page_num} of "
                content_body = page_content
                
                sections.append((page_header, content_body, page_num))
    
    return sections


def find_matching_sections(content_by_pages, keywords, case_sensitive=False):
    """
    Find sections that match any of the keywords.
    
    Args:
        sections (list): List of (title, content, page_number) tuples
        keywords (list): List of keywords to search for
        case_sensitive (bool): Whether to perform case-sensitive matching
        
    Returns:
        dict: Dictionary mapping keywords to lists of matching sections
    """
    matches = defaultdict(list)
    
    for keyword in keywords:
        search_keyword = keyword if case_sensitive else keyword.lower()
        
        for title, content, page_num in content_by_pages:
            search_title = title if case_sensitive else title.lower()
            search_content = content if case_sensitive else content.lower()
            
            # Check if keyword appears in title or content
            if search_keyword in search_title or search_keyword in search_content:
                matches[keyword].append((title, content, page_num))
    
    return matches


def format_output_content(sections, keyword, output_format, original_filename):
    """
    Format the matching sections for output.
    
    Args:
        sections (list): List of (title, content, page_number) tuples
        keyword (str): The keyword that matched these sections
        output_format (str): Output format ('text' or 'markdown')
        original_filename (str): Original filename for reference
        
    Returns:
        str: Formatted content
    """
    if not sections:
        return ""
    
    if output_format == 'markdown':
        # Markdown format
        result = [f"# {keyword.title()} - Content Breakdown\n"]
        result.append(f"*Extracted from: {original_filename}*\n")
        result.append(f"*Keyword: {keyword}*\n")
        result.append(f"*Matching sections: {len(sections)}*\n")
        result.append("---\n")
        
        for i, (title, content, page_num) in enumerate(sections, 1):
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
        result.append(f"{separator}\n")
        
        for i, (title, content, page_num) in enumerate(sections, 1):
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
            keywords = [k.strip() for k in args.keywords.split(',') if k.strip()]
            if not keywords:
                print("Error: No valid keywords provided.")
                sys.exit(1)
        else:
            keywords = load_keywords_from_file(args.keywords_file)
        
        print(f"Loaded {len(keywords)} keyword(s): {', '.join(keywords)}")
        
        # Read input file
        print(f"Reading input file '{args.input_file}'...")
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.strip():
            print("Error: Input file is empty.")
            sys.exit(1)
        
        # Parse content into sections
        print(f"Parsing content into pages ...")
        content_by_pages = parse_content_pages(content)
        print(f"Found {len(content_by_pages)} content sections.")
        
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
            
            # Format content
            formatted_content = format_output_content(
                matching_sections, keyword, output_format, input_path.name
            )
            
            if not formatted_content.strip():
                continue
            
            # Generate output filename
            safe_keyword = sanitize_filename(keyword)
            output_filename = f"{input_path.stem}_{safe_keyword}{file_extension}"
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