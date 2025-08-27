/*
** Trivial ctypesgen demo library
**  from http://code.google.com/p/ctypesgen
*/

#ifdef _WIN32
    #ifdef DEMOLIB_DLL_EXPORT
        #define DEMOLIB_API __declspec(dllexport)
    #else
        #define DEMOLIB_API __declspec(dllimport)
    #endif
#else
    #define DEMOLIB_API
#endif

#define ABC 123

DEMOLIB_API int trivial_add(int a, int b);
