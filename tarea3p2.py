from math import *
from scipy import integrate as int
from scipy import optimize 
import pyfits #modulo para leer archivos fits
import matplotlib.pyplot as p #modulo para graficar
import numpy #este modulo es para trabajar con matrices como en matlab
import matplotlib as mp
from mpl_toolkits.mplot3d import Axes3D
#mp.rcParams['xtick.labelsize']=13
#mp.rcParams['ytick.labelsize']=13


sigma=10
beta=8/3
rho=28
N=numpy.power(10,5)
b=20*pi
h=b/N

t=numpy.linspace(0,b,N+1)
x=numpy.zeros(N+1)
y=numpy.zeros(N+1)
z=numpy.zeros(N+1)

x[0]=6
y[0]=0
z[0]=-5

def f1(x,y):
    return sigma*(y-x)

def f2(x,y,z):
    return x*(rho-z)-y

def f3(x,y,z):
    return x*y - beta*z

for i in range(N):
    k1=h*f1(x[i],y[i])
    l1=h*f2(x[i],y[i],z[i])
    m1=h*f3(x[i],y[i],z[i])
    k2=h*f1(x[i]+k1/2,y[i]+l1/2)
    l2=h*f2(x[i]+k1/2,y[i]+l1/2,z[i]+m1/2)
    m2=h*f3(x[i]+k1/2,y[i]+l1/2,z[i]+m1/2)
    k3=h*f1(x[i]+k2/2,y[i]+l2/2)
    l3=h*f2(x[i]+k2/2,y[i]+l2/2,z[i]+m2/2)
    m3=h*f3(x[i]+k2/2,y[i]+l2/2,z[i]+m2/2)
    
    k4=h*f1(x[i]+k3,y[i]+l3)
    l4=h*f2(x[i]+k3,y[i]+l3,z[i]+m3)
    m4=h*f3(x[i]+k3,y[i]+l3,z[i]+m3)
    x[i+1]=x[i]+ (k1+k4+2*(k2+k3))/6
    y[i+1]=y[i]+ (l1+l4+2*(l2+l3))/6
    z[i+1]=z[i]+ (m1+m4+2*(m2+m3))/6




fig = p.figure(1)
fig.clf()

ax = fig.add_subplot(111, projection='3d')
ax.set_aspect('equal')

ax.plot(x,y,z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

p.show()



#p.plot(y,v)
#p.plot(k,y, label='Altura')
#p.xlabel('Numero de choque')
#p.ylabel('Velocidad')
#p.legend(loc='upper right')
#p.title('Velocidad despues de cada choque')
#p.grid()
#p.show()



