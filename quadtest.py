import numpy as np
from scipy.stats import qmc

import matplotlib.pyplot as plt

def f(x, y):
    """Function to integrate: max(x+y, 0)"""
    return np.maximum(x + y-1/np.pi, 0)

def sobol_quadrature(N):
    """
    Compute Sobol quadrature for max(x+y, 0) over [0,1]^2
    Returns the integral approximation
    """
    sampler = qmc.Sobol(d=2, seed=None)
    points = sampler.random(N)
    x, y = points[:, 0], points[:, 1]
    integral = np.mean(f(x, y))
    return integral

# Exact integral: ∫∫ max(x+y, 0) dx dy over [0,1]^2 = 2/3
exact_value = 0.6870653023894314

# Test convergence for different N values
N_values = np.logspace(1, 6, 20, dtype=int)
errors = []

for N in N_values:
    approx = sobol_quadrature(N)
    error = np.abs(approx - exact_value)
    errors.append(error)

print(approx)

errors = np.array(errors)

# Plot convergence rate
plt.figure(figsize=(10, 6))
plt.loglog(N_values, errors, 'b-o', label='Error', linewidth=2, markersize=6)
plt.loglog(N_values, 1/N_values, 'r--', label='$O(1/N)$', linewidth=2)
plt.loglog(N_values, 1/np.sqrt(N_values), 'g--', label='$O(1/\sqrt{N})$', linewidth=2)
plt.xlabel('Number of quadrature points (N)', fontsize=12)
plt.ylabel('Absolute error', fontsize=12)
plt.title('Sobol Quadrature Convergence: max(x+y, 0) over [0,1]²', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, which='both', alpha=0.3)
plt.tight_layout()
plt.show()

print(f"Exact integral: {exact_value:.6f}")
print(f"Approximation (N=10000): {sobol_quadrature(10000):.6f}")