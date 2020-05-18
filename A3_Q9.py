import numpy as np
import matplotlib.pyplot as plt

a=-5
b=5
h=0.02
n=int((b-a)/h+1)
x=np.linspace(a,b,n)
t=np.linspace(a,b,n)

def y(x):
    if abs(x)<=1:
        return 1
    else:
        return 0
f=np.zeros(n)   #function array of f
g=np.zeros(n)   #function array of g
fg=np.zeros(n)  #function array of f*g
for i in range(n): # function f
    f[i]=y(x[i])
print(f)


for j in range(n):
    fg[j]=0
    for k in range(n):
        dt=h
        g[k]=y(x[j]-t[k])   #function g
        fg[j]=fg[j]+f[k]*g[k]*dt    #fg= sum of f(x)*g(x-t)dt for x=x[j]

print(fg)
plt.plot(x,f,'--r',label='f(x)')
plt.plot(x,fg,'--b',label='f(x)*f(x-t)')
plt.grid(True)
plt.legend()
plt.minorticks_on()
plt.grid(which='minor', linewidth='0.2')
plt.show()
