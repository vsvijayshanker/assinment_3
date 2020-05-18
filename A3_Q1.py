import numpy as np
import matplotlib.pyplot as plt

ax=-10  #left bound of x space
bx=10   #right bound of x space
hx=0.1     
nx=int((bx-ax)/hx+1)
x=np.linspace(ax,bx,nx)
print(x)

ak=-5   #left bound of k space
bk=5    #right bound of k space
hk=0.1
nk=int(1+(bk-ak)/hk)
k=np.linspace(ak,bk,nk)
print(k)

def f(x): #defining the function
    return np.sin(x)/x

y=np.zeros(nx)  #Actual function array
for i in range(nx):
    if x[i]==0:
        y[i]=1
    else:
        y[i]=f(x[i])
print(y)

ft=np.zeros(nk) #fourier transform array
for i in range(nk):
    ft[i]=0
    for p in range(nx):
        ft[i]=ft[i]+hx*y[p]*np.exp(1.j*k[i]*x[p])/((2*np.pi)**0.5)
print(ft)

plt.plot(x,y,'b', label='Actual Function',)
plt.plot(k,ft,'r', label='Fourier Transform')
plt.grid(True)
plt.legend()
plt.minorticks_on()
plt.grid(which='minor',linewidth='0.2')
plt.show()


