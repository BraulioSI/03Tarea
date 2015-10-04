from math import *
from scipy import integrate as int
from scipy import optimize 
import pyfits #modulo para leer archivos fits
import matplotlib.pyplot as p #modulo para graficar
import numpy #este modulo es para trabajar con matrices como en matlab
import matplotlib as mp
#mp.rcParams['xtick.labelsize']=13
#mp.rcParams['ytick.labelsize']=13


mu=1.977
N=numpy.power(10,6)
b=20*pi
h=b/N

s=numpy.linspace(0,b,N+1)
y=numpy.zeros(N+1)
v=numpy.zeros(N+1)

y[0]=4
v[0]=0

def f(x,z):
    return (-x - (mu*(numpy.power(x,2)-1)*z))

for i in range(N):
    k1=h*v[i]
    l1=h*f(y[i],v[i])
    k2=h*(v[i]+ l1/2)
    l2=h*f(y[i]+k1/2,v[i]+l1/2)
    k3=h*(v[i]-l1+2*l2)
    l3=h*f(y[i]-k1+2*k2, v[i]-l1+2*l2)
    y[i+1]=y[i]+ (k1+k3+4*k2)/6
    v[i+1]=v[i]+ (l1+l3+4*l2)/6











p.plot(s,y)
#p.plot(y,v)
#p.plot(k,y, label='Altura')
#p.xlabel('Numero de choque')
#p.ylabel('Velocidad')
#p.legend(loc='upper right')
#p.title('Velocidad despues de cada choque')
p.grid()
p.show()



