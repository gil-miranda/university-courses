from math import sqrt
from math import cos
from math import atan2
from math import sin

class Body:
    ## All vectors are decomposed in x-axis and y-axis
    ## p = (x,y) -> Actual Position Vector
    ## v = (x,y) -> Actual Velocity Vector
    ## pos_x -> List of all x-axis positions over time
    ## pos_y -> List of all y-axis positions over time
    ## color -> Orbit trace and planet color

    def __init__(self, name_of = 'UNNAMED', color_of = 'gray'):
        self.name = name_of
        self.color = color_of

    mass = 0
    v_x = v_y = v_x0 = v_y0 = v_z = v_z0 = 0
    p_x = p_y = p_x0 = p_y0 = p_z = p_z0 = 0
    pos_x = []
    pos_y = []
    pos_z = []
    angle = 0
    kinetic = 0
    potential = 0
    ang_mo = 0

    def acceleration(self, bodies, pos = [0,0,0], retpe = False, G = 6.67428e-11, retm = False):
        acc_x = acc_y = acc_z = 0
        pe = 0
        m = 0
        for other in bodies:
            if self is other:
                continue
            d_x = (other.p_x - pos[0])
            d_y = (other.p_y - pos[1])
            d_z = (other.p_z - pos[2])
            d = sqrt(d_x**2 + d_y**2 + d_z**2) ## Calculate the distance between the bodies
            if d == 0:
                raise ValueError('The bodies %r and %r collided' %(self.name, other.name))

            ## Compute acceleration OTHER causes on THIS
            acc = G * other.mass / d**2

            if retm:
                v = self.v_x**2 + self.v_y**2 #v^2
                dsun = (self.p_x**2 + self.p_y**2)
                try:
                    m += sqrt(dsun * (self.mass**2 * v) - (self.p_x * self.v_x * self.mass + self.mass * self.p_y * self.v_y)**2)
                except:
                    m += 0

            ## Compute potential Energy
            if retpe:
                pe += G * other.mass * self.mass / d
            ## Decomposing the acceleration on x-axis and y-axis
            theta = atan2(d_y, d_x)
            a_x = acc * cos(theta)
            a_y = acc * sin(theta)
            a_z = acc * sin(self.angle)
            acc_x += a_x
            acc_y += a_y
            acc_z += a_z


        if retpe and retm:
            return acc_x, acc_y, acc_z, pe, m
        else:
            return acc_x, acc_y, acc_z
