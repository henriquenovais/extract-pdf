#!/usr/bin/env python3
"""
Format slides.txt into a readable markdown file.

Converts raw PDF-extracted text into well-formatted markdown suitable for studying.
"""

import re
import sys
from pathlib import Path


def is_copyright_line(line):
    """Check if a line contains copyright notices or headers."""
    copyright_patterns = [
        r'©\s*Stephane\s*Maarek',
        r'NOT\s+FOR\s+DISTRIBUTION',
        r'www\.datacumulus\.com',
        r'https://links\.datacumulus\.com',
        r'^EXTRA\s+PRACTICE\s+EXAMS$',
        r'^COURSE$',
        r'^Disclaimer:',
    ]
    line_upper = line.upper()
    for pattern in copyright_patterns:
        if re.search(pattern, line, re.IGNORECASE):
            return True
    return False


def extract_title_from_copyright_line(line):
    """Extract slide title from a copyright line if present."""
    # Pattern to match copyright prefix and extract what comes after
    # This handles various copyright formats
    patterns = [
        # Standard format: © Stephane MaarekNOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com <title>
        r'©\s*Stephane\s*MaarekNOT\s+FOR\s+DISTRIBUTION\s*©\s*Stephane\s*Maarek\s*www\.datacumulus\.com\s*(.+?)(?:•|$)',
        # Format with links before title
        r'©\s*Stephane\s*MaarekNOT\s+FOR\s+DISTRIBUTION\s*©\s*Stephane\s*Maarek\s*www\.datacumulus\.com\s*(?:https://links\.datacumulus\.com/[^\s]*\s*)*(.+?)(?:•|$)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, line, re.IGNORECASE)
        if match:
            title = match.group(1).strip()
            # Remove any remaining copyright fragments
            title = re.sub(r'https://links\.datacumulus\.com/[^\s]*\s*', '', title)
            title = re.sub(r'www\.datacumulus\.com\s*', '', title)
            title = re.sub(r'\s+', ' ', title).strip()
            # Only return if it looks like a title (not too long, doesn't start with bullet)
            if title and len(title) > 2 and len(title) < 150 and not title.startswith('•'):
                return title
    return None


def clean_line(line):
    """Remove copyright notices from a line while preserving content."""
    # Remove copyright prefix patterns
    line = re.sub(r'^©\s*Stephane\s*MaarekNOT\s+FOR\s+DISTRIBUTION\s*©\s*Stephane\s*Maarek\s*www\.datacumulus\.com\s*', '', line)
    line = re.sub(r'https://links\.datacumulus\.com/[^\s]*\s*', '', line)
    line = re.sub(r'www\.datacumulus\.com\s*', '', line)
    # Remove any remaining copyright fragments
    line = re.sub(r'©\s*Stephane\s*Maarek\s*', '', line, flags=re.IGNORECASE)
    line = re.sub(r'NOT\s+FOR\s+DISTRIBUTION\s*', '', line, flags=re.IGNORECASE)
    
    # Clean up multiple spaces but preserve single spaces
    line = re.sub(r'\s+', ' ', line)
    return line.strip()


def is_likely_diagram_element(line):
    """Check if a line is likely a diagram element (not real content)."""
    # Single words that are likely diagram labels
    if len(line.split()) <= 2 and line.isalpha() and len(line) < 20:
        # Common diagram labels
        if line.lower() in ['alice', 'bob', 'charles', 'david', 'edward', 'fred', 'www', 'ram']:
            return True
        # Single capitalized words
        if line[0].isupper() and line.isalpha():
            return True
    
    # Lines that are just symbols or very short
    if len(line.strip()) <= 3 and not line.strip().endswith('.'):
        return True
    
    return False


def is_section_header(line, context):
    """Determine if a line is a section header based on context."""
    if not line or len(line) < 5:
        return False
    
    # Skip if it looks like a diagram element
    if is_likely_diagram_element(line):
        return False
    
    # Lines that are all caps and reasonable length (likely headers)
    if line.isupper() and 10 <= len(line) <= 100:
        return True
    
    # Lines that start with capital and contain AWS/service keywords
    if line[0].isupper():
        aws_keywords = [
            'AWS', 'Amazon', 'EC2', 'S3', 'IAM', 'RDS', 'Route 53', 'VPC',
            'Elastic', 'CloudFront', 'DynamoDB', 'Lambda', 'SNS', 'SQS',
            'ElastiCache', 'Aurora', 'CloudFormation', 'CloudWatch', 'CloudTrail',
            'Kinesis', 'API Gateway', 'Step Functions', 'Cognito', 'SES',
            'Elastic Beanstalk', 'ECS', 'EKS', 'EBS', 'EFS', 'FSx',
            'Direct Connect', 'Snowball', 'DataSync', 'Batch', 'Glue',
            'Redshift', 'Athena', 'EMR', 'SageMaker', 'Rekognition',
            'Comprehend', 'Translate', 'Polly', 'Transcribe', 'Textract',
            'GuardDuty', 'WAF', 'Shield', 'Secrets Manager', 'Certificate Manager',
            'Systems Manager', 'Config', 'Trusted Advisor', 'Cost Explorer',
            'Outposts', 'AppFlow', 'Amplify'
        ]
        for keyword in aws_keywords:
            if keyword in line and len(line) < 120:
                # Not a bullet point
                if not line.startswith('•') and '•' not in line[:20]:
                    return True
        
        # Pattern: "Service - Subsection" or "Service: Subsection"
        if re.match(r'^[A-Z][^•]*?\s*[-–—:]\s*[A-Z]', line) and len(line) < 100:
            # Contains a dash or colon separating likely title parts
            # Not ending with punctuation that suggests it's a sentence
            if not line.endswith('.') and not line.endswith(','):
                return True
    
    return False


def format_bullet_points(text):
    """Convert bullet points (•) to markdown list format."""
    if '•' not in text:
        return text
    
    # Split by bullet points
    parts = text.split('•')
    formatted = []
    for part in parts:
        part = part.strip()
        if part:
            # Check if this part itself contains nested bullets (indicated by colon)
            if ':' in part and not part.startswith('http'):
                # Try to format as nested list
                main_part, rest = part.split(':', 1)
                formatted.append(f"- **{main_part.strip()}**: {rest.strip()}")
            else:
                formatted.append(f"- {part}")
    
    return '\n'.join(formatted) if formatted else text


def is_json_code(line):
    """Check if a line looks like JSON code."""
    line_stripped = line.strip()
    return (line_stripped.startswith('{') or 
            line_stripped.startswith('[') or
            (line_stripped.startswith('"') and ':' in line_stripped and 
             ('Version' in line_stripped or 'Effect' in line_stripped or 'Action' in line_stripped)))


def format_urls(text):
    """Convert URLs to markdown links."""
    url_pattern = r'(https?://[^\s\)]+)'
    def replace_url(match):
        url = match.group(1)
        # Remove trailing punctuation from URL
        url_clean = url.rstrip('.,;:!?)')
        return f'[{url_clean}]({url_clean})'
    return re.sub(url_pattern, replace_url, text)


def format_slides(input_file, output_file):
    """Main function to format slides from text to markdown."""
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    formatted_lines = []
    in_code_block = False
    code_block_lines = []
    prev_line_empty = False
    prev_line_was_copyright = False
    skip_next_empty = False
    pending_slide_title = None  # Title extracted from copyright line
    in_slide = False  # Track if we're inside a slide (after the main title)
    first_slide = True  # Track if this is the first slide (no separator before)
    previous_main_title = None  # Track previous main slide title to detect subsections
    
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        original_line = line
        
        # Skip empty lines at the very start
        if not formatted_lines and not line.strip():
            i += 1
            continue
        
        # Check if this is a copyright line
        is_copyright = is_copyright_line(line)
        if is_copyright:
            # If we have a pending title from previous copyright line, process it first
            if pending_slide_title:
                # Determine if this should be a subsection (##) or main slide (#)
                is_subsection = False
                if previous_main_title:
                    # Check if title contains a dash (e.g., "DynamoDB - Basics")
                    if ' - ' in pending_slide_title or ' – ' in pending_slide_title:
                        is_subsection = True
                    else:
                        # Check if title starts with a word from previous title
                        prev_words = set(previous_main_title.split())
                        current_words = set(pending_slide_title.split())
                        # If there's significant overlap or current title starts with a prev word
                        if current_words.intersection(prev_words):
                            # Additional check: if current title is shorter/more specific
                            if len(pending_slide_title) < len(previous_main_title) or \
                               any(pending_slide_title.startswith(word) for word in prev_words if len(word) > 3):
                                is_subsection = True
                
                # Add separator before new slide (except first slide and subsections)
                if not first_slide and not is_subsection and formatted_lines and formatted_lines[-1] != '':
                    formatted_lines.append('')
                    formatted_lines.append('---')
                    formatted_lines.append('')
                first_slide = False
                
                # Use appropriate header level
                if is_subsection:
                    formatted_lines.append(f"## {pending_slide_title}")
                    formatted_lines.append('')
                    # Keep the same main title for subsequent checks
                else:
                    formatted_lines.append(f"# {pending_slide_title}")
                    formatted_lines.append('')
                    previous_main_title = pending_slide_title
                in_slide = True
            
            # Extract title from current copyright line if present
            extracted_title = extract_title_from_copyright_line(line)
            if extracted_title:
                pending_slide_title = extracted_title
            else:
                pending_slide_title = None
            
            prev_line_was_copyright = True
            skip_next_empty = True
            in_slide = False  # Reset slide state for new slide (will be set to True when title is processed)
            i += 1
            continue
        
        # Clean the line
        cleaned = clean_line(line)
        
        # Skip if line is empty after cleaning
        if not cleaned:
            if skip_next_empty:
                skip_next_empty = False
                i += 1
                continue
            if formatted_lines and formatted_lines[-1] != '':
                formatted_lines.append('')
            prev_line_empty = True
            prev_line_was_copyright = False
            i += 1
            continue
        
        # Handle slide title after copyright
        if prev_line_was_copyright:
            # Check if we have a pending title from copyright line
            if pending_slide_title:
                # Determine if this should be a subsection (##) or main slide (#)
                is_subsection = False
                if previous_main_title:
                    # Check if title contains a dash (e.g., "DynamoDB - Basics")
                    if ' - ' in pending_slide_title or ' – ' in pending_slide_title:
                        is_subsection = True
                    else:
                        # Check if title starts with a word from previous title
                        prev_words = set(previous_main_title.split())
                        current_words = set(pending_slide_title.split())
                        # If there's significant overlap or current title starts with a prev word
                        if current_words.intersection(prev_words):
                            # Additional check: if current title is shorter/more specific
                            if len(pending_slide_title) < len(previous_main_title) or \
                               any(pending_slide_title.startswith(word) for word in prev_words if len(word) > 3):
                                is_subsection = True
                
                # Add separator before new slide (except first slide and subsections)
                if not first_slide and not is_subsection and formatted_lines and formatted_lines[-1] != '':
                    formatted_lines.append('')
                    formatted_lines.append('---')
                    formatted_lines.append('')
                first_slide = False
                
                # Use appropriate header level
                if is_subsection:
                    formatted_lines.append(f"## {pending_slide_title}")
                    formatted_lines.append('')
                else:
                    formatted_lines.append(f"# {pending_slide_title}")
                    formatted_lines.append('')
                    previous_main_title = pending_slide_title
                pending_slide_title = None
                in_slide = True
                prev_line_was_copyright = False
                i += 1
                continue
            # If no title extracted, check if this line is a section header
            elif is_section_header(cleaned, {'prev_empty': prev_line_empty}):
                # Determine if this should be a subsection
                is_subsection = False
                if previous_main_title:
                    if ' - ' in cleaned or ' – ' in cleaned:
                        is_subsection = True
                    else:
                        prev_words = set(previous_main_title.split())
                        current_words = set(cleaned.split())
                        if current_words.intersection(prev_words):
                            if len(cleaned) < len(previous_main_title) or \
                               any(cleaned.startswith(word) for word in prev_words if len(word) > 3):
                                is_subsection = True
                
                # Add separator before new slide (except first slide and subsections)
                if not first_slide and not is_subsection and formatted_lines and formatted_lines[-1] != '':
                    formatted_lines.append('')
                    formatted_lines.append('---')
                    formatted_lines.append('')
                first_slide = False
                
                # Use appropriate header level
                if is_subsection:
                    formatted_lines.append(f"## {cleaned}")
                    formatted_lines.append('')
                else:
                    formatted_lines.append(f"# {cleaned}")
                    formatted_lines.append('')
                    previous_main_title = cleaned
                in_slide = True
                prev_line_was_copyright = False
                i += 1
                continue
        
        # Check if we're entering a code block (JSON)
        if is_json_code(cleaned) and not in_code_block:
            in_code_block = True
            code_block_lines = [cleaned]
            i += 1
            continue
        
        # Collect code block lines
        if in_code_block:
            if cleaned.strip() and (is_json_code(cleaned) or 
                                   cleaned.strip().startswith('"') or 
                                   cleaned.strip().startswith('}') or 
                                   cleaned.strip().startswith(']') or
                                   cleaned.strip().startswith(',') or
                                   'Resource' in cleaned or 'Action' in cleaned):
                code_block_lines.append(cleaned)
                i += 1
                continue
            else:
                # End of code block
                if code_block_lines:
                    # Try to format JSON nicely
                    json_text = ' '.join(code_block_lines)
                    formatted_lines.append('```json')
                    # Try to add some basic formatting
                    json_text = json_text.replace('{', '{\n    ')
                    json_text = json_text.replace('}', '\n}')
                    json_text = json_text.replace(',', ',\n    ')
                    formatted_lines.append(json_text)
                    formatted_lines.append('```')
                    formatted_lines.append('')
                in_code_block = False
                code_block_lines = []
                # Don't increment i, process this line normally
        
        # Skip diagram elements
        if is_likely_diagram_element(cleaned):
            prev_line_empty = False
            prev_line_was_copyright = False
            i += 1
            continue
        
        # Check if this is a subsection header (when already inside a slide)
        if in_slide and not prev_line_was_copyright:
            # Check if next line has content (not just empty or copyright)
            has_content_after = False
            next_line_idx = i + 1
            while next_line_idx < len(lines) and next_line_idx <= i + 3:  # Check up to 3 lines ahead
                next_line = lines[next_line_idx].strip()
                if not next_line:
                    next_line_idx += 1
                    continue
                if is_copyright_line(next_line):
                    break
                # Found non-empty content, this could be a subsection header
                if len(next_line) > 5:
                    has_content_after = True
                    break
                next_line_idx += 1
            
            if has_content_after and is_section_header(cleaned, {'prev_empty': prev_line_empty}):
                if formatted_lines and formatted_lines[-1] != '':
                    formatted_lines.append('')
                formatted_lines.append(f"## {cleaned}")
                formatted_lines.append('')
                prev_line_empty = False
                prev_line_was_copyright = False
                i += 1
                continue
        
        # Format bullet points
        if '•' in cleaned:
            # Format URLs in the text
            cleaned = format_urls(cleaned)
            bullet_formatted = format_bullet_points(cleaned)
            formatted_lines.append(bullet_formatted)
            prev_line_empty = False
            prev_line_was_copyright = False
            i += 1
            continue
        
        # Regular content line
        # Format URLs
        cleaned = format_urls(cleaned)
        
        # Check if it's a sub-header (short line, capitalized, looks like a title)
        # Skip this if we're in a slide and it might be a subsection (already handled above)
        if (not in_slide or not is_section_header(cleaned, {})) and \
           (len(cleaned) < 70 and cleaned[0].isupper() and 
            not cleaned.endswith('.') and not cleaned.endswith(',') and
            i + 1 < len(lines) and lines[i+1].strip() and
            not any(char in cleaned for char in ['•', ':', '=']) and
            not cleaned.startswith('http')):
            # Check if next line is content (not empty, not copyright)
            next_line = lines[i+1].strip() if i+1 < len(lines) else ''
            if next_line and not is_copyright_line(next_line) and len(next_line) > 10:
                # Use ### for minor sub-headers when not in a slide
                formatted_lines.append(f"### {cleaned}")
                formatted_lines.append('')
            else:
                formatted_lines.append(cleaned)
        else:
            formatted_lines.append(cleaned)
        
        prev_line_empty = False
        prev_line_was_copyright = False
        i += 1
    
    # Handle any pending slide title at the end
    if pending_slide_title:
        # Determine if this should be a subsection
        is_subsection = False
        if previous_main_title:
            if ' - ' in pending_slide_title or ' – ' in pending_slide_title:
                is_subsection = True
            else:
                prev_words = set(previous_main_title.split())
                current_words = set(pending_slide_title.split())
                if current_words.intersection(prev_words):
                    if len(pending_slide_title) < len(previous_main_title) or \
                       any(pending_slide_title.startswith(word) for word in prev_words if len(word) > 3):
                        is_subsection = True
        
        # Add separator before new slide (except first slide and subsections)
        if not first_slide and not is_subsection and formatted_lines and formatted_lines[-1] != '':
            formatted_lines.append('')
            formatted_lines.append('---')
            formatted_lines.append('')
        
        # Use appropriate header level
        if is_subsection:
            formatted_lines.append(f"## {pending_slide_title}")
        else:
            formatted_lines.append(f"# {pending_slide_title}")
        formatted_lines.append('')
    
    # Handle any remaining code block
    if in_code_block and code_block_lines:
        json_text = ' '.join(code_block_lines)
        formatted_lines.append('```json')
        formatted_lines.append(json_text)
        formatted_lines.append('```')
    
    # Clean up excessive empty lines
    cleaned_lines = []
    prev_empty = False
    for line in formatted_lines:
        if not line.strip():
            if not prev_empty:
                cleaned_lines.append('')
            prev_empty = True
        else:
            cleaned_lines.append(line)
            prev_empty = False
    
    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('# AWS Solutions Architect Associate - Study Notes\n\n')
        f.write('*Formatted from course slides*\n\n')
        f.write('---\n\n')
        f.write('\n'.join(cleaned_lines))
        if cleaned_lines and cleaned_lines[-1]:
            f.write('\n')
    
    print(f"Successfully formatted {input_file} -> {output_file}")
    print(f"Processed {len(lines)} input lines into {len(cleaned_lines)} formatted lines")


def main():
    """Main entry point."""
    input_file = Path('slides.txt')
    output_file = Path('slides.md')
    
    if not input_file.exists():
        print(f"Error: {input_file} not found.")
        sys.exit(1)
    
    try:
        format_slides(input_file, output_file)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
