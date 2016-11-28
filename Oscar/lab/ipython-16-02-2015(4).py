import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

R=2

ax=plt.axes(xlim=(-20,20), ylim=(-20,20))
ax.set_aspect('equal')

plt.plot((0,8*R),(R*(1-(0/(4*R))),R*(1-(8*R/(4*R)))))
plt.plot((-8*R,0),(-R*(1+(-8*R/(4*R))),-R*(1+(0/(4*R)))))

plt.show()
