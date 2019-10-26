### My big library of scientific computing methods
### Gil Miranda

# ---------------------------------------------------------------------------- #

##### Vectorized forward euler
### Input:  F -> Differential equation;
###         y0 -> list or scalar for initial condition;
###         ts -> list of points in time to evaluate the equation;
###         p -> list or scalar for parameters for F, default is set to 0 if F has no extra parameters;
### Output: ys -> numpy array with all solutions for each step t, ys is a Matrix
##### Gil Miranda - last revision 23/10/2019
def mylib_feuler(F, ts, y0, p = 0):
    ys = [y0]
    h = ts[1]-ts[0]
    for tnext in ts[1:]:
        ynext = ys[-1] + F(tnext, ys[-1], p)*h
        ys.append(ynext)
        t = tnext
    return np.array(ys)

# ---------------------------------------------------------------------------- #

##### Vectorized backward euler
### Input:  F -> Differential equation;
###         y0 -> list or scalar for initial condition;
###         ts -> list of points in time to evaluate the equation;
###         p -> list or scalar for parameters for F, default is set to 0 if F has no extra parameters;
### Output: ys -> numpy array with all solutions for each step t, ys is a Matrix
##### Gil Miranda - last revision 26/10/2019
def mylib_beuler(F, ts, y0, p = 0):
    ys = [y0]
    t = ts[0]
    h = ts[1]-ts[0]
    for tnext in ts[1:]:
        y = ys[-1]
        ynext = y + mylib_beuler_step(F,t,y,h)
        ys.append(ynext)
        t = tnext
    return np.array(ys)

def mylib_beuler_step(F, t, y, h, tol = 1e-6):
    tnext = t+h
    fw_step = F(t, y) * h
    def f(step): return step - F(tnext, y+step)*h
    step = bissection(f, 0, 2*fw_step, tol)
    return step

# ---------------------------------------------------------------------------- #

##### Bissection
### Input:  f -> Equation for the root to be found;
###         a -> min of the interval;
###         b -> max of the interval;
###         tol -> tolerance;
### Output: z -> f(z) < tol (root)
##### Gil Miranda - last revision 26/10/2019
def bissection(f, a, b, tol = 1e-6):
    z = a/2+b/2 # (a+b)/2 without errors if they are big
    if b - a < tol:
        return z
    if f(a)*f(z) < 0:
        return bissection(f, a, z, tol)
    else:
        return bissection(f, z, b, tol)

# ---------------------------------------------------------------------------- #

##### Vectorized 4th Order Runge Kutta
### Input:  F -> Differential equation;
###         y0 -> list or scalar for initial condition;
###         ts -> list of points on time to evaluate the equation;
###         p -> list or scalar for parameters for F, default is set to 0 if F has no extra parameters;
### Output: ys -> numpy array with all solutions for each step t, ys is a Matrix
##### Gil Miranda - last revision 26/09/2019
def rk_4(F, y0, ts, p = 0):
    ys = [y0]
    t = ts[0]
    h = ts[1] - ts[0]
    for tnext in ts:
        k1 = h*F(t, ys[-1], p)
        k2 = h*F(t + h/2, ys[-1] + k1/2, p)
        k3 = h*F(t + h/2, ys[-1] + k2/2, p)
        k4 = h*F(t + h, ys[-1] + k3)
        ynext = ys[-1] + (k1/6+k2/3+k3/3+k4/6)
        ys.append(ynext)
        t = tnext
    return np.array(ys[:-1])

# ---------------------------------------------------------------------------- #

##### Vectorized 2nd/3rd Order Runge Kutta (uses 3rd order to verify 2nd order solution)
### Input:  F -> Differential equation;
###         y0 -> list or scalar for initial condition;
###         ts -> list of points on time to evaluate the equation;
###         p -> list or scalar for parameters for F, default is set to 0 if F has no extra parameters;
### Output: ys -> numpy array with all solutions for each step t, ys is a Matrix
##### Gil Miranda - last revision 26/09/2019
def mylib_rk23(F, ts, y0, p = 0):
    ys = [y0]
    ys_til = [y0]
    t = ts[0]
    h = ts[1] - ts[0]
    for tnext in ts:
        k1 = F(t, ys[-1], p)
        k2 = F(t + h/2, ys[-1] + k1/2, p)
        k3 = F(t + 3*h/4, ys[-1] + 3*h*k2/4, p)
        k4 = F(t + h, ys[-1] + h/9 * (2*k1 + 3*k2 + 4*k3))
        ynext = ys[-1] + h/9 * (2*k1+3*k2+4*k3)
        ynext_til = ys[-1] + h/24 * (7*k1+6*k2+8*k3+3*k4)
        ys.append(ynext)
        ys_til.append(ynext_til)
        t = tnext
    return np.array(ys[:-1]),np.array(ys_til[:-1])

# ---------------------------------------------------------------------------- #

##### Vectorized 2nd/3rd Order Adaptative Runge Kutta (uses 3rd order to verify 2nd order solution)
### Input:  F -> Differential equation;
###         y0 -> list or scalar for initial condition;
###         tf -> final point in time;
###         p -> list or scalar for parameters for F, default is set to 0 if F has no extra parameters;
### Output: ys -> numpy array with all solutions for each step t, ys is a Matrix
##### Gil Miranda - last revision 26/09/2019
def mylib_rk23_adp(F, tf, y0, tol = 1e-3, p = 0):
    ys = [y0]
    ys_til = [y0]
    h = 0.1
    ts = [0]
    ti = ts[-1]
    while ti < tf:
        k1 = F(ti, ys[-1], p)
        k2 = F(ti + h/2, ys[-1] + k1/2, p)
        k3 = F(ti + 3*h/4, ys[-1] + 3*h*k2/4, p)
        k4 = F(ti + h, ys[-1] + h/9 * (2*k1 + 3*k2 + 4*k3))
        ynext = ys[-1] + h/9 * (2*k1+3*k2+4*k3)
        ynext_til = ys[-1] + h/24 * (7*k1+6*k2+8*k3+3*k4)
        while abs(ynext_til - ynext) > tol:
            h = h/2
            k1 = F(ti, ys[-1], p)
            k2 = F(ti + h/2, ys[-1] + k1/2, p)
            k3 = F(ti + 3*h/4, ys[-1] + 3*h*k2/4, p)
            k4 = F(ti + h, ys[-1] + h/9 * (2*k1 + 3*k2 + 4*k3))
            ynext = ys[-1] + h/9 * (2*k1+3*k2+4*k3)
            ynext_til = ys[-1] + h/24 * (7*k1+6*k2+8*k3+3*k4)
        h = h*(tol/abs(ynext_til - ynext))**(1/(2))
        ys.append(ynext)
        ys_til.append(ynext_til)
        ti += h
        ts.append(ti)
    return np.array(ys),np.array(ys_til), ts
