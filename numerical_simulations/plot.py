from math import log
import matplotlib.pyplot as plt


#xlist = [0.1, 0.07, 0.03, 0.01, 0.007, 0.003, 0.001, 0.0007, 0.0003, 0.0001]
x_list = [0.1, 0.04, 0.02, 0.01, 0.004, 0.002, 0.001, 0.0004, 0.0002, 0.0001]
#ylist = [1.9628720274749862, 0.8210484760414204, 0.7044713239319443, 1.00420970409681, 0.9943519712259054, 1.00042437011137, 1.0003313606236395, 1.0000661062695848, 1.0000098288220713, 1.0000034656271268]
y_list = [1.9628720274749862, 0.49905207794877127, 0.8762215772023585, 1.00420970409681, 1.0041638199498022, 1.0012317378226068, 1.0003313606236395, 1.0000551300106866, 1.000013903900782, 1.0000034656271268]
xnewlist = []
ynewlist = []
for i in x_list:
    i = -log(i, 10)
    xnewlist.append(i)
#print (xnewlist)
for i in y_list:
    i = log(abs(i-1.0), 10)
    ynewlist.append(i)
#print (ynewlist)
plt.plot(xnewlist, ynewlist, "ro")
plt.ylabel("log of |ratio-1|")
plt.xlabel("negative log of time steps ")
plt.savefig("different_time_step.png", dpi = 300)
plt.show()