import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

ax=-10  #left bound of x space
bx=10   #right bound of x space
hx=0.1     
nx=int((bx-ax)/hx+1)
x=np.linspace(ax,bx,nx)
print(x)

ay=-3  #left bound of y space
by=3   #right bound of y space
hy=0.1     
ny=int((by-ay)/hy+1)
y=np.linspace(ay,by,ny)
print(y)

akx=-5   #left bound of kx space
bkx=5    #right bound of kx space
hkx=0.1
nkx=int(1+(bkx-akx)/hkx)
kx=np.linspace(akx,bkx,nkx)
print(kx)

aky=-3   #left bound of ky space
bky=3    #right bound of ky space
hky=0.1
nky=int(1+(bky-aky)/hky)
ky=np.linspace(aky,bky,nky)
print(ky)

def f(x,y):
    return np.exp(-(x**2+y**2))


for p in range(nx):
    for q in range(ny):
        z=np.zeros(ny)
        z[q]=f(x[p],y[q])
        fig=plt.figure()
        ax=plt.axes(projection='3d')
        ax.plot3D(x,y,z)
        print('z is',z)

fig=plt.figure()
ax=plt.axes(projection='3d')

ax.plot3D(x,y,z)

plt.grid(True)
plt.legend()
plt.minorticks_on()
plt.grid(which='minor',linewidth='0.2')
plt.show()


