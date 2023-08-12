import matplotlib.pyplot as plt
import numpy as np

r=1
pitch=1
n_turns=5
theta_max=n_turns*2*np.pi

theta=np.linspace(0,theta_max,1000)
x=r*np.cos(theta)
y=r*np.sin(theta)
z=pitch*theta/(2*np.pi)

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
plt.plot(x,y,z)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.show()
