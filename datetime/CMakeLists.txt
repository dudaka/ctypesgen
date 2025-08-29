cmake_minimum_required(VERSION 3.15)
project(GrassDateTime VERSION 1.0.0 LANGUAGES C)

# Set C standard
set(CMAKE_C_STANDARD 99)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Add compiler flags for debug/release
if(MSVC)
    set(CMAKE_C_FLAGS_DEBUG "/Od /Zi /MDd")
    set(CMAKE_C_FLAGS_RELEASE "/O2 /DNDEBUG /MD")
else()
    set(CMAKE_C_FLAGS_DEBUG "-g -O0 -Wall -Wextra")
    set(CMAKE_C_FLAGS_RELEASE "-O3 -DNDEBUG")
endif()

# Set default build type to Release if not specified
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build." FORCE)
    set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "MinSizeRel" "RelWithDebInfo")
endif()

# Include directories
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

# Collect all source files from lib/datetime
file(GLOB DATETIME_SOURCES "lib/datetime/*.c")

# Build shared library only
add_library(grass_datetime SHARED ${DATETIME_SOURCES})
target_compile_definitions(grass_datetime PRIVATE GRASS_DATETIME_DLL_EXPORT)

# Set output properties
set_target_properties(grass_datetime PROPERTIES
    OUTPUT_NAME "grass_datetime"
    PREFIX ""
    VERSION 1.0.0
    SOVERSION 1
)

# Install shared library
install(TARGETS grass_datetime
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

# Install headers
install(DIRECTORY include/grass
    DESTINATION include
    FILES_MATCHING PATTERN "*.h"
)

# Display build information
message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")
message(STATUS "C compiler: ${CMAKE_C_COMPILER}")
message(STATUS "Output directory: ${CMAKE_CURRENT_BINARY_DIR}")
