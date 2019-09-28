from vpython import *
print('oi')

scene = canvas(width = 600, height = 600, center = vector(0,5,0))
Sun = sphere(pos=vector(0,0,0), radius = 100, color = color.orange)
earth = sphere(pos = vector(-200,0,0), radius = 10, color = color.blue, make_trail=True, trail_type='points', interval=10, retain=50)
earthv = vector(0,5,0)
for i in range(0,10000):
    rate(100)
    earth.pos += earthv
