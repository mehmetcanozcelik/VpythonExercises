from vpython import *

scene = canvas(width=550, height=580)

L1= 1
L2= 1

pivot= sphere(pos=vector(0,0,0), radius=0.0001 , color=color.red)

dp1=sphere(pos=pivot.pos+vector(0,L1,0), radius=0.1, color=color.green)
pen1=cylinder(pos=pivot.pos, axis=dp1.pos-pivot.pos, radius=0.015, color=color.blue)

dp2=sphere(pos=dp1.pos+vector(L1,L1,0), radius=0.1, color=color.green)
pen2=cylinder(pos=dp1.pos, axis=dp2.pos-dp1.pos, radius=0.015, color=color.blue)


g=9.8
theta1=pi
omega1=pi-0.1
theta2=0
omega2=0
t=0
dt=0.0001


pen1.axis=dp1.pos-pivot.pos
pen2.pos=dp1.pos
pen2.axis=dp2.pos-dp1.pos

while t<500:
    rate(3000)
    theta2new= (-g*((2*sin(theta1)-sin(omega1)*cos(theta1-omega1)))/L1-0.5*(theta2*theta2)*sin(2*theta1-2*omega1)-((omega2*omega2)*sin(theta1-omega1)))/(1+(sin(theta1-omega1)*sin(theta1-omega1)))
    omega2new= (-g*((2*sin(omega1)-2*sin(theta1)*cos(theta1-omega1)))/L1+0.5*(omega2*omega2)*sin(2*theta1-2*omega1)+(2*(theta2*theta2)*sin(theta1-omega1)))/(1+(sin(theta1-omega1)*sin(theta1-omega1)))
    
    
    theta2=theta2+theta2new*dt
    omega2=omega2+omega2new*dt
    theta1=theta1+theta2*dt
    omega1=omega1+omega2*dt

    dp1.pos=pivot.pos+vector(L1*sin(theta1),-L1*cos(theta1),0)
    dp2.pos=dp1.pos+vector(L2*sin(theta2),-L2*cos(theta2),0)
    pen1.axis=dp1.pos-pivot.pos
    pen2.pos=dp1.pos
    pen2.axis=dp2.pos-dp1.pos
    t=t+dt
    
