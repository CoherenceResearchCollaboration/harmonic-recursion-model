import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.stats import zscore

# Output folder
output_dir = "hrm_phase_portrait"
os.makedirs(output_dir, exist_ok=True)

# HRM Constants
phi = (1 + np.sqrt(5)) / 2
alpha = 1 / 137.035999084
M0 = 2.2374e-26
epsilon = 1e-20

# HRM Recursive Functions
def Q(n): return 1 / ((n + 1.01)**2 * (1.01)**3)
def S(n): return 1 - np.exp(-np.sqrt(n) / (phi * alpha))
def B(n): return 1 + np.exp(-(n - 62)**2 / (2 * 5**2))
def Sigma(n): return np.sin(n / alpha)**2 * (1 - np.exp(-(n - 62) / 15)) if n >= 62 else 0

def M(n):  # Recursive memory coherence (mass)
    return M0 * (1 + alpha * n) * (np.log(n + 1) / (phi * n)) * np.sin(n / phi) * Q(n) * S(n) * B(n) * Sigma(n)

def r_n(n): return np.tanh(n / phi) * np.exp(-n / (2 * alpha))
def omega(n): return np.abs(np.sin(n / phi) / (r_n(n) + epsilon))

# Recursion steps to analyze
n_vals = np.arange(1, 501)
n_min = n_vals[0]
n_max = n_vals[-1]
mass_vals = np.array([M(n) for n in n_vals])
omega_vals = np.array([omega(n) for n in n_vals])

# Detect statistical outliers using z-score
z_mass = zscore(mass_vals)
z_omega = zscore(omega_vals)
outliers = (np.abs(z_mass) > 2.5) | (np.abs(z_omega) > 2.5)
outlier_steps = n_vals[outliers]

# Plot the phase portrait with outliers
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(mass_vals, omega_vals, 'o-', color='mediumslateblue', label='HRM Trajectory')
ax.plot(mass_vals[outliers], omega_vals[outliers], 'ro', markersize=8, label='Outliers')
ax.set_xlabel("Mass M(n)", fontsize=12)
ax.set_ylabel("Angular Velocity ω(n)", fontsize=12)
plt.title(f"HRM Phase Portrait (Recursive Identity Space) | n = {n_min}–{n_max}")
ax.grid(True)
ax.legend()

# Save the plot
plot_path = os.path.join(output_dir, f"hrm_phase_portrait_n{n_min}-n{n_max}.png")
plt.savefig(plot_path, dpi=300, bbox_inches='tight')
plt.close()

# Print the steps that were identified as outliers
print("📍 Outlier Steps:", outlier_steps)
print("✅ Image saved to:", plot_path)
