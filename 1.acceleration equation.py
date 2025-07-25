import matplotlib.pyplot as plt
import numpy as np

# If our pod has to reach 'v' speed, and there is 's' meters before before i reach that v, how much acceleration 
# must be done? So my 'a' - acceleration will be dependent var, and v and s will be independent.
# using v^2 - u^2 = 2as, we get u = 0, since pod is at rest initially.
# therefore, a = v^2/(2s)
v_values = np.linspace(25, 300, 3000)
s_values = np.linspace(100,500, 1000)  # Adjust resistance range as needed

# Create a 3D meshgrid
v, s = np.meshgrid(v_values, s_values)

# Calculate energy values
a = v**2/(2*s)

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(v,s,a, cmap='viridis', alpha=0.7)

# Set labels and title
ax.set_xlabel('cruise velocity to attain (m/s)')
ax.set_ylabel('\n\n\ndistance covered before\n attaining cruise speed (m)')
ax.set_zlabel('required acceleration (m/s^2)')

plt.show()