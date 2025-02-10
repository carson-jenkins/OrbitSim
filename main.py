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
TIME_STEP = 1  # Increment per step (seconds)
SIM_DURATION = 10800  # Full simulation time (seconds)
ITERATIONS = int(SIM_DURATION / TIME_STEP)

# Compute gravitational acceleration
def compute_gravity(pos):
    dist = np.linalg.norm(pos)
    return -GRAVITY_CONST * EARTH_MASS * pos / dist**3

# Storage for trajectory plotting
x_data, y_data = [], []

# Runge-Kutta 4th order method for numerical integration
for _ in range(ITERATIONS):
    dv1 = compute_gravity(coords) * TIME_STEP
    dp1 = speed * TIME_STEP
    
    dv2 = compute_gravity(coords + 0.5 * dp1) * TIME_STEP
    dp2 = (speed + 0.5 * dv1) * TIME_STEP
    
    dv3 = compute_gravity(coords + 0.5 * dp2) * TIME_STEP
    dp3 = (speed + 0.5 * dv2) * TIME_STEP
    
    dv4 = compute_gravity(coords + dp3) * TIME_STEP
    dp4 = (speed + dv3) * TIME_STEP
    
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
