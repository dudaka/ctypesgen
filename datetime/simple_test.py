#!/usr/bin/env python3
"""
Simple test program for grass_datetime.py

This is a focused test that demonstrates basic functionality of the GRASS DateTime library
wrapped with ctypesgen. Use this as a starting point for your own datetime operations.
"""

import sys
from ctypes import byref, c_int, c_double

# Import the generated grass_datetime module
try:
    from grass_datetime import DateTime, DATETIME_ABSOLUTE, DATETIME_YEAR, DATETIME_SECOND
    import grass_datetime as gdt
except ImportError as e:
    print(f"Error importing grass_datetime: {e}")
    print("Make sure grass_datetime.py is in the same directory")
    print("and grass_datetime.dll is available in PATH or current directory")
    sys.exit(1)

def create_sample_datetime():
    """Create and return a sample DateTime object"""
    dt = DateTime()
    
    # Set the datetime type (absolute, from year to second precision)
    if hasattr(gdt, 'datetime_set_type'):
        result = gdt.datetime_set_type(byref(dt), DATETIME_ABSOLUTE, DATETIME_YEAR, DATETIME_SECOND, 0)
        print(f"Set datetime type: {result}")
    
    # Set individual values
    dt.year = 2025
    dt.month = 8
    dt.day = 29
    dt.hour = 14
    dt.minute = 30
    dt.second = 45.0
    dt.positive = 1  # Positive datetime
    
    return dt

def print_datetime(dt, label="DateTime"):
    """Print a DateTime object in a readable format"""
    print(f"{label}:")
    print(f"  Date: {dt.year:04d}-{dt.month:02d}-{dt.day:02d}")
    print(f"  Time: {dt.hour:02d}:{dt.minute:02d}:{dt.second:06.3f}")
    print(f"  Mode: {dt.mode}, From: {dt._from}, To: {dt.to}")
    print(f"  Positive: {bool(dt.positive)}")

def test_basic_operations():
    """Test basic datetime operations"""
    print("=== Basic DateTime Operations ===")
    
    # Create a datetime
    dt1 = create_sample_datetime()
    print_datetime(dt1, "Created DateTime")
    
    # Test validation if available
    if hasattr(gdt, 'datetime_is_valid_type'):
        is_valid = gdt.datetime_is_valid_type(byref(dt1))
        print(f"Is valid type: {bool(is_valid)}")
    
    # Test copy if available
    if hasattr(gdt, 'datetime_copy'):
        dt2 = DateTime()
        gdt.datetime_copy(byref(dt2), byref(dt1))
        print_datetime(dt2, "Copied DateTime")
        
        # Test if they are the same
        if hasattr(gdt, 'datetime_is_same'):
            same = gdt.datetime_is_same(byref(dt1), byref(dt2))
            print(f"Original and copy are same: {bool(same)}")
    
    return dt1

def test_utility_functions():
    """Test utility functions"""
    print("\n=== Utility Functions ===")
    
    # Test leap year
    if hasattr(gdt, 'datetime_is_leap_year'):
        leap_2024 = gdt.datetime_is_leap_year(2024, DATETIME_ABSOLUTE)
        leap_2025 = gdt.datetime_is_leap_year(2025, DATETIME_ABSOLUTE)
        print(f"2024 is leap year: {bool(leap_2024)}")
        print(f"2025 is leap year: {bool(leap_2025)}")
    
    # Test days in month
    if hasattr(gdt, 'datetime_days_in_month'):
        days_feb = gdt.datetime_days_in_month(2024, 2, DATETIME_ABSOLUTE)
        days_apr = gdt.datetime_days_in_month(2024, 4, DATETIME_ABSOLUTE)
        print(f"Days in Feb 2024: {days_feb}")
        print(f"Days in Apr 2024: {days_apr}")

def test_getset_functions():
    """Test getter and setter functions"""
    print("\n=== Get/Set Functions ===")
    
    dt = create_sample_datetime()
    
    # Test setting and getting year
    if hasattr(gdt, 'datetime_set_year') and hasattr(gdt, 'datetime_get_year'):
        gdt.datetime_set_year(byref(dt), 2030)
        year = c_int()
        result = gdt.datetime_get_year(byref(dt), byref(year))
        print(f"Set year to 2030, got back: {year.value} (result: {result})")
    
    # Test setting and getting month
    if hasattr(gdt, 'datetime_set_month') and hasattr(gdt, 'datetime_get_month'):
        gdt.datetime_set_month(byref(dt), 12)
        month = c_int()
        result = gdt.datetime_get_month(byref(dt), byref(month))
        print(f"Set month to 12, got back: {month.value} (result: {result})")
    
    # Print final state
    print_datetime(dt, "After modifications")

def test_error_handling():
    """Test error handling"""
    print("\n=== Error Handling ===")
    
    # Clear any existing errors
    if hasattr(gdt, 'datetime_clear_error'):
        gdt.datetime_clear_error()
        print("Cleared error state")
    
    # Check error code
    if hasattr(gdt, 'datetime_error_code'):
        error_code = gdt.datetime_error_code()
        print(f"Current error code: {error_code}")
    
    # Try to cause an error by setting invalid values
    dt = DateTime()
    if hasattr(gdt, 'datetime_set_month'):
        result = gdt.datetime_set_month(byref(dt), 13)  # Invalid month
        print(f"Tried to set month to 13, result: {result}")
        
        # Check error after invalid operation
        if hasattr(gdt, 'datetime_error_code'):
            error_code = gdt.datetime_error_code()
            print(f"Error code after invalid operation: {error_code}")

def main():
    """Main test function"""
    print("GRASS DateTime Library - Simple Test")
    print("=====================================")
    
    try:
        print(f"Available constants:")
        print(f"  DATETIME_ABSOLUTE: {DATETIME_ABSOLUTE}")
        print(f"  DATETIME_YEAR: {DATETIME_YEAR}")
        print(f"  DATETIME_SECOND: {DATETIME_SECOND}")
        
        # Run tests
        test_basic_operations()
        test_utility_functions()
        test_getset_functions()
        test_error_handling()
        
        print("\n=== Test Completed Successfully! ===")
        
    except Exception as e:
        print(f"\nError during testing: {e}")
        print("\nPossible issues:")
        print("1. grass_datetime.dll is not found or not in PATH")
        print("2. DLL architecture mismatch (32-bit vs 64-bit Python)")
        print("3. Missing DLL dependencies")
        print("4. Incorrect grass_datetime.py file")
        
        # Print some diagnostic info
        print(f"\nPython architecture: {sys.maxsize > 2**32 and '64-bit' or '32-bit'}")
        print(f"Python version: {sys.version}")
        
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
