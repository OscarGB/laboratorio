import numpy as np	
from random import randint
import matplotlib.pyplot as plt
import scipy.special as spc



def x(t):
	return g(t)*np.cos(t)

def y(t):
	return g(t)*np.sin(t)


#definimos la tangente
def g(t):
	return t/(t-1)


#t=np.linspace(-100,0,1000)
#t1=np.linspace(2,100,1000)


t=np.linspace((-1)*1e2,1-1e-2,1000)
t1=np.linspace(1+1e-2,1e2,1000)



fig=plt.figure()

plt.plot(x(t), y(t), color = 'magenta')
plt.plot(x(t1), y(t1), color = 'black')

#plt.plot([-5,20],[g(-5),g(20)],color='blue')


plt.axis('equal')
plt.axis([-5,5,-5,5])



plt.show()

