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
 * Q1 - P3
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
  long long n = 3852914583882; // Número a ser fatorado
  // Utilizaremos o fato de que todo divisor de n, menor que a raiz quadrada de n possui um divisor de n maior que a raiz quadrada de n correspondente.
  long long aux; // variavel auxiliar para calculos
  aux = floor(sqrt(n));
  int i; // variavel para controle do laço de repetição
  long long maiorFator = 1;

  for (i = 2; i <= aux; i++) {
    if (n % i == 0) {
      long long d = n/i;
      if (verificaPrimalidade(d)) {
        if (d > maiorFator) {
          maiorFator = d;
        }
      }
      if (verificaPrimalidade(i)) {
        if (i > maiorFator) {
          maiorFator = i;
        }
      }
    }
  }
  cout << "O maior fato primo: "<< maiorFator << endl;
  return 0;
}
