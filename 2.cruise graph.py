import matplotlib.pyplot as plt
import numpy as np

# If our pod has reached 'v' cruise speed after accelearation, and there is 't' time before i need to start 
# deccelerating, how much distance will i have covered during my cruising period? 
# So my 'd' - distance of cruise will be dependent var, and v and t will be independent.
# using d = vt
v_values = np.linspace(25, 300, 3000)
t_values = np.linspace(1800, 7200, 7000)  # Adjust resistance range as needed

# Create a 3D meshgrid
v, t = np.meshgrid(v_values, t_values)

# Calculate energy values
d = v*t

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(v,t,d, cmap='viridis', alpha=0.7)

# Set labels and title
ax.set_xlabel('cruise velocity we have attained (m/s)')
ax.set_ylabel('time for which we\'ll cruise (s)')
ax.set_zlabel('\n\n\ndistance we\'ll cover before attaining cruise speed (m)')
ax.set_title('Cruise eqn v = dt')

plt.show()