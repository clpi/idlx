cmake_minimum_requirement(VERSION 3.1)

project(idlex LANGUAGES C CXX)

include(CTest)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED on)
set(CMAKE_CXX_EXTENSIONS off)

OPTION(LLVM_IDLEX "Support for LLVM dep graph" on)
OPTION(ENABLE_CFG "Enable CFG edges in the dep graph" on)
OPTION(NO_EXCEPTIONS, "Compille with -fno-exceptions" on)

if(NOT CMAKE_BUILD_TYPE)
    message(STATUS "Build type not set. Setting default")
    set(CMAKE_BUILD_TYPE, "RelWithDebInfo" CACHE STRING "" FORCE)
endif()

message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")
set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "RelWithDebInfo" "MinSizeRel" "Release")

if(LLVM_IDLEX)
    if(NOT ENABLE_CFG)
        message(STATUS "Enabling CFG edges due to LLVM_IDLEX")
    endif()

    set(ENABLE_CFG on)
    find_package(LLVM REQUIRED CONFIG)

    message(STATUS "Found LLVM ${LLVM_PACKAGE_VERSION}")
    message(STATUS "Using LLVM_CONFIG.cmake in: ${LLVM_DIR}")
    message(STATUS "Using LLVM binaries in: ${LLVM_TOOLS_BINARY_DIR}")
