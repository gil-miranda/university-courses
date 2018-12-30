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
 * Q1 - P1
 **/

#include <iostream>

using namespace std;

int main() {

  // É fácil ver que todos os múltiplos de 5 formam uma PA de razão 5 e último termo 2000
  // Então utilizaremos a fórmula da soma da PA para chegar a soma dos múltiplos de 5
  // (( a_1 + a_n ) * ( n ) )/2 - a_1 primeiro termo - a_n último termo - n quantidade de termos
  int sum_5 = ((5 + 2000)*(2000/5))/2;

  // Utilizando o mesmo raciocinio chegamos aos múltiplos de 7 mas agora o último múltiplo é 1995
  int sum_7 = ((7 + 1995)*(1995/7))/2;

  // Na soma de cada uma das PAs temos somados os termos do tipo n*35, que são múltiplos consecutivos de 5 e 7
  // Somaremos uma PA de razão 35 e subtrairemos da soma total, assim teremos somados estes termos apenas uma vez
  int sum_35 = ((35 + 1995)*(1995/35))/2;

  // int sum receberá o valor total das somas.
  int sum = sum_5 + sum_7 - sum_35;

  cout << "A soma das PAs de 5 e 7 eh: " << sum << endl;
  return 0;
}
