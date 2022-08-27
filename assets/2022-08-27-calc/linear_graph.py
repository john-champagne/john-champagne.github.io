import numpy as np
import matplotlib.pyplot as plt


font = {'size'   : 15}

plt.rc('font', **font)



t = np.linspace(0,18,100)

plt.plot(t,t, lw=5)
plt.plot(t,2*t, lw=5)
plt.xlim([0,18])
plt.ylim([0,18])
plt.xticks([9,18], ['10 minutes', '20 minutes'])
plt.yticks([9,18], ['9 miles', '18 miles'])
#plt.xlabel("Time (minutes)")
#plt.ylabel("Distance (miles)")
fig = plt.gcf()
fig.set_size_inches(7, 3)
plt.tight_layout()
plt.savefig("linear_graph2.png", dpi=300)