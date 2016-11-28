import numpy as np	
from random import randint
import matplotlib.pyplot as plt
import scipy.special as spc


def x(t):
	return (np.sin(t)*np.cos(t))/(2*np.cos(t)-1)

def y(t):
	return (np.sin(t)*np.sin(t))/(2*np.cos(t)-1)


t=np.linspace(-np.pi/3+0.001, np.pi/3-0.001, 10000)
t1=np.linspace(np.pi/3+0.001, 5*np.pi/3-0.001,  10000)


fig=plt.figure()

plt.plot(x(t), y(t), color = 'magenta')
plt.plot(x(t1), y(t1), color = 'lime')


plt.xlim(-2,2)
plt.ylim(-2,2)


plt.show()

