from numpy import linspace
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits import mplot3d
import numpy as np
AU = (149.6e9)

def simulate(bodies, step = 3600, period = 365, method = 'euler', G = 6.67428e-11):
    count = 0
    pos = {}
    vel_sq = {}
    potential = {}
    ang_mo = {}
    for body in bodies:
        pos[body.name] = []
        vel_sq[body.name] = []
        potential[body.name] = []
        ang_mo[body.name] = []
        ## Routine that resets body position state in each simulation
        body.p_x = body.p_x0
        body.p_y = body.p_y0
        body.p_z = body.p_z0
        body.v_x = body.v_x0
        body.v_y = body.v_y0
        body.v_z = body.v_z0

    while count < period:
        acc = {}
        for body in bodies:
            acc_x = acc_y = acc_z = 0
            for other in bodies:
                if body is other:
                    continue
                acc_x, acc_y, acc_z, body.potential, body.ang_mo = body.acceleration(bodies, pos = [body.p_x, body.p_y, body.p_z], retm = True, retpe = True)
                acc[body] = (acc_x, acc_y, acc_z)

        for body in bodies:
            pos[body.name].append((body.p_x,body.p_y, body.p_z))
            vel_sq[body.name].append((body.v_x**2 + body.v_y**2 + body.v_z**2))
            potential[body.name].append(body.potential)
            #print(str(body.ang_mo) + ' - ' + body.name)
            ang_mo[body.name].append(body.ang_mo)

            a_x, a_y, a_z = acc[body]

            if method == 'euler-cromer':
            ## Sympletic 1st-order Euler
                body.v_x += a_x * step
                body.v_y += a_y * step
                body.v_z += a_z * step
                
                body.p_x += body.v_x * step
                body.p_y += body.v_y * step
                body.p_z += body.v_z * step
            elif method == 'velocity-verlet':
            ## Velocity Verlet / Leapfrog - Sympletic 2nd-order methods
                vhalf_x = body.v_x + 0.5 * step * a_x
                vhalf_y = body.v_y + 0.5 * step * a_y
                vhalf_z = body.v_z + 0.5 * step * a_z
 
                body.p_x += vhalf_x * step
                body.p_y += vhalf_y * step
                body.p_z += vhalf_z * step

                ax_new, ay_new, az_new = body.acceleration(bodies, pos = [body.p_x, body.p_y, body.p_z])

                body.v_x = vhalf_x + ax_new * 0.5 * step
                body.v_y = vhalf_y + ay_new * 0.5 * step
                body.v_z = vhalf_z + az_new * 0.5 * step

            elif method == 'position-verlet':
            ## Velocity Verlet / Leapfrog - Sympletic 2nd-order methods
                phalf_x = body.p_x +  0.5 * step * body.v_x
                phalf_y = body.p_y +  0.5 * step * body.v_y
                phalf_z = body.p_z + 0.5 * step * body.v_z

                ax_new, ay_new, az_new = body.acceleration(bodies, pos = [phalf_x, phalf_y, phalf_z])

                body.v_x += ax_new * step
                body.v_y += ay_new * step
                body.v_z += az_new * step

                body.p_x = phalf_x + body.v_x * step/2
                body.p_y = phalf_y + body.v_y * step/2
                body.p_z = phalf_z + body.v_z * step/2

            elif method == 'leapfrog':
                w = 2**(1./3.)
                f = 2 - w

                lf1 = (0.5 * step / f)
                p1_x = body.p_x + lf1 * body.v_x
                p1_y = body.p_y + lf1 * body.v_y

                ax_new, ay_new = body.acceleration(bodies, pos = [p1_x, p1_y])

                lf2 = step / f
                v2_x = body.v_x + lf2 * ax_new
                v2_y = body.v_y + lf2 * ay_new

                lf3 = (1 - w) * step * 0.5 / f
                p3_x = p1_x + lf3 * v2_x
                p3_y = p1_y + lf3 * v2_y

                ax_new, ay_new = body.acceleration(bodies, pos = [p3_x, p3_y])

                lf4 = -step * w / f
                v4_x = v2_x + lf4 * ax_new
                v4_y = v2_y + lf4 * ay_new

                p5_x = p3_x + lf3 * v4_x
                p5_y = p3_y + lf3 * v4_y

                ax_new, ay_new = body.acceleration(bodies, pos = [p5_x, p5_y])

                body.v_x = v4_x + lf2 * ax_new
                body.v_y = v4_y + lf2 * ay_new

                body.p_x = p5_x + lf1 * body.v_x
                body.p_y = p5_y + lf1 * body.v_y

            else:
            ## 1st-order Euler
                body.p_x += body.v_x * step
                body.p_y += body.v_y * step

                body.v_x += a_x * step
                body.v_y += a_y * step
        count += 1
    return pos, vel_sq, potential, ang_mo

