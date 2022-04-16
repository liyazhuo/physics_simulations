# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 00:36:42 2022

@author: desk_
"""

from vpython import *


# Set up ground

ground = box(pos=vector(0,0,0), width=8, height=0.1, length=15, color=color.green)
#Set up wind

vwind = vector(-9,0,0)
# Set up ball

V = 20.0
theta = 60.0*pi/180.0 # Convert to radians
rad = 0.5
ball = sphere(pos=vector(0,rad,0), vel = vector(V*cos(theta), V*sin(theta), 0), radius=rad, color=color.red)

# Set up gravity and other constants
m = 0.3
g = vector(0,-9.8,0)
A = (4.0*pi*rad**3)/3.0
C = 0.7
rho = 1.1
# Loop
t = 0
dt = 0.002

while ball.pos.y >= rad:
    rate(100)
    t = t + dt
    a = g - 0.5*A*C*rho*mag(vrel)**2*norm(vrel)/m
    ball.vel = ball.vel + a*dt
    ball.pos = ball.pos + ball.vel*dt
    vrel = ball.vel - vwind
    
print(ball.pos)
