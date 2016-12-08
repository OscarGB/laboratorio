import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

R=1;

t=numpy.arange(-numpy.pi, numpy.pi, 1e-3);
aux=numpy.arange(-numpy.pi,numpy.pi,0.01);
t1=numpy.arange(-2*numpy.pi, 0, 1e-3);
m=numpy.arange(0,20,0.1)

fig=plt.figure(figsize=(10,10));
ax=plt.axes(xlim=(-5,5), ylim=(-5, 5));

line,=ax.plot([],[], linewidth=1, color='red');
otra,=ax.plot([],[], linewidth=1, color='green');

def x(t):
  return R*(t-numpy.sin(t));
def y(t):
  return -R*(1-numpy.cos(t));

def s(a,b):
    return xx(a)+yy(b)

#plt.plot(x(t),y(t))
plt.plot(x(t1)+numpy.pi,y(t1)-2, 'g')

for i in aux:
    h=plt.plot(x(t),y(t),'b')
    g=plt.plot(x(i),y(i), 'ro')
    plt.pause(0.0001)
    g.pop(0).remove()
    h.pop(0).remove()

def init():
    line.set_data([],[]);
    #otra.set_data([],[]);
    return line;

def animate(j):
    #line.set_data(x(aux), y(aux))
    #otra.set_data()
    return line;

anim=animation.FuncAnimation(fig, animate, init_func=init, frames=len(t), interval=1, blit=False, repeat=False);

plt.show();

plt.close(fig);
