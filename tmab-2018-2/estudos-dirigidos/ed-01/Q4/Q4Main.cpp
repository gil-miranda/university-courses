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
#include "Q4Header.h"
#include "Q4Model.cpp"

using namespace std;

void Menu() {
  int menu;

  do {
    cout << endl << endl << "Escolha uma opcao: " << endl << "1 - Multiplos de 5 e 7" << endl << "2 - Fibonacci" << endl << "3 - Maior fator primo" << endl << "4 - Maior produto Palindromo" << endl << "5 - 10001esimo primo" << endl << "0 - Encerrar programa" << endl;
    cin >> menu;
    switch (menu) {
      case 1: somaMultiplos(); break;
      case 2: fibonacci(); break;
      case 3: fatorPrimo(); break;
      case 4: palindromos(); break;
      case 5: enessimoPrimo(); break;
      default: cout << "Opcao invalida" << endl;
    }
  } while (menu != 0);
}

int main() {
  Menu();
  return 0;
}
