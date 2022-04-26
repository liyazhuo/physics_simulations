#We will model the motions of spring pendulum
from vpython import *
import matplotlib.pyplot as plt


#Setup some constants
g = vector(0, -9.8, 0) #gravity constant
m = 5.0 #mass of the weight
k = 10.0 #spring constant
L = 10.0 #length of the spring

#Setup the spring and weight
equilibrium = vector(0, -m*mag(g)/k, 0)
pivot = vector(0,10,0)
weight = sphere(pos = equilibrium, vel = vector(0,0,0), radius = 0.2)
spring = helix(pos=pivot, axis=( weight.pos - pivot), color = color.yellow)

#Setup air drag
A = pi*(weight.radius)**2#Cross area size
rho = 1.1#Air density
C =  0.7 #drag coefficient

#Resonance (Natural ways for the weight to oscillate around the spring)
T = 2*pi*sqrt(m/k) #Up and down oscillation
#T = 2*pi*sqrt(L/mag(g)+m/k) #Left and right oscillation
#T = 4.2
amp = 0.2 #amplification

#Make the weight move
t = 0.0
dt = 0.01


while t < 100:
    rate(500)         
    spring.axis = weight.pos - pivot  
    a = g - k*(mag(spring.axis)-L)*norm(spring.axis)/m -0.5*A*C*rho*mag(weight.vel)**2*norm(weight.vel)/m #acceleration
    weight.vel = weight.vel + a*dt
    weight.pos = weight.pos+ weight.vel*dt
    pivot = amp*vector(sin(2*pi*t/T), cos(2*pi*t/T), 0) + vector(0,10,0) #adding oscillation 
    t+=dt

