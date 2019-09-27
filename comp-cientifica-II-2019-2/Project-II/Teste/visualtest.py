from vpython import *
print('oi')

Sun = sphere(pos=(0,0,0), radius = 100, color = color.orange)
earth = sphere(pos(0,0,0), radius = 10, material = materials.earth)
earthv = vector(0,0,5)
for i in range(0,100):
    earth.pos += earthv
