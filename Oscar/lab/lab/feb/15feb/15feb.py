import numpy as np	
from random import randint
import matplotlib.pyplot as plt
import scipy.special as spc



def x(t):
	return t**2-2*t

def y(t):
	return 1./(t**2)+t**2


#definimos la tangente
def g(x):
	return 4.*x+6


t=np.linspace(-5,20,1000)
t1=np.linspace(-10,-1,1000)

fig=plt.figure()

plt.plot(x(t), y(t), color = 'magenta')
plt.plot(x(t1), y(t1), color = 'magenta')

plt.plot([-5,20],[g(-5),g(20)],color='blue')


plt.axis('equal')
plt.axis([-5,20,-5,20])

#plt.xlim(-5,20)
#plt.ylim(-5,20)

plt.show()

