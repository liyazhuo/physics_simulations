# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 12:26:57 2022

@author: desk_
"""
from vpython import *
import pylab as plt

#set up black hole
M = 8.0*10**30
G = 6.67*10**(-11)
h = 1000000.0
EventHorizon = sphere(pos=vector(0,0,0), radius = 11000.0, color=color.black)
DangerZone = sphere(pos=vector(0,0,0), radius = 311000.0, color=color.red, opacity = 0.5)

# Set up spaceship

theta = 90*pi/180.0
v0 = 16000000.0 
#v0 = sqrt(G*M/h)
ship = sphere(pos = vector(h,0,0), vel=vector(v0*cos(theta),v0*sin(theta),0), radius = 20000.0, color=color.yellow)

#print (v0)

#set up graph
#myplot = graph(xtitle = "Time (s)", ytitle = "Height (m)", fast = False)
#line = gcurve(color = color.red )

# Move spaceship via loop
t = 0.0
dt = 0.0001
t_full = 2*pi*h/v0

#print(mag(ship.vel))
#print(mag(ship.pos))


while t < 0.1:
    rate(100)
    t = t + dt
    a = -G*M/(mag(ship.pos)**2)*norm(ship.pos)
    ship.vel = ship.vel + a*dt
    ship.pos = ship.pos + ship.vel*dt 


ratio=(0.5*mag(ship.vel)**2 + G*M/mag(ship.pos))/( 0.5*v0**2 + G*M/h)

#print(mag(ship.vel))
#print(mag(ship.pos))
print(ratio)


