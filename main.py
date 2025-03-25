import numpy as np
import matplotlib.pyplot as plt

# Universal constants
GRAVITY_CONST = 6.67430e-11  # Newton's gravitational constant (Nm^2/kg^2)
EARTH_MASS = 5.972e24  # Earth's mass in kg
SATELLITE_MASS = 1000  # Satellite's mass in kg
INITIAL_RADIUS = 6.771e6  # Initial orbital radius (m)

# Starting conditions
coords = np.array([INITIAL_RADIUS, 0])  # (x, y) coordinate initialization
speed = np.array([0, np.sqrt(GRAVITY_CONST * EARTH_MASS / INITIAL_RADIUS)])  # Circular orbit velocity

# Simulation details
time_step = 1  # Increment per step (seconds)
sim_duration = 10800  # Full simulation time (seconds)
iterations = int(sim_duration / time_step)

# Compute gravitational acceleration
def compute_gravity(pos):
    dist = np.linalg.norm(pos)
    return -GRAVITY_CONST * EARTH_MASS * pos / dist**3

# Storage for trajectory plotting
x_data, y_data = [], []

# Runge-Kutta 4th order method for numerical integration
for _ in range(iterations):
    dv1 = compute_gravity(coords) * time_step
    dp1 = speed * time_step
    
    dv2 = compute_gravity(coords + 0.5 * dp1) * time_step
    dp2 = (speed + 0.5 * dv1) * time_step
    
    dv3 = compute_gravity(coords + 0.5 * dp2) * time_step
    dp3 = (speed + 0.5 * dv2) * time_step
    
    dv4 = compute_gravity(coords + dp3) * time_step
    dp4 = (speed + dv3) * time_step
    
    speed += (dv1 + 2*dv2 + 2*dv3 + dv4) / 6
    coords += (dp1 + 2*dp2 + 2*dp3 + dp4) / 6
    
    x_data.append(coords[0])
    y_data.append(coords[1])

# Generate orbit visualization
plt.figure(figsize=(8, 8))
plt.plot(x_data, y_data, label='Orbital Path')
plt.plot(0, 0, 'ro', label='Earth')  # Earth's fixed position
plt.xlabel('X Coordinate (m)')
plt.ylabel('Y Coordinate (m)')
plt.title('Satellite Trajectory Simulation')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
