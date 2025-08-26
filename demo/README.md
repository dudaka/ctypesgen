Small Demonstration of Ctypesgen
================================

This little demonstration was originally written by developer clach04 (when this
was still residing on code.google.com).  This example shows how bindings for a
very simple c-library and associated header can be quickly generated using
Ctypesgen and accessed by a Python program.

Most of the instructions are included in the top of the various files, but a
summary is given here.


Steps:
----------
1. Compile the shared c-library

    `gcc -fPIC -shared -o demolib.so demolib.c`


    `"D:\mingw64\bin\gcc" -fPIC -shared -o demo\demolib.dll demo\demolib.c`


    `"D:\mingw64\bin\gcc" -o demo\demoapp demo\demoapp.c demo\demolib.c`

    `demo\demoapp.exe`


    `cl /LD demolib.c /Fe:demolib_msvc.dll`


    `dumpbin /exports demolib_msvc.dll`

    `cl demoapp.c demolib_msvc.lib /Fe:demoapp_msvc.exe`

    `demoapp_msvc.exe`



2. (Re)Generate the bindings (or you can just try the bindings that were
    already generated and saved in this directory)

    `../run.py -o pydemolib.py -l demolib.so demolib.h`

    `python ../run.py --cpp "D:\mingw64\bin\gcc -E"  -o pydemolib.py -l demolib.dll demolib.h`

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
