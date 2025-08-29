#!/usr/bin/env python3
"""
Minimal test for grass_datetime.py - Just verify library loading and basic functionality
"""

import sys
import os

def test_import():
    """Test if we can import the grass_datetime module"""
    print("Testing grass_datetime import...")
    try:
        import grass_datetime
        print("✓ Successfully imported grass_datetime")
        return grass_datetime
    except ImportError as e:
        print(f"✗ Failed to import grass_datetime: {e}")
        return None

def test_constants(gdt):
    """Test if constants are available"""
    print("\nTesting constants...")
    constants = ['DATETIME_ABSOLUTE', 'DATETIME_RELATIVE', 'DATETIME_YEAR', 'DATETIME_SECOND']
    
    for const in constants:
        if hasattr(gdt, const):
            value = getattr(gdt, const)
            print(f"✓ {const}: {value}")
        else:
            print(f"✗ {const}: not found")

def test_datetime_creation(gdt):
    """Test basic DateTime structure creation"""
    print("\nTesting DateTime creation...")
    try:
        dt = gdt.DateTime()
        print("✓ Created DateTime structure")
        print(f"  Initial values - Year: {dt.year}, Month: {dt.month}, Day: {dt.day}")
        return dt
    except Exception as e:
        print(f"✗ Failed to create DateTime: {e}")
        return None

def test_function_availability(gdt):
    """Test which functions are available"""
    print("\nChecking function availability...")
    
    test_functions = [
        'datetime_set_type',
        'datetime_is_valid_type', 
        'datetime_set_year',
        'datetime_get_year',
        'datetime_is_leap_year',
        'datetime_days_in_month',
        'datetime_copy',
        'datetime_is_same'
    ]
    
    available = []
    for func_name in test_functions:
        if hasattr(gdt, func_name):
            print(f"✓ {func_name}")
            available.append(func_name)
        else:
            print(f"✗ {func_name}")
    
    return available

def test_simple_function_call(gdt, available_functions):
    """Test calling a simple function if available"""
    print("\nTesting simple function calls...")
    
    # Try leap year function (doesn't require DateTime structure)
    if 'datetime_is_leap_year' in available_functions:
        try:
            result = gdt.datetime_is_leap_year(2024, gdt.DATETIME_ABSOLUTE)
            print(f"✓ datetime_is_leap_year(2024): {bool(result)} (2024 is leap year)")
        except Exception as e:
            print(f"✗ datetime_is_leap_year failed: {e}")
    
    # Try days in month function
    if 'datetime_days_in_month' in available_functions:
        try:
            result = gdt.datetime_days_in_month(2024, 2, gdt.DATETIME_ABSOLUTE)
            print(f"✓ datetime_days_in_month(2024, Feb): {result} days")
        except Exception as e:
            print(f"✗ datetime_days_in_month failed: {e}")

def main():
    """Main test function"""
    print("="*50)
    print("GRASS DateTime - Minimal Test")
    print("="*50)
    
    # Test import
    gdt = test_import()
    if not gdt:
        print("\nCannot proceed without successful import.")
        print("Make sure:")
        print("1. grass_datetime.py is in the current directory")
        print("2. grass_datetime.dll is in current directory or PATH")
        print("3. All dependencies are available")
        return 1
    
    # Test constants
    test_constants(gdt)
    
    # Test DateTime creation
    dt = test_datetime_creation(gdt)
    
    # Check function availability
    available_functions = test_function_availability(gdt)
    
    # Test simple function calls
    if available_functions:
        test_simple_function_call(gdt, available_functions)
    else:
        print("\nNo functions available to test!")
        return 1
    
    print("\n" + "="*50)
    print("Minimal test completed!")
    print("="*50)
    
    if dt and available_functions:
        print("✓ Library appears to be working correctly")
        print(f"✓ {len(available_functions)} functions are available")
        return 0
    else:
        print("✗ Some issues detected")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
