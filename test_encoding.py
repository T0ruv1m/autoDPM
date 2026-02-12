#!/usr/bin/env python3
"""
Test script to verify character encoding fixes for Excel file reading.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.data_loader import load_items, fix_encoding

def test_encoding_fix():
    """Test the encoding fix function - returns True/False without printing Unicode chars"""
    test_cases = [
        ("Ã§Ã£o", "ação"),
        ("Ã¡rea", "área"),
        ("mÃ©dio", "médio"),
        ("polÃ§Ã£o", "polição"),
        ("coraÃ§Ã£o", "coração"),
        ("capacitaÃ§Ã£o", "capacitação"),
        ("comunicaÃ§Ã£o", "comunicação"),
        ("constituiÃ§Ã£o", "constituição"),
        ("educaÃ§Ã£o", "educação"),
        ("organizaÃ§Ã£o", "organização"),
        ("produÃ§Ã£o", "produção"),
        ("qualidade", "qualidade"),
        ("tecnolÃ³gico", "tecnológico"),
    ]
    
    all_passed = True
    for input_text, expected in test_cases:
        result = fix_encoding(input_text)
        if result != expected:
            all_passed = False
            print(f"FAILED: '{input_text}' -> '{result}' (expected: '{expected}')")
    
    return all_passed

def test_special_characters():
    """Test that special characters are preserved correctly"""
    special_chars = ['ã', 'á', 'â', 'ê', 'í', 'ó', 'õ', 'ú', 'ç', 'é', 'è', 'ñ', 'Á', 'É', 'Í', 'Ó', 'Ú']
    test_text = "Test with special chars: " + "".join(special_chars)
    result = fix_encoding(test_text)
    return test_text == result

if __name__ == "__main__":
    print("Character Encoding Test")
    print("=" * 40)
    
    # Test the fix_encoding function
    encoding_test_passed = test_encoding_fix()
    print(f"Encoding fix test: {'PASSED' if encoding_test_passed else 'FAILED'}")
    
    # Test special character preservation
    special_chars_test_passed = test_special_characters()
    print(f"Special chars preservation: {'PASSED' if special_chars_test_passed else 'FAILED'}")
    
    # Test with actual Excel file if it exists
    excel_files = [f for f in os.listdir('.') if f.endswith(('.xlsx', '.xls'))]
    if excel_files:
        print(f"\nFound Excel files: {excel_files}")
        try:
            # Test with the first Excel file found
            items = load_items(excel_files[0])
            print(f"Successfully loaded {len(items)} items from {excel_files[0]}")
            
            # Check for items with special characters
            special_char_items = [item for item in items if any(c in item.descricao for c in 'ãáâêíóõúçÁÉÍÓÚÑ')]
            print(f"Found {len(special_char_items)} items with special characters")
            
            if special_char_items:
                print("\nSample items with special characters (showing as raw strings):")
                for i, item in enumerate(special_char_items[:3]):  # Show first 3
                    print(f"  {i+1}. Descricao: {repr(item.descricao)}, Codigo: {item.codigo_ed}")
            
        except Exception as e:
            print(f"Error loading Excel file: {e}")
    else:
        print("\nNo Excel files found in current directory")
        print("To test with your actual Excel file, place it in the project directory and run this script again.")
    
    print(f"\nOverall test result: {'PASSED' if encoding_test_passed and special_chars_test_passed else 'FAILED'}")