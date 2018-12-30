## Function libs
## @author: Gil Miranda
## @email: gilsmneto@gmail.com
## @github: mirandagil
## @page: www.gilmiranda.me
## @class of functions: ALL FUNCTIONS
## @last update: 22/10/2018
## -- Computação Cientifica 2018.2 @ UFRJ --


### - EULER METHODS FOR ODE - ###

    ### - FORWARD EULER - ###
def forward_euler(F, t0, y0, ts):
    """Calcula uma solução aproximada da equação y' = F(t,y) pelo método de Euler, nos pontos [ts]."""
    ys = [y0]
    t = t0
    for tnext in ts:
        ynext = ys[-1] + F(t, ys[-1])*(tnext-t)
        ys.append(ynext)
        t = tnext
    return ys

    ### - FORWARD EULER WITH NUMBER OF POINTS - ###
def feuler_npts(F, I, y0, npts, retpts=False):
    if retpts:
        ts, h = np.linspace(I[0], I[-1], num = npts, retstep = True)
    else:
        ts = np.linspace(I[0], I[-1], num = npts)
    ys = forward_euler(F, I[0], y0, ts[1:])
    if retpts:
        return ts, ys
    else:
        return ys

    ### - FORWARD EULER WITH SIZE OF STEPS - ###
def eulerH(F, I, y0, h, retpts=False):
    npts = int(((I[-1]-I[0])/h)+1)
    ts = np.linspace(I[0], I[-1], npts)
    ys = forward_euler(F, I[0], y0, ts[1:])
    if retpts:
        return ts, ys
    else:
        return ys


        ### - BACKWARD EULER - ###
def implicit_euler(solveF, t0, y0, ts):
    """Calcula uma solução aproximada da equação y' = F(t,y) pelo método de Euler implícito, nos pontos [ts].
    A função solveF(t,y,h) dá a solução de dy = F(t,y+dy)*h."""
    ys = [y0]
    t = t0
    for tnext in ts:
        y = ys[-1]
        ynext = y + solveF(t,y,(tnext-t))
        ys.append(ynext)
        t = tnext
    return ys[:-1]

        ### - GENERATE SOLVE F - ###
        ### - dependency: bissection from rootfinding - ###
def generate_solveF(F):
    def solveF(t, ycurr, h):
        def eqynext(ynext):
            return ynext - ycurr - F(t, ynext) * h
        return bissection(eqynext, ycurr, ycurr+2*F(t,ycurr)*h)
    return solveF

# ----------------------------------------------------------------------------#

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

    ### - BASIC ITERATIVE BISSECTION - ###
def bissecaoIterativa(f, a, b, tol=1e-6):
    while (b-a) > tol:
        a, b = bissecaoStep(f, a, b)
    return (a+b)/2

    ### - BISSECTION WITH TUPLE OF POINTS - ###
def rangeSize(I):
    return I[-1] - I[0]

def bissecaoTupleStep(f, I):
    a, b = I
    z = (a+b)/2

    if f(z) == 0:
        return (z,z)
    elif f(a)*f(z) < 0:
        return (a,z)
    else:
        return (z,b)

def bissecaoTupleIterativa(f, I, tol=1e-6):
    """Bissection algorithm for function f on the interval [a,b], stopping when the width becomes less than `tol`."""
    while rangeSize(I) > tol:
        I = bissecaoTupleStep(f, I)
    return I

def bissecaoTupleRecursiva(f, I, tol=1e-6):
    if rangeSize(I) < tol:
        return I
    else:
        I = bissecaoTupleStep(f, I)
        return bissecaoTupleRecursiva(f, I)

# ----------------------------------------------------------------------------#

### - NEWTON'S METHOD FOR ODEs - ###

def newtonStop(f,df,x, prec=1e-8, tol=1e-8, maxiter=100, iterr = 0):
    if maxiter == iterr:
        return None
    dx = f(x)/df(x)
    newx = x - dx

    if abs(dx) < prec or f(x) < tol:
        return newx, iterr
    else:
        return newton(f,df,newx, prec, tol, iterr = iterr+1)

        ### - NEWTON RETORNANDO A RAIZ - ###
def newtonRootOnly(f,df,x, prec=1e-8, maxiter=100, iterr = 0):
    if maxiter == iterr:
        return None
    dx = f(x)/df(x)
    newx = x - dx
    if abs(dx) < prec:
        return newx, iterr
    else:
        return newton(f,df,newx, prec,iterr = iterr+1)


        ### --- NEWTON RETORNANDO LISTA DE PONTOS --- ###
def newton(f,df,x, prec=1e-8, maxiter=100, iterr = 0, lst = [], reti = False):
    if maxiter == iterr:
        return None
    dx = f(x)/df(x)
    newx = x - dx
    xs = lst[:]
    xs.append(x)
    if abs(dx) < prec:
        if reti:
            return xs, iterr
        else:
            return xs
    else:
        return newton(f,df,newx, prec,iterr = iterr+1, lst = xs)

### MÉTODO DA SECANTE  ###

def newton_sec(f, x_1, x_2, tol=1e-8, maxiter=100):
    x_n = (x_1*f(x_2) - x_2*f(x_1))/(f(x_2) - f(x_1))
    if abs(x_n - x_2) < tol: return x_n
    if maxiter == 0: return x_n
    return newton_sec(f,x_2,x_n, tol, maxiter-1)

# ----------------------------------------------------------------------------#

### - POLYNOMIAL ROOTFINDING AND DERIVATIVE METHODS - ###
    ### - ROOT FINDER FOR FIRST DEGREE POLYNOMIAL - ###
def rootFinder1(f):
    b = f(0)
    a = f(1) - f(0)
    return -b/a

    ### - NUMERICAL POINT DERIVATIVE OF POLYNOMIALS - ###
def derivate_pol(x, coefs):
    ## enumerate() fará com que cada coeficiente fique associado a seu respectivo grau em uma tupla (x,y)
    pol = list(enumerate(coefs))
    lst = [] ## lista a receber os coeficientes já derivados e aplicados ao ponto x
    for i in pol:
        n = ((i[1])*(i[0]))*(x**(i[0]-1)) ## (a_n*n)*(x^(n-1))
        lst.append(n)
    dyDx = sum(lst)
    return dDx

# ----------------------------WORK IN PROGRESS------------------------------------#

### - PROGRESSION SUMS - ###

    ### - ARITHMETIC PROGRESSION SUM - ###
def toolkitPA(a_1 = 0, a_n = 0, r = 0, n = 0, retsum = True, retr = False, retn = False, reta1 = False, retan = False):
    ret = ()
    if retsum:
        ret.append((((a_1 + a_n) * n) / 2))
    if retr && n != 0:
        ret.append(a_n/n)
    if retn && r != 0:
        ret.append(a_n/r)
    return ret

def toolkitPG(a_1, a_n):
