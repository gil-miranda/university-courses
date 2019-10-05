from math import sqrt
from math import cos
from math import atan2
from math import sin
import numpy as np

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
        self.mass = 0
        self.v_x = self.v_y = self.v_x0 = self.v_y0 = self.v_z = self.v_z0 = 0
        self.p_x = self.p_y = self.p_x0 = self.p_y0 = self.p_z = self.p_z0 = 0
        self.r = np.zeros(3)
        self.r_0 = np.zeros(3)
        self.v = np.zeros(3)
        self.v_0 = np.zeros(3)
        self.pos_x = []
        self.pos_y = []
        self.pos_z = []
        self.angle = 0
        self.kinetic = 0
        self.potential = 0
        self.ang_mo = 0
    
    
    def acceleration(self, bodies, pos = np.array([0,0,0]), retpe = False, G = 6.67428e-11, retm = False):
        acc = [0,0,0]
        pe = 0
        m = 0
        for other in bodies:
            if self is other:
                continue
            d_vec = other.r - pos
            d = np.linalg.norm(d_vec) ## Calculate the distance between the bodies
            if d == 0:
                print(other.r)
                print(pos)
                raise ValueError('The bodies %r and %r collided' %(self.name, other.name))

            ## Compute acceleration OTHER causes on THIS
            a = -G * other.mass * pos / d**3

            if retm:
                v = np.linalg.norm(self.v)**2 #v^2
                dsun = np.linalg.norm(self.r)
                try:
                    m += sqrt(dsun * (self.mass**2 * v) - (self.r[0] * self.v[0] * self.mass + self.mass * self.r[1] * self.v[1])**2)
                except:
                    m += 0

            ## Compute potential Energy
            if retpe:
                pe += G * other.mass * self.mass / d
            acc = acc + a

        if retpe and retm:
            return acc[0], acc[1], acc[2], pe, m
        else:
            return acc[0], acc[1], acc[2]
