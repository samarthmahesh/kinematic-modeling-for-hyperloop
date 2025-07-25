import matplotlib.pyplot as plt
import numpy as np

# If our pod is going at 'u' speed, and there is 's' meters before there is a kid on the track, how much deceleration 
# must be done? So my 'a' - decceleration will be dependent var, and u and s will be independent.
# using v^2 - u^2 = 2as, we get v = 0, since pod shud stop, final vel = 0
# therefore, a = -u^2/(2s)
u_values = np.linspace(25, 300, 3000)
s_values = np.linspace(100,500, 1000)  # Adjust resistance range as needed

# Create a 3D meshgrid
u, s = np.meshgrid(u_values, s_values)

a = -u**2/(2*s)

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(u,s,a, cmap='viridis', alpha=0.7)

# Set labels and title
ax.set_xlabel('cruise vel (m/s)')
ax.set_ylabel('\n\n\ndistance before crash (m)')
ax.set_zlabel('required decceleration (m/s^2)')
ax.set_title('Crash eqn a = -u^2/2s')

plt.show()