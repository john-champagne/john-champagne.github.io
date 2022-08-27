import numpy as np
import matplotlib.pyplot as plt
import tempfile
import pickle

T = tempfile.SpooledTemporaryFile()
plt.ioff()
font = {'size'   : 15}

plt.rc('font', **font)



t = np.linspace(0,16,1000)
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

def fname(ind):
    s = str(ind)
    s = "0"*(3-len(s)) + s + ".png"
    return s

def draw_line_at(t_to_draw):
    dt = 0.01
    slope = np.interp([t_to_draw-dt/2,t_to_draw+dt/2], t, d)
    slope = (slope[1]-slope[0])/dt
    plt.plot([0,16], [np.interp(t_to_draw, t, d)+slope*(0-t_to_draw), np.interp(t_to_draw, t, d)+slope*(16-t_to_draw)], 'r--', lw=2, alpha = 0.5)

frame = 0
def save_frame():
    global frame
    plt.savefig(fname(frame), dpi=300)
    frame = frame + 1
    
t1 = 2.954955
t2 = 13.44545

ts_to_draw = np.linspace(0.1,15.9,300)

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
    plt.text(8, 4.5, "{} mph".format(int(np.round(slope*60.0, decimals=0))), backgroundcolor=(1,1,1,1))
    
    if t_to_draw > t1:
        draw_line_at(t1)
    if t_to_draw > t2:
        draw_line_at(t2)
    
    
    fig = plt.gcf()
    fig.set_size_inches(7, 3)
    plt.tight_layout()
    save_frame()
    if t_to_draw > t1 and ts_to_draw[ind-1] < t1:
        for i in range(10):
            save_frame()
    if t_to_draw > t2 and ts_to_draw[ind-1] < t2:
        for i in range(10):
            save_frame()
    if t_to_draw == ts_to_draw[-1]:
        for i in range(30*3):
            save_frame()
    if ind == 0:
        for i in range(30):
            save_frame()
    plt.close()