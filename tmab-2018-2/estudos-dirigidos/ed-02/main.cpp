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

#include <iostream>
#include "includes/Matriz.h"
#include "includes/MatrizQuad.h"
#include "includes/MatrizDiag.h"
#include "includes/MatrizLin.h"
#include "includes/MatrizCol.h"

using namespace std;

int main() {
    unsigned int m, n, a, b;
   /* cout << "Bem vindo a calculadora de matrizes do Gil" << endl;
    cout << "Digite a quantidade de linhas da matriz: ";
    cin >> m;
    cout << "Digite a quantidade de colunas da matriz: ";
    cin >> n;*/

   /* cout << "Digite a quantidade de linhas da matriz: ";
    cin >> a;
    cout << "Digite a quantidade de colunas da matriz: ";
    cin >> b;*/

//Matriz A(1,m);
    //MatrizDiag B(m,n);
    /*B.printMatriz();
    B.setE(0,2,6);
    A.somaMatriz(B);
    A.printMatriz();

    A.printMatriz();*/

    //A.printMatriz();

  //  A.setE(0,1,53);
    //A.setE(1,0,499);
  //  Matriz C = A.transposta();
    //A.produtoEscalar(15);
//A.printMatriz();
    //cout << B.getN();
    //B.printMatriz();
  //  C.printMatriz();
   // Matriz D = A.produtoMatricial(B);
   // D.printMatriz();
   //MatrizLin F(n);
   //MatrizCol G(m);
   MatrizQuad A(3);
   vector<float> B;
   B.push_back(5);
   B.push_back(8);
   B.push_back(9);
   A.printMatriz();
   //cout << B.size();
   Matriz C = A.produtoMxV(B);
  cout << C.e[0][1];
  C.printMatriz();
   //G.printMatriz();
    return 0;
}