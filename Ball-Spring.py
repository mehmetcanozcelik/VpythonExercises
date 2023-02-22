from vpython import *

scene = canvas(width=550, height=580)

k=1
m=1

V1=vector(0,0,0)
V2=vector(0,0,0)
V3=vector(0,0,0)

wallL = box(pos= vector(-4,0,0), size= vector(0.1,7,0.1), color=color.cyan)
wallR = box(pos= vector(4,0,0), size= vector(0.1,7,0.1), color=color.cyan)

ball1 = sphere(pos= vector(-2,0,0), radius=0.5, color=color.blue)
ball2 = sphere(pos= vector(0,2,0), radius=0.5, color=color.blue)
ball3 = sphere(pos= vector(2,0,0), radius=0.5, color=color.blue)

helix0 = helix(pos=wallL.pos, axis=ball1.pos-wallL.pos, constant=1, radius=0.5, coils=10, thickness=0.05, color=color.green)
helix1 = helix(pos=ball1.pos, axis=ball2.pos-ball1.pos, constant=1, radius=0.5, coils=10, thickness=0.05, color=color.green)
helix2 = helix(pos=ball2.pos, axis=ball3.pos-ball2.pos, constant=1, radius=0.5, coils=10, thickness=0.05, color=color.green)
helix3 = helix(pos=ball3.pos, axis=wallR.pos-ball3.pos, constant=1, radius=0.5, coils=10, thickness=0.05, color=color.green)


t=0
dt=0.001

while True:
    rate(800)
    Pos1=ball1.pos
    Pos2=ball2.pos
    Pos3=ball3.pos

    V1prev=V1
    V2prev=V2
    V3prev=V3

    F1=k*(wallL.pos+Pos2-2*Pos1)
    F2=k*(Pos1+Pos3-2*Pos2)
    F3=k*(Pos2+wallR.pos-2*Pos3)

    V1=V1prev+F1*dt
    V2=V2prev+F2*dt
    V3=V3prev+F3*dt

    ball1.pos=Pos1+V1*dt
    ball2.pos=Pos2+V2*dt
    ball3.pos=Pos3+V3*dt

    helix0.pos=wallL.pos
    helix0.axis=ball1.pos-wallL.pos
    helix1.pos=ball1.pos
    helix1.axis=ball2.pos-ball1.pos
    helix2.pos=ball2.pos
    helix2.axis=ball3.pos-ball2.pos
    helix3.pos=ball3.pos
    helix3.axis=wallR.pos-ball3.pos
