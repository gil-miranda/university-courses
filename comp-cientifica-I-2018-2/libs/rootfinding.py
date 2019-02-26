## Function libs
## @author: Gil Miranda
## @email: gilsmneto@gmail.com
## @github: mirandagil
## @page: www.gilmiranda.me
## @class of functions: ROOTFINDING METHODS
## @last update: 26/02/2019

### - BISSECTION - ###

    ### - BASIC BISSECTION STEPPER - ###
def bissection_step(f, a, b):
    z = (a+b)/2
    if(f(z) == 0):
        return (z,z)
    elif (f(a)*f(z) < 0):
        return (a,z)
    elif (f(z)*f(b) < 0):
        return (z,b)

    ### - BASIC RECURSIVE BISSECTION - ###
    ### - dependency: bissection_step from rootfinding - ###
def bissection(f,a,b,tol=1e-6,count=0,retsteps=False):
    if f(a)*f(b) > 0:
         raise ValueError('Non-opposite signs for bissection')
    if f(a) == 0:
        if (retsteps):
            return (a,count)
        else:
            return a
    elif f(b) == 0:
        if (retsteps):
            return (b,count)
        else:
            return b
    else:
        if (abs(b-a) <= tol):
            if (retsteps):
                return ((b+a)/2,count)
            else:
                return (b+a)/2
        else:
            a, b = bissection_step(f, a, b)
            count += 1
            return bissecao(f, a, b, tol, count, retsteps)


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
