import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

t1=numpy.arange(0, 2*numpy.pi, 1e-3)
t2=numpy.arange(-2*numpy.pi, 0, 1e-3)
R=2

def apos(t):
  return R*numpy.cos(t/2)

def aneg(t):
  return -R*numpy.cos(t/2)


ax=plt.axes(xlim=(-20,20), ylim=(-20,20))
ax.set_aspect('equal')

plt.plot(t1, apos(t1), color='blue')
plt.plot(t2, aneg(t2), color='green')

plt.show()
