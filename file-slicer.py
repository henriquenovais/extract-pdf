#!/usr/bin/env python3
"""
Content Breakdown Script

Breaks down a single markdown or text file into multiple files based on sentences.
Each sentence creates a separate output file containing all content sections that match.
The output format automatically matches the input file format.
"""

import sys
import argparse
from pathlib import Path
import re
from collections import defaultdict
from unidecode import unidecode


def load_sentences_from_file(sentences_file):
    """
    Load sentences from a file (one sentence per line).
    
    Args:
        sentences_file (str): Path to the sentences file
        
    Returns:
        list: List of sentences (stripped and non-empty)
        
    Raises:
        FileNotFoundError: If the sentences file doesn't exist
    """
    sentences_path = Path(sentences_file)
    
    if not sentences_path.exists():
        raise FileNotFoundError(f"Error: Sentences file '{sentences_file}' not found.")
    
    try:
        with open(sentences_path, 'r', encoding='utf-8') as f:
            sentences = [line.strip() for line in f if line.strip()]
        
        if not sentences:
            raise ValueError(f"Error: Sentences file '{sentences_file}' is empty or contains no valid sentences.")
        
        return sentences
    except Exception as e:
        raise Exception(f"Error reading sentences file: {e}")


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

    print(f"[INFO] Total pages detected: {number_of_total_pages}")
    
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
                    print("[ERROR] Could not detect total number of pages")
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

def find_matching_sections(content_by_pages, sentences, case_sensitive=False):
    """
    Find sections that match exactly one sentence with no other significant content.
    Prioritizes longer, more specific sentences when multiple matches are found.
    
    Args:
        content_by_pages (list): List of (title, content, page_number) tuples
        sentences (list): List of sentences to search for
        case_sensitive (bool): Whether to perform case-sensitive matching
        
    Returns:
        dict: Dictionary mapping sentences to lists of matching sections
    """
    matches = defaultdict(list)
    
    # Prepare sentences for matching - sort by length (longest first) to prioritize specific matches
    sentence_pairs = []
    for sentence in sentences:
        search_sentence = sentence if case_sensitive else sentence.lower()
        sentence_pairs.append((sentence, search_sentence))
    
    # Sort by length of search sentence (descending) to prioritize longer, more specific matches
    sentence_pairs.sort(key=lambda x: len(x[1]), reverse=True)

    print(f"[INFO] Analyzing {len(content_by_pages)} pages for sentence matches")
    print(f"[INFO] Sentences: {', '.join([s[:50] + '...' if len(s) > 50 else s for s in sentences])}")
    
    pages_with_matches = 0
    pages_with_multiple_sentences = 0
    pages_rejected_content = 0
    
    for page_idx, (page_header, content, page_num) in enumerate(content_by_pages, 1):
        search_content = content if case_sensitive else content.lower()
        cleaned_content = re.sub(r'\s+', ' ', search_content.strip())
        
        # Find which sentences appear in this page, prioritizing longer matches
        found_sentences = []
        for original_sentence, search_sentence in sentence_pairs:
            if search_sentence in cleaned_content:
                found_sentences.append((original_sentence, search_sentence))
        
        # If multiple sentences found, prioritize the longest (most specific) one
        if len(found_sentences) >= 1:
            # Take the first (longest) match due to our sorting
            original_sentence, search_sentence = found_sentences[0]
            
            # Check if the page contains essentially only this sentence
            remaining_content = cleaned_content
            
            # Remove all occurrences of the sentence
            if case_sensitive:
                remaining_content = remaining_content.replace(original_sentence, '')
            else:
                remaining_content = re.sub(re.escape(search_sentence), '', remaining_content, flags=re.IGNORECASE)
            
            # Clean up remaining content - remove extra whitespace
            remaining_content = re.sub(r'\s+', ' ', remaining_content.strip())
            
            # Check if remaining content is minimal
            minimal_content_pattern = r'^[\s\-_=\.\,\;\:\!\?\(\)\[\]\{\}]*$'
            actual_text = re.sub(r'[^\w]', '', remaining_content)
            
            # For sentences, we need to be more lenient with remaining content
            # Allow up to 10 characters of actual text (excluding punctuation/whitespace)
            if (re.match(minimal_content_pattern, remaining_content) or 
                len(actual_text) <= 10):
                matches[original_sentence].append((page_header, content, page_num))
                pages_with_matches += 1
                sentence_preview = original_sentence[:30] + '...' if len(original_sentence) > 30 else original_sentence
                
                # Show if multiple sentences were found but we picked the longest
                if len(found_sentences) > 1:
                    other_sentences = [s[0][:20] + '...' if len(s[0]) > 20 else s[0] for s in found_sentences[1:]]
                    print(f"       Page {page_num}: MATCH for '{sentence_preview}' (also found: {', '.join(other_sentences)})")
                else:
                    print(f"       Page {page_num}: MATCH for '{sentence_preview}'")
            else:
                pages_rejected_content += 1
                sentence_preview = original_sentence[:30] + '...' if len(original_sentence) > 30 else original_sentence
                
                if len(found_sentences) > 1:
                    other_sentences = [s[0][:20] + '...' if len(s[0]) > 20 else s[0] for s in found_sentences[1:]]
                    print(f"       Page {page_num}: REJECTED '{sentence_preview}' (extra content: '{actual_text[:20]}...', also found: {', '.join(other_sentences)})")
                else:
                    print(f"       Page {page_num}: REJECTED '{sentence_preview}' (extra content: '{actual_text[:20]}...')")
    
    # Summary
    print(f"\n[SUMMARY] Matching Results:")
    print(f"          Pages analyzed: {len(content_by_pages)}")
    print(f"          Pages with matches: {pages_with_matches}")
    print(f"          Pages with multiple sentences: {pages_with_multiple_sentences}")
    print(f"          Pages rejected (extra content): {pages_rejected_content}")
    
    for sentence in sentences:
        match_count = len(matches[sentence])
        sentence_preview = sentence[:40] + '...' if len(sentence) > 40 else sentence
        if match_count > 0:
            page_numbers = [str(page_num) for _, _, page_num in matches[sentence]]
            print(f"          '{sentence_preview}': {match_count} match(es) on pages {', '.join(page_numbers)}")
        else:
            print(f"          '{sentence_preview}': No matches found")
    
    return matches


