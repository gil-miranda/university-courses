//
// Created by zoso on 01/10/18.
//

#include "../includes/MatrizDiag.h"

#include <vector>
#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

MatrizDiag::MatrizDiag(unsigned int m, unsigned int n): Matriz(1,n)
{
    this->setM(n);
}

void MatrizDiag::printMatriz()
{
    for(int i = 0; i < this->m; i++){
        for(int j = 0; j < this->n; j++)
        {
            if(i == j) {
                cout << this->e[0][j] << "\t";
            } else {
                cout << "0\t";
            }

        }
        cout << endl;
    }
    cout << endl;
}