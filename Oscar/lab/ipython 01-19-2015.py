import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

T=5
t=numpy.arange(-5,T,1e-3)

delta=numpy.arange(1,-0.1,-0.1)
s=numpy.arange(-1,1,1e-3)

t0=0

def x(t):
  return ((t*t)+t)/2

def y(t):
  return ((t*t)-t)/2

f, (ax1, ax2) = plt.subplots(1, 2)
ax1.set_aspect(aspect='equal')
ax2.set_aspect(aspect='equal')
ax1.set_xlim(-1,1); ax1.set_ylim(-1,1);
ax2.set_xlim(-1,1); ax2.set_ylim(-1,1);

ax2.arrow(0, 0, -0.5, 0.5, head_width=0.05, head_length=0.1, fc='k', ec='k')
ax2.arrow(0, 0, 0.5, -0.5, head_width=0.05, head_length=0.1, fc='k', ec='k')
ax1.arrow(0, 0, -0.5, 0.5, head_width=0.05, head_length=0.1, fc='k', ec='k')
ax1.arrow(0, 0, 0.5, -0.5, head_width=0.05, head_length=0.1, fc='k', ec='k')

ax1.plot((x(t0+s)-x(t0)), (y(t0+s)-y(t0)), '--', linewidth=1, color='red')

for d in delta:
  g=ax1.plot((x(t0+d*s)-x(t0)), (y(t0+d*s)-y(t0)), linewidth=1, color='red')
  ax2.plot(x(t0-d*s)/d-x(t0)/d, y(t0-d*s)/d-y(t0)/d, linewidth=1, color='red')
  plt.pause(1)
  g.pop(0).remove()

plt.show()

plt.close(f)
