import numpy as np
import matplotlib.pyplot as plt


font = {'size'   : 15}

plt.rc('font', **font)



t = np.linspace(0,20,100)
p = 0.4
u = 8
s = 5.4
a = 1.6
f = 30*np.cos(2*np.pi*t/8+p)+70
w = 1-np.exp(-1*((t-u)/s)**2)
h = w*f*a
d = np.cumsum(h)*t[1]
d = d - d[0]
d = d / d[-1] * 18.0


plt.plot(t,d, lw=5)
plt.xlim([0,20])
plt.ylim([0,18])
plt.xticks([10,20], ['10 minutes', '20 minutes'])
plt.yticks([9,18], ['9 miles', '18 miles'])
#plt.xlabel("Time (minutes)")
#plt.ylabel("Distance (miles)")

fig = plt.gcf()
fig.set_size_inches(7, 3)
plt.tight_layout()
plt.savefig(__file__.split("\\")[-1].replace(".py",".png"), dpi=300)