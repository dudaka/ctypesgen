#!/usr/bin/env python3
"""
Test program for grass_datetime.py generated from ctypesgen

This program demonstrates and tests various datetime functions from the GRASS DateTime library
that have been wrapped using ctypesgen.

Make sure the grass_datetime.dll is in the same directory or in your PATH before running this script.
"""

import sys
import os
from ctypes import byref, c_int, c_double, POINTER, create_string_buffer

# Import the generated grass_datetime module
try:
    from grass_datetime import *
except ImportError as e:
    print(f"Failed to import grass_datetime: {e}")
    print("Make sure grass_datetime.py is in the same directory and grass_datetime.dll is available")
    sys.exit(1)

def print_separator(title):
    """Print a section separator"""
    print("\n" + "="*60)
    print(f" {title}")
    print("="*60)

def print_datetime_info(dt, name="DateTime"):
    """Print detailed information about a DateTime structure"""
    print(f"{name} Structure:")
    print(f"  Mode: {dt.mode}")
    print(f"  From: {dt._from}")
    print(f"  To: {dt.to}")
    print(f"  Year: {dt.year}")
    print(f"  Month: {dt.month}")
    print(f"  Day: {dt.day}")
    print(f"  Hour: {dt.hour}")
    print(f"  Minute: {dt.minute}")
    print(f"  Second: {dt.second:.3f}")
    print(f"  Positive: {dt.positive}")
    print(f"  Timezone: {dt.tz}")
    print(f"  Fracsec: {dt.fracsec}")

def test_basic_datetime_creation():
    """Test basic DateTime structure creation and manipulation"""
    print_separator("BASIC DATETIME CREATION")
    
    # Create a DateTime structure
    dt = DateTime()
    print("Created empty DateTime structure:")
    print_datetime_info(dt, "Empty DateTime")
    
    # Manually set some values
    dt.year = 2025
    dt.month = 8
    dt.day = 29
    dt.hour = 14
    dt.minute = 30
    dt.second = 45.5
    dt.positive = 1
    
    print("\nAfter manually setting values:")
    print_datetime_info(dt, "Manual DateTime")
    
    return dt

def test_datetime_type_functions():
    """Test datetime type validation and setting functions"""
    print_separator("DATETIME TYPE FUNCTIONS")
    
    dt = DateTime()
    
    # Test setting type
    print("Testing datetime_set_type...")
    if 'datetime_set_type' in globals():
        result = datetime_set_type(byref(dt), DATETIME_ABSOLUTE, DATETIME_YEAR, DATETIME_SECOND, 0)
        print(f"datetime_set_type result: {result}")
        print_datetime_info(dt, "After set_type")
    else:
        print("datetime_set_type function not available")
    
    # Test type validation
    print("\nTesting datetime_is_valid_type...")
    if 'datetime_is_valid_type' in globals():
        is_valid = datetime_is_valid_type(byref(dt))
        print(f"Is valid type: {bool(is_valid)}")
    else:
        print("datetime_is_valid_type function not available")
    
    # Test absolute/relative checks
    print("\nTesting absolute/relative checks...")
    if 'datetime_is_absolute' in globals():
        is_abs = datetime_is_absolute(byref(dt))
        print(f"Is absolute: {bool(is_abs)}")
    
    if 'datetime_is_relative' in globals():
        is_rel = datetime_is_relative(byref(dt))
        print(f"Is relative: {bool(is_rel)}")
    
    return dt

