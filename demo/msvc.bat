@echo off
REM Compile a shared library for Windows using MSVC
REM Create a demo application for the shared library
REM Create a python bindings for the shared library with ctypesgen

echo Compile a shared library for Windows using MSVC...

cl /LD demolib.c /Fe:demolib_msvc.dll

echo Create a demo application for the shared library...

cl demoapp.c demolib_msvc.lib /Fe:demoapp_msvc.exe

echo Run the demo application...

demoapp_msvc.exe

echo Create a python bindings for the shared library with ctypesgen (gcc as the preprocessor)...

@REM python ../run.py --cpp "C:\opt\mingw64\bin\gcc -E"  -o pydemolib.py -l demolib_msvc.dll demolib.h

python ../run.py --cpp "cl /E"  -o pydemolib.py -l demolib_msvc.dll demolib.h

echo Run a the demo for python bindings...

python demoapp.py

echo Done!
