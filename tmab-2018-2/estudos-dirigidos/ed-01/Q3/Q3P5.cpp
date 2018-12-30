/**
 * UFRJ   - Universidade Federal do Rio de Janeiro
 * DMA/IM - Departamento de Matematica Aplicada do Instituto de Matematica
 *
 * Top. Mat. Aplicada B - Programação & Banco de Dados
 * Parte I : Programação Estruturada em C
 *
 *          1a Lista de Exercícios: Projeto Euler I
 *
 * Data de entrega: 04 de setembro de 2018
 *
 * Prof. Milton Ramirez (mil...@labma.ufrj.br)
 *
 * Aluno: Gil Sales Miranda Neto
 *
 * Q3 - P5
 **/
 #include <iostream>
 #include <math.h>

  using namespace std;

  int verificaPrimalidade(long long pp) {
    // pp - recebe o LONG possível primo
    // return false -> não é primo
    // return true -> é primo
    long long j;
    long long aux = ceil(sqrt(pp));
    bool primalidade = true;
    for (j = 2; j <= aux; j++) {
      if (pp % j == 0) {
        primalidade = false;
      }
    }
    return primalidade;
  }

  int main() {
    int i, j, limit;
    i = 1;
    j = 2;

    cout << "Digite o limite: ";
    cin >> limit;

    while (i != limit) {
      j++;
      if (verificaPrimalidade(j)) {
        i++;
      }
    }

    cout << j;

    return 0;
  }
