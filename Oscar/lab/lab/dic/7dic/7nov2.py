import numpy as np
import matplotlib.pyplot as plt
from random import randint


def f(x, y0, x0):
	return 1.0*np.log(np.e**y0+x**2-x0**2)

fig=plt.figure()
x= np.linspace(0, 10, 100)


for i in range (-5, 6):
	plt.plot(x, f(x,i, 0))

for j in range (-5, 6):
	d= (np.e**(-5)-1+j**2)**(1/2)
	a=np.arange(d, 10,1e-2)
	plt.plot(a, f(a,0, j))


plt.show()
