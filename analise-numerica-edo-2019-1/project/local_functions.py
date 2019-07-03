from numpy import linspace
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

AU = (149.6e9)

def simulate(bodies, step = 3600, period = 365, method = 'euler', G = 6.67428e-11):
    count = 0
    pos = {}
    energy = {}
    momentum = {}
    for body in bodies:
        pos[body.name] = []
        energy[body.name] = []
        momentum[body.name] = []
        ## Routine that resets body position state in each simulation
        body.p_x = body.p_x0
        body.p_y = body.p_y0
        body.v_x = body.v_x0
        body.v_y = body.v_y0

    while count < period:
        acc = {}
        for body in bodies:
            acc_x = acc_y = 0
            for other in bodies:
                if body is other:
                    continue
                acc_x, acc_y, body.energy, body.momentum = body.acceleration(bodies, pos = [body.p_x, body.p_y], retm = True, retangle = True, retpe = True)
                acc[body] = (acc_x, acc_y)

        for body in bodies:
            pos[body.name].append((body.p_x,body.p_y))
            energy[body.name].append(body.energy)
            momentum[body.name].append(body.momentum)

            a_x, a_y = acc[body]

            if method == 'euler-cromer':
            ## Sympletic 1st-order Euler
                body.v_x += a_x * step
                body.v_y += a_y * step

                body.p_x += body.v_x * step
                body.p_y += body.v_y * step
            elif method == 'velocity-verlet':
            ## Velocity Verlet / Leapfrog - Sympletic 2nd-order methods
                vhalf_x = body.v_x +  0.5 * step * a_x
                vhalf_y = body.v_y +  0.5 * step * a_y

                body.p_x += vhalf_x * step
                body.p_y += vhalf_y * step

                ax_new, ay_new = body.acceleration(bodies, pos = [body.p_x, body.p_y])

                body.v_x = vhalf_x + ax_new * 0.5 * step
                body.v_y = vhalf_y + ay_new * 0.5 * step

            elif method == 'position-verlet':
            ## Velocity Verlet / Leapfrog - Sympletic 2nd-order methods
                phalf_x = body.p_x +  0.5 * step * body.v_x
                phalf_y = body.p_y +  0.5 * step * body.v_y

                ax_new, ay_new = body.acceleration(bodies, pos = [phalf_x, phalf_y])

                body.v_x += ax_new * step
                body.v_y += ay_new * step

                body.p_x = phalf_x + body.v_x * step/2
                body.p_y = phalf_y + body.v_y * step/2

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
    return pos, energy, momentum

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
    energy = {}
    momentum = {}
    for m in methods:
        pos[m] = []
        energy[m] = []
        momentum[m] = []
        for h in steps:
            ret_pos, ret_energy, ret_momentum = simulate(bod, period = t, method = m, step = h)
            pos[m].append([h, ret_pos])
            energy[m].append([h, ret_energy])
            momentum[m].append([h, ret_momentum])
    return pos, energy, momentum

def big_plotter(methods = ['euler'], steps = [3600], graph = ['orbit'], opt = ['bodies', 'The Solar System'], pos_vec = [0], en_vec = [0], mom_vec = [0]):
    t = len(pos_vec['euler'][0][1]['Sun'])
    ts = linspace(0,2*t/24,t)
    for m in methods:
        #sim_steps = pos_vec[m]
        #print(sim_steps[0])
        if 'orbit' in graph:
                j = 0
                for h in steps:
                    orbit_plotter(pos_vec[m][j][1], opt[0], title = opt[1] + ' - ' + m + ' - h = ' + str(h))
                    j += 1

        if 'energy' in graph:
            for b in opt[0][1:]:
                i = 0
                plt.figure(figsize=(12,8))
                for h in steps:
                    plt.plot(ts, en_vec[m][i][1][b.name], label = 'h = ' + str(h) + ' $\Delta = $ '+ '{0:.3f}'.format((max(mom_vec[m][i][1][b.name])/min(mom_vec[m][i][1][b.name]) -1)*100) + '%')
                    i += 1
                plt.title(b.name + ' - ' + m)
                plt.xlabel('Days')
                plt.ylabel('Energy')
                plt.legend(loc = 1)
                plt.grid(alpha = 0.5)
                plt.show()
        if 'momentum' in graph:
            for b in opt[0][1:]:
                k = 0
                plt.figure(figsize=(12,8))
                for h in steps:
                    plt.plot(ts, mom_vec[m][k][1][b.name], label =  'h = ' + str(h)  + ' $\Delta = $ '+ '{0:.2f}'.format((max(mom_vec[m][k][1][b.name])/min(mom_vec[m][k][1][b.name]) -1)*100) + '%')
                    k += 1
                plt.title(b.name + ' - ' + m)
                plt.xlabel('Days')
                plt.grid(alpha = 0.5)
                plt.ylabel('Angular Momentum')
                plt.legend(loc = 1)
                plt.show()
