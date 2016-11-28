import numpy as np	
from random import randint
import matplotlib.pyplot as plt
import scipy.special as spc


def f(u):
	return 1.-4.*u+2.*u**2.+u**3.



fig=plt.figure()
plt.plot(0,0,'ro')

#NIVEL0

plt.plot([-3,3],[-3*((np.sqrt(13)-3)/2),3*((np.sqrt(13)-3)/2)], color = 'r') #intervalo 3 antes de b
plt.plot([-3,3],[-3*((-np.sqrt(13)-3)/2),3*((-np.sqrt(13)-3)/2)], color = 'r')
plt.plot([-3,3],[-3,3], color = 'r')


#NIVEL1


#antes de b
u3=np.linspace(-2000.,((-3.-np.sqrt(13))/2.)-1e-8,10000)
plt.plot(1./(spc.cbrt(f(u3))),u3/(spc.cbrt(f(u3))), color = 'k')

#despues de 1
u0=np.linspace(1.+1e-8,2000,10000)
plt.plot(1./(spc.cbrt(f(u0))),u0/(spc.cbrt(f(u0))), color = 'magenta')


plt.plot(0,1,'ro')
#entre a y 1
u1=np.linspace(((-3.+np.sqrt(13))/2.)+1e-5,1.-1e-8,1000)
plt.plot(1./(spc.cbrt(f(u1))),u1/(spc.cbrt(f(u1))), color = 'blue')


#entre a y b
u2=np.linspace(((-3.-np.sqrt(13))/2.)+1e-8,((-3.+np.sqrt(13))/2.)-1e-8,1000)
plt.plot(1./(spc.cbrt(f(u2))),u2/(spc.cbrt(f(u2))), color = 'k')


plt.xlim(-3, 3)
plt.ylim(-3,3)

plt.show()
