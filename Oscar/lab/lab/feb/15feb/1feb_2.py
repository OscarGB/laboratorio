import numpy as np	
from random import randint
import matplotlib.pyplot as plt


fig=plt.figure()

plt.plot(0,0,'ro')

plt.plot([-3,3],[-3*((np.sqrt(13)-3)/2),3*((np.sqrt(13)-3)/2)], color = 'r') #intervalo 3 antes de b
plt.plot([-3,3],[-3*((-np.sqrt(13)-3)/2),3*((-np.sqrt(13)-3)/2)], color = 'r')
plt.plot([-3,3],[-3,3], color = 'k')

plt.xlim(-3, 3)
plt.ylim(-3,3)

plt.show() 
