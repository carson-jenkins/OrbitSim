# OrbitSim

OrbitSim is a Python-based application that models and visualizes satellite motion in a 2D plane. It calculates orbital trajectories using Newtonian gravity and numerically integrates the equations of motion with the Runge-Kutta 4th order method.

## Features

- 2D Orbital Simulation: Models the motion of a satellite around Earth assuming a circular starting orbit
- Visual Trajectory Representation: Generates a graphical plot of the satellite’s orbital path
- Accurate Numerical Integration: Uses the Runge-Kutta 4th order method to compute position and velocity updates
- Customizable Parameters: Modify initial conditions, simulation time, and time step for different scenarios

## Installation

Ensure you have Python installed, then clone the repository and install dependencies:

```bash
git clone https://github.com/carson-jenkins/OrbitSim.git
cd OrbitSim
pip install numpy matplotlib scipy
```

## Usage
Run the simulation by executing the following command:

```
python main.py
```

## Notes

The default setup models a satellite in low Earth orbit with an initial circular trajectory.
