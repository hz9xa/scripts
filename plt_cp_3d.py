from mpl_toolkits.mplot3d import axes3d,Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np


file = open("output.txt",'r')
file_content = file.readlines()
data=file_content[2:]

fig = plt.figure()
#ax = fig.gca(projection='3d')
ax = Axes3D(fig)
X = np.arange(0, 256, 1)
Y = np.arange(0, 256, 1)
X, Y = np.meshgrid(X, Y)
#R = np.sqrt(X**2 + Y**2)
#Z = np.sin(R)
Z = np.fromstring(data[0],dtype=float,sep=' ')
for row in data[1:]:
    Z = np.vstack((Z,np.fromstring(row,dtype=float,sep=' ')))
print(Z.shape)
print(Z)
print(Z.max())
print(Z.min())
zmax=Z.max()
zmin=Z.min()
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.hot,
        linewidth=0, antialiased=False)
ax.set_zlim3d(int(zmin-10),int(zmax+10))
#ax.view_init(elev=5,azim=45)
#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

