import os
import csv
import matplotlib.pyplot as plt
import numpy as np
from mpmath import mp, mpf, sqrt, log, sin, pi, exp

mp.dps = 50

# Constants and recursive parameters
n_c = 62
phi = (1 + sqrt(5)) / 2
alpha = 1 / (3.4 * pi * phi**2)
eta = 1 / (2 * phi**2 * alpha)
M0 = mpf("2.2374e-26")
r_HRM = mpf("5.2946e-11")
E_empirical = mpf("2.18e-18")

# Filter functions
def Q(n): return mpf('1') / ((n + mpf('1.01'))**2)
def S(n): return 1 - exp(-sqrt(n) / (phi * alpha))
def B(n): return 1 + exp(-((n - n_c)**2) / (2 * mpf('5')**2))
def Sigma(n): return 1 if n < n_c else 1 + (sin(n / alpha))**2 * (1 - exp(-(n - n_c) / mpf('15')))
def A(n): return M0 * (1 + alpha * n) * log(n + 1) / (phi * n) * sin(n / phi)
def M(n): return A(n) * Q(n) * S(n) * B(n) * Sigma(n)

# Recursion and phase computation
N = 1000
n_vals = list(range(1, N + 1))
mass_sum = mpf('0')
mass_list = []
omega_list = []
phase_list = []

dt = mpf('1')

for n in n_vals:
    m_n = M(n)
    mass_sum += m_n
    omega = sqrt(E_empirical / (mass_sum * r_HRM**2) * eta)
    omega_list.append(omega)
    phase = omega * dt if n == 1 else phase_list[-1] + omega * dt
    phase_list.append(phase)
    mass_list.append(mass_sum)

# Emission metric
omega_floats = [float(w) for w in omega_list]
domega_sq_list = [abs(omega_floats[i]**2 - omega_floats[i+1]**2) for i in range(len(omega_floats)-1)]
domega_sq_list.append(0.0)

# Zoom range for plotting
zoom_start = 20
zoom_end = 80

n_zoom = n_vals[zoom_start:zoom_end]
omega_zoom = omega_floats[zoom_start:zoom_end]
domega_zoom = domega_sq_list[zoom_start:zoom_end]

# Plotting
output_dir = "hrm_phase_tracker"
os.makedirs(output_dir, exist_ok=True)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

ax1.plot(n_zoom, omega_zoom, label="Angular Velocity ω(n)", color='slateblue')
ax1.axvline(n_c, color='red', linestyle='--', label="Lock-in depth")
ax1.axvline(59, color='black', linestyle=':', label="Tuning spike (n = 59)")
ax1.set_ylabel("\u03c9(n)")
ax1.legend()
ax1.grid(True)

ax2.plot(n_zoom, domega_zoom, label="Emission Spike Metric Δω²", color='darkorange')
ax2.set_xlabel("Recursion Depth n")
ax2.set_ylabel("Δω(n)²")
ax2.grid(True)
ax2.legend()

plt.suptitle("Recursive Angular Velocity and Emission Spikes | n = 20–80")
plt.tight_layout()

plot_path = os.path.join(output_dir, f"phase_convergence_and_spikes_n{zoom_start}-n{zoom_end}.png")
plt.savefig(plot_path, dpi=300)
plt.close()

print(f"Plot saved to {plot_path}")

# CSV Export
csv_path = os.path.join(output_dir, f"phase_metrics_n{zoom_start}-n{zoom_end}.csv")
with open(csv_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["n", "omega(n)", "delta_omega(n)^2"])
    for i, n in enumerate(n_zoom):
        writer.writerow([n, omega_zoom[i], domega_zoom[i]])

print(f"CSV saved to {csv_path}")
