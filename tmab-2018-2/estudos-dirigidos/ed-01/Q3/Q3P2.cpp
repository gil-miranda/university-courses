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
 * Q3 - P2
 **/

#include <iostream>

using namespace std;

int main() {
  int fibn1 = 1;
  int fibn2 = 2;
  int aux = 0;
  int i = 0;
  long sum = 1;
  int limit; // Limite superior da sequencia

  cout << "Digite o valor maximo da sequencia: ";
  cin >> limit;
  while (i == 0) {
    aux = fibn1 + fibn2;

    if (fibn2 % 2 != 0){
      sum += fibn2;
    }

    if(aux >= limit){
      i = 1;
    } else {
      fibn1 = fibn2;
      fibn2 = aux;
    }
  }
  cout << "A soma eh: " << sum;
  return 0;
}
