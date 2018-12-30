cmake_minimum_required(VERSION 3.12)
project(ed_02)

set(CMAKE_CXX_STANDARD 14)

add_executable(ed_02 main.cpp src/Matriz.cpp includes/Matriz.h src/MatrizQuad.cpp includes/MatrizQuad.h src/MatrizTSup.cpp includes/MatrizTSup.h src/MatrizDiag.cpp includes/MatrizDiag.h src/MatrizCol.cpp includes/MatrizCol.h src/MatrizLin.cpp includes/MatrizLin.h)