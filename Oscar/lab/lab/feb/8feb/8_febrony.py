import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc

c = -(1 + np.pi/2)

def f(x, c):
	return (x + c)*np.arctan(x)

x = np.linspace(-10, 10, 999)


fig=plt.figure
fig, ax = plt.subplots()

plt.plot(x,f(x,c),color='magenta')

#ASINTOTAS OBLICUAS

plt.plot([0,10],[-(np.pi**2)/4+c,5*np.pi-(np.pi**2)/4+c], color='pink')
plt.plot([0,-10],[(1/4)*(-4+2*np.pi**2)+c,5*np.pi*(1/4)*(-4+2*np.pi**2)/4+c], color='pink')
plt.axis('equal') #para poner los ejes iguales 

plt.plot(1/c,f(1/c,c), 'wo') # punto de inflexion

#LABELS EN EL EJE HORIZONTAL
ax.set_xticks([-c, 1/c,5,10])
ax.set_xticklabels(['-c', '1/c', '5', '10'])
plt.show()
