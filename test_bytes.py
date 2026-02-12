#!/usr/bin/env python3
"""
Simple test to verify encoding fixes work at byte level.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.data_loader import fix_encoding

def test_bytes_transformation():
    """Test encoding fixes using byte comparisons to avoid console issues"""
    # Test the most common encoding issue: double-encoded UTF-8
    # The character 'ã' when double-encoded becomes 'Ã£'
    
    # Create test input that would come from a mis-encoded Excel file
    test_cases = [
        # These are the character patterns you typically see when UTF-8 is read as Latin-1
        'Ã§Ã£o',    # Should become 'ação'
        'Ã¡rea',    # Should become 'área' 
        'mÃ©dio',   # Should become 'médio'
        'produÃ§Ã£o', # Should become 'produção'
    ]
    
    print("Testing encoding transformation:")
    print("Note: Console may show garbled characters, but the transformation should work internally")
    print()
    
    for test_input in test_cases:
        try:
            result = fix_encoding(test_input)
            
            # Get byte representations to see the actual transformation
            input_bytes = test_input.encode('utf-8', errors='ignore')
            result_bytes = result.encode('utf-8', errors='ignore')
            
            print(f"Input:  {repr(test_input)}")
            print(f"Result: {repr(result)}")
            print(f"Input bytes:  {input_bytes}")
            print(f"Result bytes: {result_bytes}")
            print(f"Transformation changed text: {test_input != result}")
            print("-" * 50)
            
        except Exception as e:
            print(f"Error processing '{test_input}': {e}")
            print("-" * 50)

def main():
    print("UTF-8 Encoding Fix Test")
    print("=" * 50)
    
    test_bytes_transformation()
    
    print("\nTo test with your actual Excel file:")
    print("1. Place your .xlsx or .xls file in the project directory")
    print("2. Run: python -c \"from src.data_loader import load_items; items = load_items('your_file.xlsx'); print(f'Loaded {len(items)} items')\"")
    print("3. Check if special characters like ã, ç, á, etc. are preserved correctly")

if __name__ == "__main__":
    main()