def format_output_content(sections, sentence, output_format, original_filename, content_by_pages, all_matches):
    """
    Format the matching sections for output with section-based content extraction.
    
    Args:
        sections (list): List of (title, content, page_number) tuples for sentence matches
        sentence (str): The sentence that matched these sections
        output_format (str): Output format ('text' or 'markdown')
        original_filename (str): Original filename for reference
        content_by_pages (list): Complete list of all (title, content, page_number) tuples
        all_matches (dict): Dictionary of all sentence matches to determine section boundaries
        
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
    
    # Collect all section start pages from all sentences to determine boundaries
    all_section_starts = []
    for sent, sent_sections in all_matches.items():
        for _, _, page_num in sent_sections:
            if page_num > 0:
                all_section_starts.append(page_num)
    
    all_section_starts = sorted(set(all_section_starts))
    
    # Determine section ranges for this sentence
    section_ranges = []
    
    # Get the starting pages for this sentence's sections
    sentence_start_pages = sorted([page_num for _, _, page_num in sections if page_num > 0])
    
    for start_page in sentence_start_pages:
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
    
    # Create a shorter title for display
    sentence_title = sentence[:50] + '...' if len(sentence) > 50 else sentence
    
    if output_format == 'markdown':
        # Markdown format
        result = []
        result.append(f"# {sentence_title.title()} - Content Breakdown\n")
        result.append(f"*Extracted from: {original_filename}*\n")
        result.append(f"*Sentence: {sentence}*\n")
        result.append(f"*Matching sections: {len(sections)}*\n")
        result.append(f"*Total pages included: {total_pages_included}*\n")
        if section_ranges:
            range_str = ", ".join([f"{start}-{end}" for start, end in section_ranges])
            result.append(f"*Page ranges: {range_str}*\n")
        result.append("---\n")
        
        for i, (title, content, page_num) in enumerate(all_section_pages):
            if i > 0:  # Add separator between pages (but not before first page)
                result.append("---\n")
            
            result.append(f"## {title}")
            if page_num > 0:
                result.append(f"*Page {page_num}*\n")
            else:
                result.append("")
            
            # Clean up content - remove extra newlines and whitespace
            cleaned_content = content.strip()
            if cleaned_content:
                result.append(cleaned_content)
            result.append("")  # Single newline after content
    
    else:
        # Text format
        separator = "=" * 60
        result = [f"{separator}"]
        result.append(f"CONTENT BREAKDOWN FOR SENTENCE: {sentence_title.upper()}")
        result.append(f"Source: {original_filename}")
        result.append(f"Full sentence: {sentence}")
        result.append(f"Matching sections: {len(sections)}")
        result.append(f"Total pages included: {total_pages_included}")
        if section_ranges:
            range_str = ", ".join([f"{start}-{end}" for start, end in section_ranges])
            result.append(f"Page ranges: {range_str}")
        result.append(f"{separator}\n")
        
        for i, (title, content, page_num) in enumerate(all_section_pages):
            if i > 0:  # Add separator between pages (but not before first page)
                result.append(f"\n{'-' * 40}\n")
            
            page_info = f" (Page {page_num})" if page_num > 0 else ""
            result.append(f"{title}{page_info}")
            result.append("-" * len(f"{title}{page_info}"))
            
            # Clean up content - remove extra newlines and whitespace
            cleaned_content = content.strip()
            if cleaned_content:
                result.append(cleaned_content)
            result.append("")  # Single newline after content
    
    return "\n".join(result)

def sanitize_filename(sentence):
    """
    Sanitize a sentence to be used as a filename.
    
    Args:
        sentence (str): The sentence to sanitize
        
    Returns:
        str: Sanitized filename
    """
    # Take first 30 characters to avoid overly long filenames
    truncated = sentence[:30]
    
    # Replace spaces and special characters with underscores
    sanitized = re.sub(r'[^\w\-_.]', '_', truncated)
    # Remove multiple consecutive underscores
    sanitized = re.sub(r'_+', '_', sanitized)
    # Remove leading/trailing underscores
    sanitized = sanitized.strip('_')
    # Ensure it's not empty
    if not sanitized:
        sanitized = "sentence"
    
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
        description="Break down a single markdown or text file into multiple files based on sentences. Output format automatically matches input format.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
        Examples:
        python3 file-slicer.py slides.md --sentences "Welcome to AWS,Getting Started with EC2,Introduction to IAM"
        python3 file-slicer.py slides.txt --sentences-file sentences.txt
        python3 file-slicer.py slides.md -s "Amazon S3 Overview,AWS Lambda Functions" --case-sensitive
        python3 file-slicer.py slides.txt -sf sentences.txt --output-dir output/
        python3 file-slicer.py slides.txt -sf sentences.txt -o output/
        
        Note: Output format is automatically determined by input file extension:
        - .md/.markdown files → .md output files
        - .txt/.text files or other extensions → .txt output files
        """
    )
    
    parser.add_argument(
        'input_file',
        help='Path to the input file (markdown or text)'
    )
    
    # Sentences input (mutually exclusive)
    sentences_group = parser.add_mutually_exclusive_group(required=True)
    sentences_group.add_argument(
        '--sentences',
        '-s',
        help='Comma-separated list of sentences to search for'
    )
    sentences_group.add_argument(
        '--sentences-file',
        '-sf',
        help='Path to file containing sentences (one per line)'
    )
    
    parser.add_argument(
        '--case-sensitive',
        '-cs',
        action='store_true',
        help='Perform case-sensitive sentence matching (default: case-insensitive)'
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
        print(f"[ERROR] Input file '{args.input_file}' not found")
        sys.exit(1)
    
    # Detect file format based on extension
    input_format, output_format, file_extension = detect_file_format(input_path)
    
    print(f"[INFO] Detected file format: {input_format} → output format: {output_format}")
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Validate minimum matches
    if args.min_matches < 1:
        print("[ERROR] Minimum matches must be at least 1")
        sys.exit(1)
    
    try:
        # Load sentences
        if args.sentences:
            sentences = [normalize_text(s.strip()) for s in args.sentences.split(',') if s.strip()]
            if not sentences:
                print("[ERROR] No valid sentences provided")
                sys.exit(1)
        else:
            raw_sentences = load_sentences_from_file(args.sentences_file)
            sentences = [normalize_text(sentence) for sentence in raw_sentences]
        
        print(f"[INFO] Loaded {len(sentences)} sentence(s)")
        for i, sentence in enumerate(sentences, 1):
            preview = sentence[:60] + '...' if len(sentence) > 60 else sentence
            print(f"       {i}. {preview}")
        
        # Read input file
        print(f"[INFO] Reading input file '{args.input_file}'")
        with open(input_path, 'r', encoding='utf-8') as f:
            raw_content = f.read()
        
        if not raw_content.strip():
            print("[ERROR] Input file is empty")
            sys.exit(1)
        
        # Normalize content before processing
        print("[INFO] Normalizing raw content")
        content = normalize_text(raw_content)
        
        # Parse content into sections
        print(f"[INFO] Parsing content into pages")
        parsed_content_by_pages = parse_content_pages(content)
        content_by_pages = parsed_content_by_pages[0]
        number_of_total_pages = parsed_content_by_pages[1] # total number of pages, not used yet
        print(f"[INFO] Found {number_of_total_pages} pages")
        
        if not content_by_pages:
            print("[WARNING] No content sections found in input file")
            sys.exit(0)
        
        # Find matching sections for each sentence
        print(f"[INFO] Searching for sentence matches (case-{'sensitive' if args.case_sensitive else 'insensitive'})")
        matches = find_matching_sections(content_by_pages, sentences, args.case_sensitive)
        
        # Generate output files
        files_created = 0
        total_matches = 0
        
        print(f"\n[INFO] Generating output files")
        for sentence in sentences:
            matching_sections = matches[sentence]
            
            if len(matching_sections) < args.min_matches:
                sentence_preview = sentence[:40] + '...' if len(sentence) > 40 else sentence
                print(f"       Skipping '{sentence_preview}': only {len(matching_sections)} match(es) found (minimum: {args.min_matches})")
                continue
            
            # Format content - now passing all_matches for section boundary calculation
            formatted_content = format_output_content(
                matching_sections, sentence, output_format, input_path.name, content_by_pages, matches
            )
            
            if not formatted_content.strip():
                continue
            
            # Generate output filename
            safe_sentence = sanitize_filename(sentence)
            output_filename = f"{files_created + 1}_{input_path.stem}_{safe_sentence}{file_extension}"
            output_path = output_dir / output_filename
            
            # Write output file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(formatted_content)
            
            sentence_preview = sentence[:40] + '...' if len(sentence) > 40 else sentence
            print(f"       Created '{output_path}' with {len(matching_sections)} matching section(s) for '{sentence_preview}'")
            files_created += 1
            total_matches += len(matching_sections)
        
        # Summary
        if files_created > 0:
            print(f"\n[SUCCESS] Created {files_created} file(s) with {total_matches} total matching sections")
            print(f"          Output directory: {output_dir.absolute()}")
            print(f"          Output format: {output_format} ({file_extension} files)")
        else:
            print(f"\n[WARNING] No output files created - no sentences had sufficient matches")
    
    except FileNotFoundError as e:
        print(f"[ERROR] {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"[ERROR] {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()