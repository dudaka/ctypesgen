# Small Demonstration of Ctypesgen

This little demonstration was originally written by developer clach04 (when this
was still residing on code.google.com). This example shows how bindings for a
very simple c-library and associated header can be quickly generated using
Ctypesgen and accessed by a Python program.

Most of the instructions are included in the top of the various files, but a
summary is given here.

https://winlibs.com/

cl /EP /I. /U**GNUC** /D"**extension**=" /D"**const=const" /D"**asm**(x)=" /D"**asm(x)=" /D"cl /EP demolib.h

cl /EP demolib.h

## Steps to build a shared libary on Linux/Mac

```
cd demo

gcc -fPIC -shared -o demolib.so demolib.c

python ../run.py -o pydemolib.py -l demolib.so demolib.h

python demoapp.py

```

## Steps to build a shared library on Windows with MinGW

```bash
cd demo

C:\mingw64\bin\gcc -shared -o demolib.dll demolib.c
gcc -shared -o demolib.dll demolib.c

# power shell
objdump -p demolib.dll | Select-String -Pattern "trivial_add" -Context 2


python -c "import ctypes; dll = ctypes.CDLL('./demolib.dll'); print('DLL loaded successfully'); result = dll.trivial_add(5, 3); print(f'trivial_add(5, 3) = {result}')"

python ..\run.py -o pydemolib.py -l demolib.dll demolib.h

python demoapp.py
```

## Steps to build a shared library on Windows with MSVC

```bash

"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"

cd demo

cl /LD demolib.c /Fe:demolib_msvc.dll

dumpbin /exports demolib_msvc.dll


cl demoapp.c demolib_msvc.lib /Fe:demoapp_msvc.exe
demoapp_msvc.exe

python ../run.py --cpp "C:\opt\mingw64\bin\gcc -E"  -o pydemolib.py -l demolib_msvc.dll demolib.h

```

## Other commands

```bash

gcc -E -dD demolib.h

cl /nologo /EP /d1PP demolib.h

cl /nologo /EP /d1PP /Iinclude include/grass/datetime.h

C:\opt\mingw64\bin\gcc -E -dD -Iinclude include/grass/datetime.h

```

## Steps:

1. Compile the shared c-library

   `gcc -fPIC -shared -o demolib.so demolib.c`

   `"D:\mingw64\bin\gcc" -fPIC -shared -o demo\demolib.dll demo\demolib.c`

   `"D:\mingw64\bin\gcc" -o demo\demoapp demo\demoapp.c demo\demolib.c`

   `demo\demoapp.exe`

   `"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"`

   `cl /LD demolib.c /Fe:demolib_msvc.dll`

   `dumpbin /exports demolib_msvc.dll`

   `cl demoapp.c demolib_msvc.lib /Fe:demoapp_msvc.exe`

   `demoapp_msvc.exe`

2. (Re)Generate the bindings (or you can just try the bindings that were
   already generated and saved in this directory)

   `../run.py -o pydemolib.py -l demolib.so demolib.h`

   `python ../run.py --cpp "D:\mingw64\bin\gcc -E"  -o pydemolib.py -l demolib_msvc.dll demolib.h`

   `python ../run.py --cpp "C:\opt\mingw64\bin\gcc -E"  -o pydemolib.py -l demolib_msvc.dll demolib.h`

   `python ../run.py --cpp "C:\opt\mingw64\bin\gcc -E" --save-preprocessed-headers preprocessed-header.txt  -o pydemolib.py -l demolib_msvc.dll demolib.h`

   `python ../run.py --cpp "cl /E"  -o pydemolib.py -l demolib_msvc.dll demolib.h`

   `cl /nologo /EP /d1PP demolib.h`

   `cl /nologo /EP /d1PP /Iinclude include\grass\datetime.h`

   `C:\opt\mingw64\bin\gcc -E -dD -Iinclude include\grass\datetime.h`

3. Run the app that uses these newly generated bindings

   `./demoapp.py`

   The results of this execution should give

   ```
   a 1
   b 2
   result 3
   ```

4. You can also try executing the same code completely from a c-program

   - Compile test code:

     `gcc -o demoapp demoapp.c  demolib.c demolib.h`

   - Execute:

     `./demoapp`

   - Observe the same results as before:

     ```
     a 1
     b 2
     result 3
     ```

5. Other commands

```bash

```
