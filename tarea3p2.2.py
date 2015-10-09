from math import *
from scipy import integrate as int
from scipy import optimize
from scipy.integrate import ode
import pyfits #modulo para leer archivos fits
import matplotlib.pyplot as p #modulo para graficar
import numpy as n #este modulo es para trabajar con matrices como en matlab
import matplotlib as mp
from mpl_toolkits.mplot3d import Axes3D


sigma=10.0
beta=8.0/3
rho=28.0
N=n.power(10,5)
b=55.0
h=b/N

t=n.zeros(N+1)
x=n.zeros(N+1)
y=n.zeros(N+1)
z=n.zeros(N+1)

u0=[1.0, 2.0, -1.0]

#def funcion sistema de ecuaciones

def f(t, u):
    return [sigma*(u[1]-u[0]), u[0]*(rho-u[2])-u[1], u[0]*u[1] - beta*u[2]]

#rutina dopri5

r=ode(f).set_integrator('dopri5')

r.set_initial_value(u0, 0)


i=0

#implementacion metodo

while r.successful() and r.t<=b and i<=N:
    r.integrate(r.t+h)
    t[i]=r.t
    x[i]=r.y[0]
    y[i]=r.y[1]
    z[i]=r.y[2]
    i+=1
    



fig = p.figure(1)
fig.clf()

ax = fig.add_subplot(111, projection='3d')
ax.set_aspect('equal')

ax.plot(x,y,z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

p.show()





