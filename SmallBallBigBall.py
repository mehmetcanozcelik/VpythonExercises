from vpython import*
import random
import numpy as np

scene = canvas(width=550, height=580)

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

Smallball = sphere(pos= vector(0,0,0), radius=0.4, color=color.red, mass=1)
Bigball = sphere(pos= vector(1,2,0), radius=0.9, color=color.blue, mass=0.1)

wallR= box(pos= vector(4,0,0), size=vector(1,7,0), color=color.orange)
wallL= box(pos= vector(-4,0,0), size=vector(1,7,0), color=color.orange)
wallT= box(pos= vector(0,4,0), size=vector(7,1,0), color=color.orange)
wallB= box(pos= vector(0,-4,0), size=vector(7,1,0), color=color.orange)

rndX = random.random()
rndY = random.random()

Smallball.vel = vector(rndX,rndY,0)
Bigball.vel = vector(rndX,rndY,0)
m1=1
m2=1
m = m1+m2

attach_trail(Bigball)

t=0
dt=0.01

while t<10000:
    rate(1000)
    Smallball.pos = Smallball.pos + Smallball.vel*dt
    Bigball.pos = Bigball.pos + Bigball.vel*dt
    SBOld = Smallball.vel
    BBOld = Bigball.vel

    if abs(Smallball.pos.x) >= wallR.pos.x-1:
        Smallball.vel.x = -Smallball.vel.x
    elif abs(Smallball.pos.y) >= wallT.pos.y-1:
        Smallball.vel.y = -Smallball.vel.y
    elif abs(Bigball.pos.x) >= wallR.pos.x-1:
        Bigball.vel.x = -Bigball.vel.x
    elif abs(Bigball.pos.y) >= wallT.pos.y-1:
        Bigball.vel.y = -Bigball.vel.y
    elif distance(Smallball.pos.x, Smallball.pos.y, Bigball.pos.x, Bigball.pos.y) <= 1.3:
        SBOld = Smallball.vel
        BBOld = Bigball.vel

        Smallball.vel = ((Smallball.mass-Bigball.mass)/(Smallball.mass+Bigball.mass))*SBOld + ((2*Bigball.mass)/(Smallball.mass+Bigball.mass))*BBOld
        Bigball.vel = ((2*Smallball.mass)/(Smallball.mass + Bigball.mass))*SBOld -((Smallball.mass - Bigball.mass)/(Smallball.mass+Bigball.mass))*BBOld
        
        
    t = t + dt
    
    
