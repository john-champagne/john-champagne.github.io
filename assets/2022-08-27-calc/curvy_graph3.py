import numpy as np
import matplotlib.pyplot as plt
import tempfile
import pickle

T = tempfile.SpooledTemporaryFile()

font = {'size'   : 15}

plt.rc('font', **font)



t = np.linspace(0,16,100)
p = 0.4
u = 9
s = 8
a = 1.6
f = 30*np.cos(2*np.pi*t/8+p)+70
w = 1-np.exp(-1*((t-u)/s)**2)
h = w*f*a
d = np.cumsum(h)*t[1]
d = d - d[0]
d = d / d[-1] * 18.0


plt.plot(t,d, lw=5)
plt.plot([t[0],t[-1]],[d[0],d[-1]],'k--',lw=3)
plt.xlim([0,16])
plt.ylim([0,18])
plt.xticks([8,16], ['8 minutes', '16 minutes'])
plt.yticks([9,18], ['9 miles', '18 miles'])

pickle.dump(plt.gcf(), T)
plt.close()
plt.ioff()

ts_to_draw = np.linspace(0.1,16,3)
for ind,t_to_draw in enumerate(ts_to_draw):
    T.seek(0)
    figx = pickle.load(T)
    figx.show()    
    # Draw a tangent line
    dt = 0.01
    slope = np.interp([t_to_draw-dt/2,t_to_draw+dt/2], t, d)
    slope = (slope[1]-slope[0])/dt
    # Draw dot
    plt.plot([t_to_draw], [np.interp(t_to_draw, t, d)], 'ro', ms=10)
    
    # Draw line
    plt.plot([0,16], [np.interp(t_to_draw, t, d)+slope*(0-t_to_draw), np.interp(t_to_draw, t, d)+slope*(16-t_to_draw)], 'r--', lw=2)
    plt.text(8, 4.5, "100 mph")
    
    fig = plt.gcf()
    fig.set_size_inches(7, 3)
    plt.tight_layout()
    plt.savefig(__file__.split("\\")[-1].replace(".py","{}.png".format(ind)), dpi=300)