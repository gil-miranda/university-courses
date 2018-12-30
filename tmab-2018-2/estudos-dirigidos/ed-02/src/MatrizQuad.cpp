/**

 * UFRJ   - Universidade Federal do Rio de Janeiro

 * DMA/IM - Departamento de Matemática Aplicada do Inst. Matemática

 *

 * MAB353: TMAB - Programação e Banco de Dados - 2018.02

 *         Prof. Milton Ramirez

 *

 * Estudo Dirigido 02: Hierarquia de Classes em C++

 *

 * Alunos: Gil Miranda e Caius

 *

 **/

#include "../includes/MatrizQuad.h"

#include <vector>
#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

MatrizQuad::MatrizQuad(unsigned int m): Matriz(m,m)
{

}

float MatrizQuad::trace()
{
    float trace;
    for (int i = 0; i < this->getM(); i++)
    {
        for (int j = 0; j < this->getN(); j++)
        {
            if (i == j)
            {
                trace += this->e[i][j];
            }
        }
    }
    return trace;
}

Matriz MatrizQuad::produtoMxV(vector<float> B) //
{
    Matriz C(this->m,1);
    if(this->n != B.size())
    {
        cout << "ERRO: Operação não definida para estas matrizes";
        return 0;
    }

    for(int c_m = 0; c_m < this->m; c_m++) // loop para percorrer as linhas da matriz produto C
    {
        for(int c_n = 0; c_n < B.size(); c_n++) // loop para percorrer as colunas da matriz produto C
        {
            for(int i = 0; i < B.size(); i++){
                C.setE(c_m,1,C.e[c_m][1] + this->e[c_m][i] * B[i]);
            }
        }
    }
    return C;
}