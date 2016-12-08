from mpl_toolkits.mplot3d import Axes3D
import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

X=numpy.arange(-1, 1,0.1)
Y=numpy.arange(0,1,0.1)
X, Y = numpy.meshgrid(X, Y)
Z=X*X*X-4*X*X*Y+2*X*Y*Y+Y*Y*Y

fig = plt.figure()
ax =fig.gca(projection='3d')
surf=ax.plot_surface(X,Y,Z,rstride=1, cstride=1, cmap='hot', linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
plt.contour(X,Y,Z,0)

plt.show()
