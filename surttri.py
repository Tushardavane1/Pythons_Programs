import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.tri import Triangulation
n=50
theta=np.linspace(0,2*np.pi,n,endpoint=False)
radii=np.linspace(0.5,1.0,n)
r,th=np.meshgrid(radii,theta)


x=r*np.cos(th)
y=r*np.sin(th)
z=r*np.sin(6*r)/(r+0.3)
tri=Triangulation(x.flatten(),y.flatten())

fig=plt.figure()

ax=fig.add_subplot(111,projection='3d')
ax.plot_trisurf(tri,z.flatten(),cmap='viridis')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.show()