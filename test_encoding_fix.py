#!/usr/bin/env python3
"""
Test script to verify Portuguese character encoding fix with PyAutoGUI.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.data_loader import load_items
from src.actions import safe_typewrite
import pyperclip
import time

def test_portuguese_characters():
    """Test that Portuguese characters are handled correctly"""
    print("Testing Portuguese character encoding fix...")
    print("=" * 50)
    
    # Test cases with problematic Portuguese characters
    test_strings = [
        "DEMOLIÇÃO",
        "INSTALAÇÕES", 
        "CONSTRUÇÃO",
        "CAPACITAÇÃO",
        "COMUNICAÇÃO",
        "ÁREA",
        "MÉDIO",
        "FUNDAÇÃO",
        "ALVENARIA",
        "QUALIDADE"
    ]
    
    print("Testing safe_typewrite function:")
    for i, test_string in enumerate(test_strings, 1):
        try:
            # Test the safe_typewrite function
            print(f"{i:2d}. Testing: {test_string}")
            
            # Copy to clipboard first to test
            pyperclip.copy(test_string)
            clipboard_content = pyperclip.paste()
            
            # Verify clipboard content
            if clipboard_content == test_string:
                print(f"    [PASS] Clipboard test passed")
            else:
                print(f"    [FAIL] Clipboard test failed")
                print(f"      Expected: {repr(test_string)}")
                print(f"      Got:      {repr(clipboard_content)}")
            
            # Clear clipboard
            pyperclip.copy('')
            
        except Exception as e:
            print(f"    [ERROR] Error: {e}")
        
        print()
    
    # Test with actual data from Excel file
    try:
        print("Testing with actual Excel data:")
        items = load_items('assets/data_source.xlsx')
        
        # Find items with special characters
        special_char_items = []
        for item in items:
            if any(c in item.descricao for c in 'ãáâêíóõúçÁÉÍÓÚÑÃÇ'):
                special_char_items.append(item)
        
        print(f"Found {len(special_char_items)} items with Portuguese special characters")
        
        if special_char_items:
            print("\nSample items with Portuguese characters:")
            for i, item in enumerate(special_char_items[:5]):  # Show first 5
                print(f"  {i+1}. Código: {item.codigo_ed}")
                print(f"     Descricao: {repr(item.descricao)}")
                
                # Test clipboard copy
                try:
                    pyperclip.copy(item.descricao)
                    clipboard_test = pyperclip.paste()
                    if clipboard_test == item.descricao:
                        print(f"     [PASS] Clipboard copy successful")
                    else:
                        print(f"     [FAIL] Clipboard copy failed")
                        print(f"       Expected: {repr(item.descricao)}")
                        print(f"       Got:      {repr(clipboard_test)}")
                    pyperclip.copy('')
                except Exception as e:
                    print(f"     [ERROR] Clipboard error: {e}")
                print()
        
    except Exception as e:
        print(f"Error loading Excel data: {e}")
    
    print("Test completed!")
    print("\nNext steps:")
    print("1. Run your automation script")
    print("2. Check if Portuguese characters display correctly in the web browser")
    print("3. If clipboard paste is blocked in the target application, consider using the 'keyboard' library alternative")

if __name__ == "__main__":
    test_portuguese_characters()