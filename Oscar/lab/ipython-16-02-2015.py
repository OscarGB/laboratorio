import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

t=numpy.arange(-2*numpy.pi, 2*numpy.pi, 1e-3)
R=3

def x(t):
  return R*(t-numpy.sin(t))

def y(t):
  return -R*(1-numpy.cos(t))

fig=plt.figure(figsize=(8,8))
plt.axes(xlim=(-20,20), ylim=(-20,20))
plt.plot(x(t), y(t), color='blue')

plt.show()
