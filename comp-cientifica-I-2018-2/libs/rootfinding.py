## Function libs
## @author: Gil Miranda
## @email: gilsmneto@gmail.com
## @github: mirandagil
## @page: www.gilmiranda.me
## @class of functions: ROOTFINDING METHODS
## @last update: 10/09/2018
## -- Computação Cientifica 2018.2 @ UFRJ --

### - BISSECTION - ###

    ### - BASIC BISSECTION STEPPER - ###
def bissection_step(f, a, b):
    if (f(a)*f(b)) > 0:
        print('ERRO! O dado intervalo [' + str(a)+','+str(b)+'] não contém uma raíz.')
        return (a,b)
    else:
        m = (a+b)/2
        if(f(m) == 0):
            return (m,m)
        elif (f(a)*f(m) < 0):
            return (a,m)
        elif (f(m)*f(b) < 0):
            return (m,b)

    ### - BASIC RECURSIVE BISSECTION - ###
    ### - dependency: bissection_step from rootfinding - ###
def bissection(f,a,b,tol=1e-6,count=0,retsteps=False):
    if (abs(b-a) <= tol):
        if (f((b+a)/2)) < f(b) and f((b+a)/2) < f(a):
            if (retsteps):
                return ((b+a)/2,count)
            else:
                return (b+a)/2
        elif (f(b)<f(a)):
            if (retsteps):
                return (b,count)
            else:
                return b
        else:
            if (retsteps):
                return (a,count)
            else:
                return a
    else:
        a, b = bissection_step(f, a, b)
        count += 1
        return bissection(f, a, b, tol, count, retsteps)


# ------------------------------------------------------------------------------------ #


### NEWTON-RAPHSON ###

def newton(f, df, x, prec=1e-8, tol=1e-8, maxiter=100):
    if maxiter == 0: return none
    h = f(x)/df(x) ## passo de newton
    x_n = x - h ## gerando o próximo x
    if abs(h) < prec or abs(f(x)) < tol: return x_n ## testando se já estamos suficientemente próximos da raíz
    else: return newton(f,df, x_n, prec, tol, maxiter-1) ## chamando a função recursivamente para gerar um novo ponto

# ------------------------------------------------------------------------------------ #

### MÉTODO DA SECANTE  ###

def newton_sec(f, x_1, x_2, tol=1e-8, maxiter=100):
    x_n = (x_1*f(x_2) - x_2*f(x_1))/(f(x_2) - f(x_1))
    if abs(x_n - x_2) < tol: return x_n
    if maxiter == 0: return x_n
    return newton_sec(f,x_2,x_n, tol, maxiter-1)
