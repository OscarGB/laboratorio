import numpy as np
import matplotlib.pyplot as plt
import scipy.special as scp

def p(t):
	return 2 * np.cos(t)

def x(t):
	return p(t)*np.cos(t)

def y(t):
	return p(t)*np.sin(t)

def reflejo(k):
	return 2*k - (np.pi/2.)


in1=np.linspace(0 + 1e-3,np.pi - 1e-3,1e3)

pts=np.linspace(0 + 1e-3,np.pi - 1e-3,150)


#p1= dar valores
p2= np.pi/6
#p3=
#p4=
#q1=
q2= reflejo(p2)
#q3=
#q4=

fig=plt.figure()

plt.plot(x(in1),y(in1),'magenta')
#plt.plot([x(3*(np.pi/4.)),x(reflejo(3*(np.pi/4.)))],[y(3*(np.pi/4.)),y(reflejo(3*(np.pi/4.)))],'blue')
plt.plot([x(pts),x(reflejo(pts))],[y(pts),y(reflejo(pts))],'magenta')
plt.plot(((x(reflejo(pts)) - x(pts))/2.)+x(pts),((y(reflejo(pts)) - 
y(pts))/2.)+y(pts), 'ro')


plt.axis('equal')

plt.show()

