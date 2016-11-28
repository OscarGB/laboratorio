import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

teta0=numpy.arange(-2*numpy.pi, 0, 1e-3)
teta1=numpy.arange(0, 0.99, 1e-3)
teta2=numpy.arange(1.01, 2*numpy.pi, 1e-3)
teta3=numpy.arange(2*numpy.pi, 4*numpy.pi, 1e-3)

ax=plt.axes(xlim=(-50,50), ylim=(-50,50))
def ro(teta):
  return teta/(teta-1);

def x(teta):
  return ro(teta)*numpy.cos(teta);

def y(teta):
  return ro(teta)*numpy.sin(teta);

plt.plot(x(teta1),y(teta1))
plt.plot(x(teta2),y(teta2))
plt.plot(x(teta0),y(teta0))
plt.plot(x(teta3),y(teta3))

plt.show()
