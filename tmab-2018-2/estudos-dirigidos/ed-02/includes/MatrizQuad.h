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

#ifndef ED_02_MATRIZQUAD_H
#define ED_02_MATRIZQUAD_H

#include "Matriz.h"
#include "MatrizCol.h"
#include <vector>
#include <iostream>

using namespace std;

class MatrizQuad: public Matriz {
    public:
        MatrizQuad(unsigned int = 0);
        float trace();
        Matriz produtoMxV(vector<float>);
};


#endif //ED_02_MATRIZQUAD_H
