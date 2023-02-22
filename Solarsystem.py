from vpython import *

scene = canvas(width=1100, height=1160)
R = 15e9
Rmr = 70e9
Rvn = 110e9
Re = 150e9
Rmrs = 250e9
Ms = 2e30
Mmr = 0.3e24
Mvn = 5e24
Me = 6e24
Mmrs = 0.6e24
G = 6.67e-11

sun = sphere(pos= vector(0,0,0), radius=R, color=color.yellow)
sun.m=Ms

mercury = sphere(pos= vector(Rmr,0,0), radius=0.2*R, color=color.green)
mercury.m= Mmr
mercury.p= vector(0,47e3,0)*mercury.m

venus = sphere(pos= vector(Rvn,0,0), radius=0.3*R, color=color.purple)
venus.m= Mvn
venus.p= vector(0,35e3,0)*venus.m

earth = sphere(pos= vector(Re,0,0), radius=0.4*R, color=color.blue)
earth.m= Me
earth.p= vector(0,30e3,0)*earth.m

mars = sphere(pos= vector(Rmrs,0,0), radius=0.5*R, color=color.red)
mars.m= Mmrs
mars.p= vector(0,24e3,0)*mars.m

sun.p= -(earth.p)

attach_trail(mercury)
attach_trail(venus)
attach_trail(earth)
attach_trail(mars)


t=0
dt=500

while t<15000000000:
    rate(10000)

    rse=earth.pos-sun.pos
    rsm=mercury.pos-sun.pos
    rsv=venus.pos-sun.pos
    rsmrs=mars.pos-sun.pos


    Fsm= -G*sun.m*mercury.m*norm(rsm)/mag(rsm)**2
    Fms= -Fsm

    Fsv= -G*sun.m*venus.m*norm(rsv)/mag(rsv)**2
    Fvs= -Fsv

    Fse= -G*sun.m*earth.m*norm(rse)/mag(rse)**2
    Fes= -Fse

    Fsmrs= -G*sun.m*mars.m*norm(rsmrs)/mag(rsmrs)**2
    Fmrss= -Fsmrs

    
    

    mercury.p=mercury.p+(Fsm)*dt
    venus.p=venus.p+(Fsv)*dt
    earth.p=earth.p+(Fse)*dt
    mars.p=mars.p+(Fsmrs)*dt
    
    

    sun.pos=sun.pos+sun.p*dt/sun.m
    earth.pos=earth.pos+earth.p*dt/earth.m
    mercury.pos=mercury.pos+mercury.p*dt/mercury.m
    venus.pos=venus.pos+venus.p*dt/venus.m
    mars.pos=mars.pos+mars.p*dt/mars.m
    
    t=t+dt
    
