import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

t=numpy.arange(-numpy.pi, numpy.pi, 1e-3)
t1=numpy.arange(0, numpy.pi, 1e-3)
t2=numpy.arange(-numpy.pi, 0, 1e-3)
R=1

def x(t):
  return R*(t-numpy.sin(t))

def y(t):
  return -R*(1-numpy.cos(t))

def spos(t):
  return 4*R*(1-numpy.cos(t/2))

def sneg(t):
  return -4*R*(1-numpy.cos(t/2))

fig=plt.axes(xlim=(-4,4), ylim=(-4,0.5))
ax.set_aspect('equal')

line1,=ax.plot([],[],linewidth=3,color='red')
line2,=ax.plot([],[],linewidth=3,color='red')

def init():
  line1.set_data([],[])
  line2.set_data([],[])
  return line

plt.plot(x(t), y(t), color='blue')
plt.plot(x(t), y(t), color='green')

def animate(j):
  line1.set_data(t1,spos(t1), color='red')
  line2.set_data(t2,sneg(t2), color='red')
  return line

anim=animation.FuncAnimation(fig,animate,init_func=init,frames=len(t),interval=1,blit=False,repeat=False)

plt.show()

plt.close(fig)


plt.show()
