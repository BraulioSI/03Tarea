from math import *
from scipy import integrate as int
from scipy import optimize 
import pyfits #modulo para leer archivos fits
import matplotlib.pyplot as p #modulo para graficar
import numpy as n #este modulo es para trabajar con matrices como en matlab
import matplotlib as mp


mu=1.977
N=n.power(10,6)  #numero de intervalos de integracion
b=20*pi          #extremo final de integracion
h=b/N            #paso de integracion

s=n.linspace(0,b,N+1)   #vector s (abscisas)
y=n.zeros(N+1)          #vector y
v=n.zeros(N+1)          #vector v=dy/ds

y[0]=4.0    #condiciones iniciales
v[0]=0.0

def f(x,z):   #funcion del sistema de EDO's
    return (-x - (mu*(n.power(x,2)-1)*z))

for i in range(N):   #RK3
    k1=h*v[i]
    l1=h*f(y[i],v[i])
    k2=h*(v[i]+ l1/2)
    l2=h*f(y[i]+k1/2,v[i]+l1/2)
    k3=h*(v[i]-l1+2*l2)
    l3=h*f(y[i]-k1+2*k2, v[i]-l1+2*l2)
    y[i+1]=y[i]+ (k1+k3+4*k2)/6
    v[i+1]=v[i]+ (l1+l3+4*l2)/6









#Dependiendo de la pregunta, se selecciona alguno de los 2 graficos

#p.plot(s,y)
#p.plot(y,v)
#p.xlabel('y(s)')
#p.ylabel('dy/ds')

#p.title('Espacio de fases')
#p.grid()
#p.show()



