import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

p1=numpy.arange(-200, -3.29, 1e-3)
p2=numpy.arange(-3.31, 0.29, 1e-3)
p3=numpy.arange(0.31, 0.99, 1e-3)
p4=numpy.arange(1.01, 2000, 1e-3)

def f(p):
  return 1-4*p+2*p*p+p*p*p

def x(p):
  return 1/(f(p)**(1./3.));

def y(p):
  return p/(f(p)**(1./3.));

def ymenos(p):
  return p/(-(numpy.abs(f(p))**(1./3.)));

def xmenos(p):
  return 1/(-(numpy.abs(f(p))**(1./3.)));

ax=plt.axes(xlim=(-10,10),ylim=(-10,10))
plt.plot(xmenos(p1), ymenos(p1), color='red')
plt.plot(x(p2), y(p2), color='red')
plt.plot(x(p3), y(p3), color='red')
plt.plot(x(p4), y(p4), color='red')
plt.plot([-5,5],[0,0], color='black')
plt.plot([0,0],[-5,5], color='black')
plt.plot([-5,5],[-5*(-3.3),5*(-3.3)], color='blue')
plt.plot([-5,5],[-5*(0.3),5*0.3], color='blue')
plt.plot([-5,5],[-5,5], color='blue')


plt.show()
