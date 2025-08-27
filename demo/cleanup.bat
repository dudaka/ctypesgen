@echo off
REM Cleanup script for ctypesgen demo directory
REM This script removes generated files from building and testing

echo Cleaning up demo directory...

REM Remove compiled libraries
if exist demolib.so (
    echo Removing demolib.so
    del /f demolib.so
)

if exist demolib.dll (
    echo Removing demolib.dll
    del /f demolib.dll
)

if exist demolib_msvc.dll (
    echo Removing demolib_msvc.dll
    del /f demolib_msvc.dll
)

if exist demolib_msvc.lib (
    echo Removing demolib_msvc.lib
    del /f demolib_msvc.lib
)

if exist demolib_msvc.exp (
    echo Removing demolib_msvc.exp
    del /f demolib_msvc.exp
)

REM Remove compiled executables
if exist demoapp (
    echo Removing demoapp (Unix executable)
    del /f demoapp
)

if exist demoapp.exe (
    echo Removing demoapp.exe
    del /f demoapp.exe
)

if exist demoapp_msvc.exe (
    echo Removing demoapp_msvc.exe
    del /f demoapp_msvc.exe
)

REM Remove generated Python bindings
if exist pydemolib.py (
    echo Removing pydemolib.py
    del /f pydemolib.py
)

if exist pydemolib_new.py (
    echo Removing pydemolib_new.py
    del /f pydemolib_new.py
)

REM Remove Python cache directories
if exist __pycache__ (
    echo Removing __pycache__ directory
    rmdir /s /q __pycache__
)

REM Remove any .pyc files
if exist *.pyc (
    echo Removing .pyc files
    del /f *.pyc
)

REM Remove object files
if exist *.o (
    echo Removing object files
    del /f *.o
)

if exist *.obj (
    echo Removing MSVC object files
    del /f *.obj
)

REM Remove temporary files
if exist *.tmp (
    echo Removing temporary files
    del /f *.tmp
)

REM Remove text files
if exist *.txt (
    echo Removing text files
    del /f *.txt
)

echo Cleanup complete!
pause
