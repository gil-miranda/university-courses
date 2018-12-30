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
#include "../includes/Matriz.h"

#include <vector>
#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

Matriz::Matriz(unsigned int m, unsigned int n, int a)
{
    // Construtor da Matriz por parametro de linha e coluna

    this->e.resize(m);
       for(int k = 0; k < m; k++) this->e[k].resize(n);

    // Loop para popular a matriz com a;
    for(int i = 0; i < m; i++)
    {
        for(int j = 0; j < n; j++) this->e[i][j] = 3;
    }
    // Setar as variaveis encapsuladas;
    this->setM(m);
    this->setN(n);
}

Matriz::Matriz(std::string matrixFile)
{
    // Construtor da Matriz por parametro em arquivo
    std::ifstream arq_in(matrixFile.c_str());
}

Matriz::Matriz() {

}

unsigned int Matriz::getM() // Metódo que retorna o número de linhas da matriz
{
    return this->m;
}

unsigned int Matriz::getN() // Metódo de retorna o número de colunas da matriz
{
    return this->n;
}

void Matriz::setM(unsigned int m) // Metódo para alterar o número de linhas
{
    this->m = m;
}

void Matriz::setN(unsigned int n)  // Metódo para alterar o número de colunas
{
    this->n = n;
}

void Matriz::printMatriz() // Metódo para imprimir a matriz no terminal
{
    for(int i = 0; i < this->m; i++){
        for(int j = 0; j < this->n; j++)
        {
            cout << scientific;
            cout << this->e[i][j] << "\t";
        }
        cout << endl;
    }
    cout << endl;
}

void Matriz::setE(unsigned int m, unsigned int n, float a) // Metódo para alterar o elemento na linha M coluna N
{
    this->e[m][n] = a;
}

void Matriz::somaMatriz(Matriz B) // Operação de soma entre matrizes, altera a matriz atual
{
    if(this->m == B.getM() && this->n == B.getN())
    {
        for(int i = 0; i < this->m; i++)
        {
            for(int j = 0; j < this->n; j++) this->e[i][j] += B.e[i][j];
        }
    }
}

void Matriz::produtoEscalar(float a) // Operação de multiplicação pelo escalar a
{
    for(int i = 0; i < this->m; i++)
    {
        for(int j = 0; j < this->n; j++) this->e[i][j] *= a;
    }
}

Matriz Matriz::transposta() // Retorna a matriz A transposta A^t
{
    Matriz At(this->n,this->m);
    for(int i = 0; i < this->n; i++)
    {
        for(int j = 0; j < this->m; j++) At.e[i][j] = this->e[j][i];
    }
    return At;
}

Matriz Matriz::produtoMatricial(Matriz B) // Retorna a Matriz C = AB
{
    Matriz C(this->m, B.getN());
    if(this->n != B.getM())
    {
        cout << "ERRO: Operação não definida para estas matrizes";
        return 0;
    }
    for(int c_m = 0; c_m < this->m; c_m++) // loop para percorrer as linhas da matriz produto C
    {
        for(int c_n = 0; c_n < B.getN(); c_n++) // loop para percorrer as colunas da matriz produto C
        {
            for(int i = 0; i < B.getM(); i++)  C.e[c_m][c_n] += this->e[c_m][i] * B.e[i][c_n];

        }
    }
    return C;
}