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
#ifndef ED_02_MATRIZ_H
#define ED_02_MATRIZ_H

#include <vector>
#include <iostream>

using namespace std;

class Matriz {

    public:
        //Construtores
        Matriz(unsigned int = 0, unsigned int = 0, int a = 0);
        Matriz(string matrixFile);
        Matriz(void);

        //Metódos de saída
        unsigned int getM();
        unsigned int getN();
        void printMatriz(void);

        //Metódos de entrada
        void setM(unsigned int m);
        void setN(unsigned int n);
        void setE(unsigned int m, unsigned int n, float a);


        //Metódos de operação
        void somaMatriz(Matriz);
        void produtoEscalar(float a);
        Matriz transposta();
        Matriz produtoMatricial(Matriz);

        //Declaração de propriedades
        vector<vector<float>> e; // elemento da matriz

    protected:
        unsigned int m;
        unsigned int n;
};
#endif //ED_02_MATRIZ_H
