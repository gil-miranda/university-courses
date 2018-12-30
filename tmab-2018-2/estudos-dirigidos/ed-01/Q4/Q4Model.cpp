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
 * Alunos: Gil Sales Miranda Neto, Caius Lao de Oliveira
 *
 * Q4
 **/
 #include <iostream>
 #include <math.h>
 #include "Q4Header.h"

 using namespace std;
 int global_A, global_B;

 int verificaPrimalidade(long long pp) {
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
 bool verificaPalindromo (long ppalin) {
   int i, j, k, d, digit [6];
   long inv_ppalin; // ppalim invertido;
   j = 10;
   k = 10000;
   bool palindromo;
   inv_ppalin = 0;
   if (ppalin < 100000) {
     k = 10000;
     d = 4;
   } else if(ppalin < 1000000) {
     k = 100000;
     d = 5;
   }
   for (i = 0; i <= d; i++) {
     digit[i] = (ppalin % j)/(j/10);
     inv_ppalin += digit[i]*k;
     j *= 10;
     k /= 10;
   }
   if (ppalin == inv_ppalin) {
     palindromo = true;
   } else {
     palindromo = false;
   }
   return palindromo;
 }
 bool verificaFatores(long palin) {
   int a, b, d;
   a = 100;
   b = 999;
   bool controle;
   controle = false;

   for (a; a < b; a++) {
     if (palin % a == 0) {
       d = palin/a;
       if (d/1000 == 0 && d/100 != 0) {
         //cout << palin << " = " << a << " x " << d << endl;
         controle = true;
         global_A = a;
         global_B = d;
       }
     }
   }
   return controle;
 }

 int somaMultiplos() {
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

int fibonacci() {
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

int fatorPrimo() {
  long long n; // Número a ser fatorado
  // Utilizaremos o fato de que todo divisor de n, menor que a raiz quadrada de n possui um divisor de n maior que a raiz quadrada de n correspondente.
  long long aux; // variavel auxiliar para calculos
  aux = floor(sqrt(n));
  int i; // variavel para controle do laço de repetição
  long long maiorFator = 1;

  cout << "Digite o numero a ser fatorado: ";
  cin >> n;

  for (i = 2; i <= aux; i++) {
    if (n % i == 0) {
      long long d = n/i;
      if (verificaPrimalidade(d)) {

      }
      if (verificaPrimalidade(i)) {

      }
    }
  }
  cout << "O maior fato primo: "<< maiorFator << endl;
  return 0;
}

int palindromos() {
  const int COTA_SUP = 998001;
  const int COTA_INF = 10000;
  long maiorPalindromo;
  int i;
  maiorPalindromo = 0;

  for (i = COTA_SUP; i >= COTA_INF; i--) {
    if(verificaPalindromo(i)) {
      if (i > maiorPalindromo) {
        if (verificaFatores(i)){
          maiorPalindromo = i;
        }
      }
    }
  }
  cout << "O maior palindromo: " << maiorPalindromo << " = " << global_A << " x " << global_B << endl;
  return 0;
}


int enessimoPrimo() {
  int i, j;
  i = 1;
  j = 2;

  while (i != 10001) {
    j++;
    if (verificaPrimalidade(j)) {
      i++;
    }
  }

  cout << j;
}