def test_datetime_values():
    """Test setting and getting individual datetime values"""
    print_separator("DATETIME VALUE FUNCTIONS")
    
    dt = DateTime()
    
    # Set up a basic datetime type first
    if 'datetime_set_type' in globals():
        datetime_set_type(byref(dt), DATETIME_ABSOLUTE, DATETIME_YEAR, DATETIME_SECOND, 0)
    
    # Test setting individual values
    print("Setting individual datetime values...")
    
    if 'datetime_set_year' in globals():
        result = datetime_set_year(byref(dt), 2025)
        print(f"Set year to 2025: {result}")
    
    if 'datetime_set_month' in globals():
        result = datetime_set_month(byref(dt), 8)
        print(f"Set month to 8: {result}")
    
    if 'datetime_set_day' in globals():
        result = datetime_set_day(byref(dt), 29)
        print(f"Set day to 29: {result}")
    
    if 'datetime_set_hour' in globals():
        result = datetime_set_hour(byref(dt), 14)
        print(f"Set hour to 14: {result}")
    
    if 'datetime_set_minute' in globals():
        result = datetime_set_minute(byref(dt), 30)
        print(f"Set minute to 30: {result}")
    
    if 'datetime_set_second' in globals():
        result = datetime_set_second(byref(dt), 45.5)
        print(f"Set second to 45.5: {result}")
    
    print("\nAfter setting values:")
    print_datetime_info(dt, "Set Values DateTime")
    
    # Test getting individual values
    print("\nGetting individual datetime values...")
    
    if 'datetime_get_year' in globals():
        year = c_int()
        result = datetime_get_year(byref(dt), byref(year))
        print(f"Get year: {year.value} (result: {result})")
    
    if 'datetime_get_month' in globals():
        month = c_int()
        result = datetime_get_month(byref(dt), byref(month))
        print(f"Get month: {month.value} (result: {result})")
    
    if 'datetime_get_day' in globals():
        day = c_int()
        result = datetime_get_day(byref(dt), byref(day))
        print(f"Get day: {day.value} (result: {result})")
    
    if 'datetime_get_second' in globals():
        second = c_double()
        result = datetime_get_second(byref(dt), byref(second))
        print(f"Get second: {second.value:.3f} (result: {result})")
    
    return dt

def test_datetime_validation():
    """Test datetime validation functions"""
    print_separator("DATETIME VALIDATION")
    
    dt = DateTime()
    
    # Set up a datetime
    if 'datetime_set_type' in globals():
        datetime_set_type(byref(dt), DATETIME_ABSOLUTE, DATETIME_YEAR, DATETIME_SECOND, 0)
    
    # Test validation functions
    print("Testing validation functions...")
    
    # Test year validation
    if 'datetime_check_year' in globals():
        valid_year = datetime_check_year(byref(dt), 2025)
        invalid_year = datetime_check_year(byref(dt), -1)
        print(f"Year 2025 valid: {bool(valid_year)}")
        print(f"Year -1 valid: {bool(invalid_year)}")
    
    # Test month validation
    if 'datetime_check_month' in globals():
        valid_month = datetime_check_month(byref(dt), 8)
        invalid_month = datetime_check_month(byref(dt), 13)
        print(f"Month 8 valid: {bool(valid_month)}")
        print(f"Month 13 valid: {bool(invalid_month)}")
    
    # Test day validation
    if 'datetime_check_day' in globals():
        valid_day = datetime_check_day(byref(dt), 29)
        invalid_day = datetime_check_day(byref(dt), 32)
        print(f"Day 29 valid: {bool(valid_day)}")
        print(f"Day 32 valid: {bool(invalid_day)}")

def test_datetime_utility_functions():
    """Test utility functions like leap year, days in month, etc."""
    print_separator("UTILITY FUNCTIONS")
    
    # Test leap year function
    if 'datetime_is_leap_year' in globals():
        print("Testing leap year function...")
        leap_2024 = datetime_is_leap_year(2024, DATETIME_ABSOLUTE)
        leap_2025 = datetime_is_leap_year(2025, DATETIME_ABSOLUTE)
        print(f"2024 is leap year: {bool(leap_2024)}")
        print(f"2025 is leap year: {bool(leap_2025)}")
    
    # Test days in month
    if 'datetime_days_in_month' in globals():
        print("\nTesting days in month function...")
        days_feb_2024 = datetime_days_in_month(2024, 2, DATETIME_ABSOLUTE)  # Leap year
        days_feb_2025 = datetime_days_in_month(2025, 2, DATETIME_ABSOLUTE)  # Not leap year
        days_dec = datetime_days_in_month(2025, 12, DATETIME_ABSOLUTE)
        print(f"Days in Feb 2024 (leap): {days_feb_2024}")
        print(f"Days in Feb 2025 (normal): {days_feb_2025}")
        print(f"Days in Dec 2025: {days_dec}")
    
    # Test days in year
    if 'datetime_days_in_year' in globals():
        print("\nTesting days in year function...")
        days_2024 = datetime_days_in_year(2024, DATETIME_ABSOLUTE)
        days_2025 = datetime_days_in_year(2025, DATETIME_ABSOLUTE)
        print(f"Days in 2024: {days_2024}")
        print(f"Days in 2025: {days_2025}")

