## Function libs
## @author: Gil Miranda
## @email: gilsmneto@gmail.com
## @github: mirandagil
## @page: www.gilmiranda.me
## @class of functions: METHODS FOR SOLVING DIFERENTIAL EQUATIONS
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
