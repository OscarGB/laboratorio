import numpy as np
import matplotlib.pyplot as plt
from random import randint
import math
import scipy.special as sp

C=range(-5,6)

def f(x, C):
	return np.exp(x**2)*(C+(np.sqrt(np.pi)/2)*sp.erf(x));


x=np.linspace(-3,3,100)
fig = plt.figure()



for i in range(len(C)):
	plt.plot(x, f(x, C[i]))
	i+=1

plt.ylim(-15,15)
plt.title('FUNCION ERROR', color = 'magenta')

plt.show() 


