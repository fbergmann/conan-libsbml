PROJECT(LibSBMLPackageTest)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

ADD_EXECUTABLE(libsbml_info libsbml_info.cpp)
TARGET_LINK_LIBRARIES(libsbml_info ${CONAN_LIBS})
ADD_EXECUTABLE(createExampleSBML createExampleSBML.cpp)
TARGET_LINK_LIBRARIES(createExampleSBML ${CONAN_LIBS})
ADD_EXECUTABLE(printSBML printSBML.cpp)
TARGET_LINK_LIBRARIES(printSBML ${CONAN_LIBS})
