## Function libs
## @author: Gil Miranda
## @email: gilsmneto@gmail.com
## @github: mirandagil
## @page: www.gilmiranda.me
## @class of functions: DERIVATING METHODS
## @last update: 29/10/2018
## -- Computação Cientifica 2018.2 @ UFRJ --

## Derivação de Polinômios
## coefs: lista de coeficientes do polinômio de grau n = len(coefs)-1
##        onde coefs[0] representa o termo x^0 e coefs[-1] o termo x^n
## x: ponto a ser derivado
def pol_derivator(coefs, x):
    terms = [i*j * x**(j-1) for j,i in enumerate(coefs)]
    return sum(terms)