def momentum_calc(bodies, methods, hs, vel_vec, t):
    momentum = {}
    for m in methods:
        momentum[m] = []
        for h in range(0,len(hs)):
            mom = np.array([0.0]*t)
            for b in bodies:
                mom += vel_vec[m][h][1][b.name]
            mom = mom / 2
            momentum[m].append((h, mom))
    return momentum

def ang_mo_calc(bodies, methods, hs, mo_vec, t):
    ang_mo = {}
    for m in methods:
        ang_mo[m] = []
        for h in range(0,len(hs)):
            mo = np.array([0.0]*t)
            for b in bodies:
                mo += mo_vec[m][h][1][b.name]
            mo = mo / 2
            ang_mo[m].append((h, mo))
    return ang_mo

def potential_calc(bodies, methods, hs, pot_vec, t):
    potential = {}
    for m in methods:
        potential[m] = []
        for h in range(0,len(hs)):
            pot = np.array([0.0]*t)
            for b in bodies:
                pot += pot_vec[m][h][1][b.name]
            pot = pot / 2
            potential[m].append((h, pot))
    return potential

def orbit_plotter(pos, bodies, title = 'Orbits', scale = False, color = False):
    for b in bodies:
        b.pos_x = [i[0] for i in pos[b.name]]
        b.pos_y = [i[1] for i in pos[b.name]]

    plt.figure(figsize=(10,10))

    for b in bodies:
        plt.plot(b.pos_x, b.pos_y, label = b.name, color = b.color, linestyle=':' )
        plt.scatter(b.pos_x[-1],b.pos_y[-1], color = b.color)

    plt.legend()
    plt.grid(alpha=0.2)


    ax = plt.gca()
    if color:
        ax.set_facecolor('black')
    ticks = ticker.FuncFormatter(lambda x, pos: '{0:.2f}'.format(x/AU))
    ax.xaxis.set_major_formatter(ticks)
    ax.yaxis.set_major_formatter(ticks)
    plt.xlabel('Latitudinal distance in AU')
    plt.ylabel('Longitudinal distance in AU')

    plt.title(title)
    plt.show()
    return ax

def big_simulation(methods = ['euler'], steps = [3600], t = 1000, bod = 0):
    pos = {}
    vel = {}
    energy = {}
    ang_mo = {}
    for m in methods:
        pos[m] = []
        vel[m] = []
        energy[m] = []
        ang_mo[m] = []
        for h in steps:
            ret_pos, ret_vel, ret_energy, ret_ang = simulate(bod, period = t, method = m, step = h)
            pos[m].append([h, ret_pos])
            vel[m].append([h, ret_vel])
            energy[m].append([h, ret_energy])
            ang_mo[m].append([h, ret_ang])
    return pos, vel, energy, ang_mo



def big_plotter(methods = ['euler'], t = 100, steps = [3600], graph = ['orbit'], opt = ['bodies', 'The Solar System'], pos_vec = [0], u_vec = [0], p_vec = [0], ang_vec = [0]):
    ts = linspace(0,t,t)
    for m in methods:
        if 'orbit' in graph:
                j = 0
                for h in steps:
                    orbit_plotter(pos_vec[m][j][1], opt[0], title = opt[1] + ' - ' + m + ' - h = ' + '{0:.2f}'.format(h/(3600*24)) + ' days')
                    j += 1

        if 'hamilton' in graph:
            plt.figure(figsize=(12,8))
            i = 0
            for h in steps:
                H = p_vec[m][i][1] - u_vec[m][i][1]
                plt.plot(ts, H, label = 'h = ' + '{0:.2f}'.format(h/(3600*24)) + ' days -> '+ ' $\Delta = $ '+ '{0:.3f}'.format(((max(H)-min(H))/min(H))*100) + '%')
                i += 1
            plt.title('Hamiltoniano - '+ m)
            plt.xlabel('Periods')
            plt.ylabel('Hamiltonian')
            plt.legend(loc = 1)
            plt.grid(alpha = 0.5)
            plt.show()

        if 'momentum' in graph:
            plt.figure(figsize=(12,8))
            i = 0
            for h in steps:
                plt.plot(ts, ang_vec[m][i][1], label = 'h = ' + '{0:.2f}'.format(h/(3600*24)) + ' days -> '+ ' $\Delta = $ '+ '{0:.6f}'.format(((max(ang_vec[m][i][1])-min(ang_vec[m][i][1]))/min(ang_vec[m][i][1]))*100) + '%')
                i += 1
            plt.title('Angular Momentum - '+ m)
            plt.xlabel('Periods')
            plt.ylabel('Angular Momentum')
            plt.legend(loc = 1)
            plt.grid(alpha = 0.5)
            plt.show()

            
