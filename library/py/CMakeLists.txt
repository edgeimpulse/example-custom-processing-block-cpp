cmake_minimum_required(VERSION 3.15...3.27)

project(eicpp)

find_package(Python3 REQUIRED)
find_package(Python 3.9 COMPONENTS Interpreter Development.Module REQUIRED)
find_package(pybind11 REQUIRED HINTS "${Python3_SITELIB}")

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

if (NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build." FORCE)
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "MinSizeRel" "RelWithDebInfo")
endif()

include_directories(../cpp)

set_property(TARGET PROPERTY POSITION_INDEPENDENT_CODE ON)

pybind11_add_module(eicpp eicpp.cpp)
