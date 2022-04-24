# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 12:26:57 2022

@author: desk_
"""

from pickle import GLOBAL
from vpython import *
import pylab as plt

#All variables have the standard scientific units, ie. distance - meter, time - second, mass - kg, etc

#set up black hole
M = 8.0*10**30 #Mass of the black hole
G = 6.67*10**(-11) #gravitational constant
h = 1000000.0 #initial distance from black hole
EventHorizon = sphere(pos=vector(0,0,0), radius = 11000.0, color=color.black) #Position and size of the black hole
DangerZone = sphere(pos=vector(0,0,0), radius = 311000.0, color=color.red, opacity = 0.5) #Spaceship will be torn apart within this zone

# Set up spaceship

theta = 90*pi/180.0 #inital angle
#v0 = 16000000.0 #Inital velocity of spaceship
v0 = sqrt(G*M/h) #Inital velocity of spaceship needed for a perfect circular orbit around the black hole 
ship = sphere(pos = vector(h,0,0), vel=vector(v0*cos(theta),v0*sin(theta),0), radius = 20000.0, color=color.yellow)

#print (v0)

# Move spaceship via loop
t = 0.0 
dt = 0.0001 #time step
t_full = 2*pi*h/v0 #running time for orbit of a full circle


while t < t_full:
    rate(100)
    t = t + dt
    a = -G*M/(mag(ship.pos)**2)*norm(ship.pos) #acceleration of the ship due to gravity
    ship.vel = ship.vel + a*dt
    ship.pos = ship.pos + ship.vel*dt 


ratio=(0.5*mag(ship.vel)**2 + G*M/mag(ship.pos))/( 0.5*v0**2 + G*M/h) #Ratio of final energy and initial energy of spaceship, if simulation is perfect, this should be 1.

#print(mag(ship.vel))
#print(mag(ship.pos))
print(ratio)


