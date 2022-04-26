#We will model the motions of spring pendulum with oscillation without any vpython objects.
from vpython import *
import matplotlib.pyplot as plt


#Setup some constants
g = vector(0, -9.8, 0) #gravity constant
m = 5.0 #mass of the weight
k = 10.0 #spring constant
L = 10.0 #length of the spring

#Setup the spring and weight
equilibrium = vector(0, -m*mag(g)/k, 0)
weight_pos = equilibrium
weight_vel = vector(0,0,0)
weight_radius = 0.2
pivot = vector(0,10,0)

spring_pos = pivot
spring_axis = weight_pos - pivot

#Setup air drag
A = pi*(weight_radius)**2#Cross area size
rho = 1.1#Air density
C =  0.7 #drag coefficient

#Resonance (Natural ways for the weight to oscillate around the spring)
#T = 2*pi*sqrt(m/k) #Up and down oscillation
#T = 2*pi*sqrt(L/mag(g)+m/k) #Left and right oscillation
T = 1.0
amp = 0.2 #amplification

#Make the weight move
t = 0.0
dt = 0.01
dT = 0.01
maxdlist = []
Tlist = []

while T < 12.0:
    t = 0.0
    maxd = 0
    while t < 100: 
        spring_axis = weight_pos - pivot  
        a = g - k*(mag(spring_axis)-L)*norm(spring_axis)/m -0.5*A*C*rho*mag(weight_vel)**2*norm(weight_vel)/m #acceleration
        weight_vel = weight_vel + a*dt
        weight_pos = weight_pos+ weight_vel*dt
        pivot = amp*vector(sin(2*pi*t/T), cos(2*pi*t/T), 0) + vector(0,10,0) #adding oscillation 

        displacement = mag(weight_pos-equilibrium)
        maxd = max(displacement,maxd)
        t+=dt
    T = T+dT
    Tlist.append(T)
    maxdlist.append(maxd)

plt.plot(Tlist, maxdlist, "r-")
plt.ylabel("Maximum displacement of the pendulum (m)")
plt.xlabel("oscilllation time period (s)")
plt.savefig("different_time_period", dpi = 300)
plt.show()