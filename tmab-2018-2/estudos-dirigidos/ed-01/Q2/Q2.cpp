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
 * Q2
 **/
 #include <iostream>
 #include <math.h>

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

 int q1p1() {

   int sum_5 = ((5 + 2000)*(2000/5))/2;

   int sum_7 = ((7 + 1995)*(1995/7))/2;

   int sum_35 = ((35 + 1995)*(1995/35))/2;

   int sum = sum_5 + sum_7 - sum_35;

   cout << "A soma das PAs de 5 e 7 eh: " << sum << endl;
   return 0;
 }

  int q1p2() {
    int fibn1 = 1;
    int fibn2 = 2;
    int aux = 0;
    int i = 0;
    long sum = 1;
    int limit = 4000000; // Limite superior da sequencia
   cout << fibn1 << endl;
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
    cout << "A soma eh: " << sum << endl;
    return 0;
  }

  int q1p3() {
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

  int q1p4() {
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

  int q1p5() {
    int i, j;
    i = 1;
    j = 2;

    while (i != 10001) {
      j++;
      if (verificaPrimalidade(j)) {
        i++;
      }
    }

    cout << "O 10001-esimo primo: " << j << endl;
    return 0;
  }

  int main() {
   int menu;

   do {
     cout << endl << endl << "Escolha uma opcao: " << endl << "1 - Multiplos de 5 e 7" << endl << "2 - Fibonacci" << endl << "3 - Maior fator primo" << endl << "4 - Maior produto Palindromo" << endl << "5 - 10001esimo primo" << endl << "0 - Encerrar programa" << endl;
     cin >> menu;
     switch (menu) {
       case 1: q1p1(); break;
       case 2: q1p2(); break;
       case 3: q1p3(); break;
       case 4: q1p4(); break;
       case 5: q1p5(); break;
       default: cout << "Opcao invalida" << endl;
     }
   } while (menu != 0);

   return 0;
 }
