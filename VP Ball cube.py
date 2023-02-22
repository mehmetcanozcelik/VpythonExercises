from vpython import *
import random

scene = canvas(width=550, height=580)

ball = sphere(pos= vector(0,0,0), radius=0.8, color=color.red)

wallR= box(pos= vector(4,0,0), size= vector(1,7,7), color=color.cyan)
wallL= box(pos= vector(-4,0,0), size= vector(1,7,7), color=color.red)
wallT= box(pos= vector(0,4,0), size=vector(7,1,7), color=color.blue)
wallB= box(pos= vector(0,-4,0), size=vector(7,1,7), color=color.orange)
wallBck= box(pos= vector(0,0,-4), size=vector(7,7,1), color=color.magenta)


rndX = random.random()
rndY = random.random()
rndZ = random.random()

ball.vel = vector(rndX,rndY,rndZ)

t = 0
dt = 0.01

while t<50:
    rate(1000)
    ball.pos = ball.pos + ball.vel*dt
    if abs(ball.pos.x) >= wallR.pos.x-1:
        ball.vel.x = -ball.vel.x
        if ball.vel.x <0:
            ball.color = wallR.color
        else :
            ball.color = wallL.color
    elif abs(ball.pos.y) >= wallT.pos.y-1:
        ball.vel.y = -ball.vel.y
        if ball.vel.y <0:
            ball.color = wallT.color
        else :
            ball.color = wallB.color
    elif abs(ball.pos.z) >= -(wallBck.pos.z+1):
        ball.vel.z = -ball.vel.z
        if ball.vel.z <0:
            ball.color = color.white
        else :
            ball.color = wallBck.color
        
    t = t + dt
