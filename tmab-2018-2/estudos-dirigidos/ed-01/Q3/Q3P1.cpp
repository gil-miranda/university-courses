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
 * Q3 - P1
 **/

#include <iostream>

using namespace std;

int main() {

  // É fácil ver que todos os múltiplos de 5 formam uma PA de razão 5 e último termo 2000
  // Então utilizaremos a fórmula da soma da PA para chegar a soma dos múltiplos de 5
  // (( a_1 + a_n ) * ( n ) )/2 - a_1 primeiro termo - a_n último termo - n quantidade de termos
  int sum[4];
  int n[4], d; // a e b recebem os numeros a serem encontrados multiplo, c e o limite. d recebe o mmc de a e b;
  int aux[4]; // variavel auxiliar para calculos
  int soma, i;
  cout << "Digite o primeiro numero: " << endl;
  cin >> n[0];
  cout << "Digite o segundo numero: " << endl;
  cin >> n[1];
  cout << "Digite o limite: " << endl;
  cin >> n[3];

  n[3] -= 1; // excluindo o limite do conjunto solução

  n[2] = n[0] * n[1]; // calculando um multiplo comum

  for (i = 0; i < 4; i++) {
    aux[i] = n[3] % n[i];
    aux[i] = n[3] - aux[i];
  }
  for (i = 0; i < 3; i++) {
    sum[i] = ((n[i] + aux[i])*(aux[i]/n[i]))/2;
  }
  if (n[2] <= n[3]) {
    soma = sum[0] + sum[1] - sum[2];
  } else {
    soma = sum[0] + sum[1];
  }

  cout << "A soma das PAs de 5 e 7 eh: " << soma << endl;
  return 0;
}
