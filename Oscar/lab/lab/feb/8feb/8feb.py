#trazar la grafica de y, las asintotas y el punto de inflexion
#Los dos ejes tienen que tener la misma escala, y hay que dar
# valores entre -5 y 20 en la vertical

import numpy as np	
from random import randint
import matplotlib.pyplot as plt
import scipy.special as spc



def f(x):
	return (x-np.pi/2.-1)*np.arctan(x)



fig=plt.figure()
plt.plot(0,0,'ro')

x=np.linspace(-15,15,100)

plt.plot(x, f(x), color = 'magenta')


#asintotas oblicuas
plt.plot([0,10],[,],color='blue')
plt.plot([0,-10],[,],color='blue')


plt.axis('equal')
#plt.xlim(-15, 20)
#plt.ylim(-5,20)

plt.show()