def orbit_plotter3D(pos, bodies, title = 'Orbits', scale = False, color = False):
    for b in bodies:
        b.pos_x = [i[0] for i in pos[b.name]]
        b.pos_y = [i[1] for i in pos[b.name]]
        b.pos_z = [i[2] for i in pos[b.name]]

    plt.figure(figsize=(10,10))
    ax = plt.axes(projection='3d')
    
    for b in bodies:
        
        ax.plot3D(b.pos_x, b.pos_y, b.pos_z, label = b.name, color = b.color, linestyle=':')
        #plt.title('Atrator de Lorenz', fontweight = 'bold')
        #plt.show()
        #plt.plot(b.pos_x, b.pos_y, label = b.name, color = b.color, linestyle=':' )
        ax.scatter3D(b.pos_x[-1],b.pos_y[-1], b.pos_z[-1], color = b.color)

    plt.legend()
    plt.grid(alpha=0.2)


    ax = plt.gca()
    if color:
        ax.set_facecolor('black')
    ticks = ticker.FuncFormatter(lambda x, pos: '{0:.2f}'.format(x/AU))
    ax.xaxis.set_major_formatter(ticks)
    ax.yaxis.set_major_formatter(ticks)
    plt.xlabel('Latitudinal distance in AU')
    plt.ylabel('Longitudinal distance in AU')

    plt.title(title)
    plt.show()
    return ax

def big_plotter3D(methods = ['euler'], t = 100, steps = [3600], graph = ['orbit'], opt = ['bodies', 'The Solar System'], pos_vec = [0], u_vec = [0], p_vec = [0], ang_vec = [0]):
    ts = linspace(0,t,t)
    for m in methods:
        if 'orbit' in graph:
                j = 0
                for h in steps:
                    orbit_plotter3D(pos_vec[m][j][1], opt[0], title = opt[1] + ' - ' + m + ' - h = ' + '{0:.2f}'.format(h/(3600*24)) + ' days')
                    j += 1

        if 'hamilton' in graph:
            plt.figure(figsize=(12,8))
            i = 0
            for h in steps:
                H = p_vec[m][i][1] - u_vec[m][i][1]
                plt.plot(ts, H, label = 'h = ' + '{0:.2f}'.format(h/(3600*24)) + ' days -> '+ ' $\Delta = $ '+ '{0:.3f}'.format(((max(H)-min(H))/min(H))*100) + '%')
                i += 1
            plt.title('Hamiltoniano - '+ m)
            plt.xlabel('Periods')
            plt.ylabel('Hamiltonian')
            plt.legend(loc = 1)
            plt.grid(alpha = 0.5)
            plt.show()

        if 'momentum' in graph:
            plt.figure(figsize=(12,8))
            i = 0
            for h in steps:
                plt.plot(ts, ang_vec[m][i][1], label = 'h = ' + '{0:.2f}'.format(h/(3600*24)) + ' days -> '+ ' $\Delta = $ '+ '{0:.6f}'.format(((max(ang_vec[m][i][1])-min(ang_vec[m][i][1]))/min(ang_vec[m][i][1]))*100) + '%')
                i += 1
            plt.title('Angular Momentum - '+ m)
            plt.xlabel('Periods')
            plt.ylabel('Angular Momentum')
            plt.legend(loc = 1)
            plt.grid(alpha = 0.5)
            plt.show()