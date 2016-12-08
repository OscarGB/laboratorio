import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

t1=numpy.arange(0.1, 5, 1e-3)
t2=numpy.arange(-5,-0.1,1e-3)
coso=numpy.arange(-5,5,1e-3)

def x(t):
  return (t*t-2*t)

def y(t):
  return (1/(t*t)+t*t)
  
def asin(coso):
  return (4*(coso+1)+2)


plt.plot(x(t1), y(t1), color='blue')
plt.plot(x(t2), y(t2), color='blue')
plt.plot(coso,asin(coso))

plt.show()