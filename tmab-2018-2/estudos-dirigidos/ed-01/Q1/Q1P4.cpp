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
 * Q1 - P4
 **/
 #include <iostream>

  using namespace std;
  int global_A, global_B;

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
   /* O loop cria a seguinte estrutura:
    *   digit[0] = ppalin % 10;
    *   digit[1] = floor((ppalin % 100)/10);
    *   digit[2] = floor((ppalin % 1000)/100);
    *   digit[3] = floor((ppalin % 10000)/1000);
    *   digit[4] = floor((ppalin % 100000)/10000);
    *   inv_ppalin = 10000*digit[0] + 1000*digit[1] + 100*digit[2] + 10*digit[3] + digit[4];
    */
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

 // O menor inteiro de 3 digitos é dado pelo número: 100
 // O maior número de 3 digitos é dado pelo número: 999
 // Então o maior e menor produto de 2 numeros de 3 digitos é: 999² = 998001 e 100² = 10000
 // É dentro desse 'range' que iremos procurar números palimdromos.

int main() {
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
