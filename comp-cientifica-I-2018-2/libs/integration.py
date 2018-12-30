## Function libs
## @author: Gil Miranda
## @email: gilsmneto@gmail.com
## @github: mirandagil
## @page: www.gilmiranda.me
## @class of functions: METHODS FOR INTEGRATION
## @last update: 22/10/2018
## -- Computação Cientifica 2018.2 @ UFRJ --

### - TRAPEZOIDAL - ###

    ### - BASIC TRAPEZOIDAL STEPPER - ###
    ### - dependency: bissection from rootfinding - ###
def trapezoidal_step(F,t,h,ycurr):
    tnext = t+h
    def aux(dy):
        return (F(t,ycurr)+F(tnext,ycurr+dy))*h/2 - dy
    valor = bissecao(aux,0,2*F(t,ycurr))
    return valor

    ### - BASIC TRAPEZOIDAL STEPPER - ###
    ### - dependency: trapezoidal_step from integration - ###
def trapezoidal(F,t0,y0,ts):
    ys = [y0]
    ycurr = y0
    tcurr = t0
    for tnext in ts[1:]:
        ynext = ycurr + trapezoidal_step(F,tcurr,tnext-tcurr,ycurr)
        ycurr = ynext
        tcurr = tnext
        ys.append(ynext)
    return ys


## Integração de Polinômios
## coefs: lista de coeficientes do polinômio de grau n = len(coefs)-1
##        onde coefs[0] representa o termo x^0 e coefs[-1] o termo x^n
## a,b: limites de integração
def pol_integrator(coefs, a, b):
    term = [i*((b**(j+1) - a**(j+1))/(j+1)) for j,i in enumerate(coefs)]
    return sum(term)
