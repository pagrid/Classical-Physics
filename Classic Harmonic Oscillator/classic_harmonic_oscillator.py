# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Harmonic Oscillator Simulation
------------------------------
Author: Petros Agridos
Description:
This script simulates the motion of a simple, damped, and driven harmonic oscillator.
It compares numerical integration methods (Euler, Runge–Kutta 4th order, and SciPy’s solve_ivp),
analyzes the oscillator’s energy, and provides an interactive visualization using ipywidgets.
"""

# =============================================
#  Import Required Libraries
# =============================================
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# =============================================
#  Define the Differential Equation
# =============================================
def harmonic_oscillator(t, y, omega):
    """
    Simple harmonic oscillator:
        x'' + ω²x = 0

    Parameters
    ----------
    t : float
        Time variable
    y : list
        [x, v] = [displacement, velocity]
    omega : float
        Angular frequency

    Returns
    -------
    dydt : list
        [dx/dt, dv/dt]
    """
    x, v = y
    dxdt = v
    dvdt = -omega**2 * x
    return [dxdt, dvdt]


# =============================================
#  Numerical Methods
# =============================================

def euler_method(func, t_eval, y0, omega):
    """Simple Euler integration method."""
    dt = t_eval[1] - t_eval[0]
    y = np.zeros((len(t_eval), len(y0)))
    y[0] = y0

    for i in range(1, len(t_eval)):
        y[i] = y[i - 1] + dt * np.array(func(t_eval[i - 1], y[i - 1], omega))

    return y


def runge_kutta_method(func, t_eval, y0, omega):
    """Classical 4th-order Runge–Kutta integration."""
    dt = t_eval[1] - t_eval[0]
    y = np.zeros((len(t_eval), len(y0)))
    y[0] = y0

    for i in range(1, len(t_eval)):
        t = t_eval[i - 1]
        k1 = np.array(func(t, y[i - 1], omega))
        k2 = np.array(func(t + dt / 2, y[i - 1] + dt * k1 / 2, omega))
        k3 = np.array(func(t + dt / 2, y[i - 1] + dt * k2 / 2, omega))
        k4 = np.array(func(t + dt, y[i - 1] + dt * k3, omega))
        y[i] = y[i - 1] + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return y


# =============================================
#  Simulation Parameters
# =============================================
omega = 2 * np.pi      # Natural frequency (rad/s)
x0, v0 = 1.0, 0.0      # Initial conditions
t_span = (0, 10)       # Simulation time range
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # Time points

# =============================================
#  Solve the Simple Harmonic Oscillator
# =============================================
solution = solve_ivp(harmonic_oscillator, t_span, [x0, v0], args=(omega,), t_eval=t_eval)
euler_solution = euler_method(harmonic_oscillator, t_eval, [x0, v0], omega)
rk4_solution = runge_kutta_method(harmonic_oscillator, t_eval, [x0, v0], omega)

# Extract results
scipy_x = solution.y[0]
euler_x = euler_solution[:, 0]
rk4_x = rk4_solution[:, 0]

# =============================================
#  Plot Comparison of Numerical Methods
# =============================================
plt.figure(figsize=(10, 6))
plt.plot(t_eval, euler_x, label="Euler Method", linestyle='dotted')
plt.plot(t_eval, rk4_x, label="Runge–Kutta 4th Order")
plt.plot(t_eval, scipy_x, label="SciPy solve_ivp", linestyle='dashed')
plt.title("Simple Harmonic Oscillator: Numerical Methods Comparison")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.legend()
plt.grid()
plt.show()


# =============================================
#  Damped and Driven Oscillator
# =============================================
def damped_driven_oscillator(t, y, omega, gamma, F0, omega_d):
    """
    Damped and driven harmonic oscillator:
        x'' + γx' + ω²x = F₀ cos(ω_d t)
    """
    x, v = y
    dxdt = v
    dvdt = -gamma * v - omega**2 * x + F0 * np.cos(omega_d * t)
    return [dxdt, dvdt]


# Parameters for damping and driving
gamma = 0.5
F0 = 0.5
omega_d = 1.5 * omega

solution_dd = solve_ivp(
    damped_driven_oscillator, t_span, [x0, v0],
    args=(omega, gamma, F0, omega_d), t_eval=t_eval
)

# =============================================
#  Energy Analysis
# =============================================
m = 1.0
k = omega**2 * m
displacement = solution_dd.y[0]
velocity = solution_dd.y[1]

KE = 0.5 * m * velocity**2
PE = 0.5 * k * displacement**2
total_energy = KE + PE

# =============================================
#  Plot Displacement and Energies
# =============================================
plt.figure(figsize=(10, 6))
plt.plot(t_eval, displacement, label="Damped Driven Oscillator")
plt.title("Damped Driven Harmonic Oscillator")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(t_eval, KE, label="Kinetic Energy")
plt.plot(t_eval, PE, label="Potential Energy")
plt.plot(t_eval, total_energy, label="Total Energy", linestyle='dashed')
plt.title("Energy of the Damped Driven Oscillator")
plt.xlabel("Time (s)")
plt.ylabel("Energy (J)")
plt.legend()
plt.grid()
plt.show()


# =============================================
#  Interactive Visualization
# =============================================
from ipywidgets import interact, FloatSlider

def interactive_plot(gamma, F0, omega_d):
    """Interactive visualization for varying damping and driving force."""
    sol = solve_ivp(damped_driven_oscillator, t_span, [x0, v0],
                    args=(omega, gamma, F0, omega_d), t_eval=t_eval)
    plt.figure(figsize=(10, 6))
    plt.plot(t_eval, sol.y[0], label=f"γ={gamma}, F₀={F0}, ω_d={omega_d:.2f}")
    plt.title("Interactive Damped Driven Harmonic Oscillator")
    plt.xlabel("Time (s)")
    plt.ylabel("Displacement (m)")
    plt.legend()
    plt.grid()
    plt.show()

# Run interactive visualization (for Jupyter Notebook)
interact(
    interactive_plot,
    gamma=FloatSlider(min=0, max=1, step=0.1, value=0.5),
    F0=FloatSlider(min=0, max=1, step=0.1, value=0.5),
    omega_d=FloatSlider(min=0, max=3 * omega, step=0.1, value=1.5 * omega)
)
