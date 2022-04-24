import matplotlib.pyplot as plt
#This is to model how the intensity of light decreases as it penetrates deeper into the dust cloud.

# Starting conditions
x = 0.0 #starting position
I = 1000.0 #Initial light intensity
N=2.0e6 #Number of dust grains per unit volumn
sigma = 1.0e-8 #Cross section area of each dust grain

# Plot
xlist = []
Ilist = []
# Set up time step
dx = 0.1

# Set up a loop

while I >= 10.0: 
    dI = -I*N*sigma*dx
    I = I + dI
    x = x + dx
    xlist.append(x)
    Ilist.append(I)


print(x)
plt.plot(xlist, Ilist, "ro")
plt.ylabel("Light Intensity")
plt.xlabel("time (s)")
#plt.savefig("different_time_step.png", dpi = 300)
plt.show()