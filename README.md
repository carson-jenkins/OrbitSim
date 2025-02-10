# OrbitSim

OrbitSim is a Python-based application that models and visualizes satellite motion in space. It calculates trajectories using gravitational interactions and allows users to simulate additional orbital disturbances for a more dynamic representation.

## Features

- 2D Orbit Simulation: Models satellite motion around Earth
- Visual Trajectory Representation: Generates graphical plots of orbital paths
- Perturbation Effects: Option to include J2 perturbation (Earth's oblateness)
- Accurate Numerical Integration: Uses the Runge-Kutta 4th order method for precision.

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