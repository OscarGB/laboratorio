import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


a=-numpy.pi/2-1

x=numpy.arange(-10, 15, 1e-3)

def curva(x):
  return ((x+a)*numpy.arctan(x))

def asint(x):
  return (numpy.pi/2)*x-1+a*numpy.pi/2
  
def asint2(x):
  return (-numpy.pi/2)*x-1-a*numpy.pi/2

plt.plot(x, curva(x))
plt.plot(x, asint(x))
plt.plot(x, asint2(x))

plt.show()