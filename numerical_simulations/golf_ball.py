# Set constants
from vpython import *

rball = 0.021
Aball = pi*rball**2
mball = 0.046
C = 0.2
g = 9.8
rho = 1.2

# Pre-compute drag constant

dragconstant = 0.5*C*rho*Aball

#Set up starting conditions

theta = 13.0*pi/180.0 # Convert to radians built in
v0 = 60.0
v_wind = vector(-80.0,0,0) #Wind speed on the x direction


# Set up objects
ball=sphere(pos=vector(0,0.01,0),
vel=v0*vector(cos(theta),sin(theta),0), radius = rball,
color=color.white, make_trail=True)
ground = box(pos = vector(0,-1,0),
length=240, width=10, height=1,
color=color.green)

t = 0.0
dt = 0.01
g = vector(0,-9.8,0)

# loop
while ball.pos.y > 0.0:
    # Compute Force
    rate(100)
    acc = -dragconstant*mag(ball.vel-v_wind)**2*norm(ball.vel-v_wind)/mball + g

    # Update the quantities
    ball.vel = ball.vel+acc*dt
    ball.pos = ball.pos + ball.vel*dt

    t += dt

print("Finishes at",ball.pos)