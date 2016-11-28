import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

p=numpy.arange(-4, 4, 1e-3)

def f(p):
  return 1-4*p+2*p*p+p*p*p

ax=plt.axes(xlim=(-5,5),ylim=(-5,5))
plt.plot(p, f(p))
plt.plot([-5,5],[0,0], color='black')
plt.plot([0,0],[-5,5], color='black')
plt.plot([-5,5],[-5*(-3.3),5*(-3.3)])
plt.plot([-5,5],[-5*(0.3),5*0.3])
plt.plot([-5,5],[-5,5])


plt.show()