def test_datetime_operations():
    """Test datetime operations like copy, difference, etc."""
    print_separator("DATETIME OPERATIONS")
    
    # Create two datetime objects
    dt1 = DateTime()
    dt2 = DateTime()
    
    if 'datetime_set_type' in globals():
        datetime_set_type(byref(dt1), DATETIME_ABSOLUTE, DATETIME_YEAR, DATETIME_SECOND, 0)
        datetime_set_type(byref(dt2), DATETIME_ABSOLUTE, DATETIME_YEAR, DATETIME_SECOND, 0)
    
    # Set different values
    dt1.year = 2025
    dt1.month = 8
    dt1.day = 29
    dt1.hour = 14
    dt1.minute = 30
    dt1.second = 0
    
    dt2.year = 2025
    dt2.month = 8
    dt2.day = 30
    dt2.hour = 16
    dt2.minute = 45
    dt2.second = 30
    
    print("Created two DateTime objects:")
    print_datetime_info(dt1, "DateTime 1")
    print_datetime_info(dt2, "DateTime 2")
    
    # Test copy function
    if 'datetime_copy' in globals():
        dt_copy = DateTime()
        datetime_copy(byref(dt_copy), byref(dt1))
        print("\nAfter copying dt1 to dt_copy:")
        print_datetime_info(dt_copy, "Copied DateTime")
    
    # Test same function
    if 'datetime_is_same' in globals():
        same_result = datetime_is_same(byref(dt1), byref(dt2))
        same_copy = datetime_is_same(byref(dt1), byref(dt_copy)) if 'datetime_copy' in globals() else False
        print(f"\ndt1 same as dt2: {bool(same_result)}")
        if 'datetime_copy' in globals():
            print(f"dt1 same as dt_copy: {bool(same_copy)}")

def test_datetime_formatting():
    """Test datetime formatting functions"""
    print_separator("DATETIME FORMATTING")
    
    dt = DateTime()
    
    # Set up a datetime
    if 'datetime_set_type' in globals():
        datetime_set_type(byref(dt), DATETIME_ABSOLUTE, DATETIME_YEAR, DATETIME_SECOND, 0)
    
    dt.year = 2025
    dt.month = 8
    dt.day = 29
    dt.hour = 14
    dt.minute = 30
    dt.second = 45.5
    
    print("DateTime to format:")
    print_datetime_info(dt, "Format Test DateTime")
    
    # Test formatting (if available)
    if 'datetime_format' in globals():
        print("\nTesting datetime_format function...")
        buffer_size = 100
        buffer = create_string_buffer(buffer_size)
        result = datetime_format(byref(dt), buffer)
        print(f"Format result: {result}")
        if result == 0:  # Assuming 0 means success
            print(f"Formatted string: '{buffer.value.decode()}'")
        else:
            print("Formatting failed or returned error")

def test_error_handling():
    """Test error handling functions"""
    print_separator("ERROR HANDLING")
    
    # Test error functions
    if 'datetime_error_code' in globals():
        error_code = datetime_error_code()
        print(f"Current error code: {error_code}")
    
    if 'datetime_error_msg' in globals():
        try:
            error_msg = datetime_error_msg()
            print(f"Current error message: '{error_msg}'")
        except Exception as e:
            print(f"Error getting error message: {e}")
    
    if 'datetime_clear_error' in globals():
        datetime_clear_error()
        print("Cleared error state")

def test_constants():
    """Test and display available constants"""
    print_separator("AVAILABLE CONSTANTS")
    
    constants = [
        'DATETIME_ABSOLUTE', 'DATETIME_RELATIVE',
        'DATETIME_YEAR', 'DATETIME_MONTH', 'DATETIME_DAY',
        'DATETIME_HOUR', 'DATETIME_MINUTE', 'DATETIME_SECOND'
    ]
    
    print("Available constants:")
    for const_name in constants:
        if const_name in globals():
            value = globals()[const_name]
            print(f"  {const_name}: {value}")
        else:
            print(f"  {const_name}: NOT AVAILABLE")

def main():
    """Main test function"""
    print("="*60)
    print(" GRASS DateTime Library Test Program")
    print(" Generated bindings test via ctypesgen")
    print("="*60)
    
    try:
        # Run all tests
        test_constants()
        test_basic_datetime_creation()
        test_datetime_type_functions()
        test_datetime_values()
        test_datetime_validation()
        test_datetime_utility_functions()
        test_datetime_operations()
        test_datetime_formatting()
        test_error_handling()
        
        print_separator("TEST COMPLETED SUCCESSFULLY")
        print("All available functions have been tested!")
        
    except Exception as e:
        print(f"\nERROR during testing: {e}")
        print("This might be due to:")
        print("1. Missing grass_datetime.dll file")
        print("2. DLL not in PATH or current directory")
        print("3. Incompatible DLL architecture (32-bit vs 64-bit)")
        print("4. Missing dependencies")
        sys.exit(1)

if __name__ == "__main__":
    main()
