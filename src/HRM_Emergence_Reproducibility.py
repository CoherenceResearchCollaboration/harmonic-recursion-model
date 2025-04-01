import os
import matplotlib.pyplot as plt
import numpy as np
from mpmath import mp, mpf, log, sqrt, sin, pi, exp
import csv

mp.dps = 50

# Constants
n_c = 62
phi = (1 + sqrt(5)) / 2
alpha = 1 / (3.4 * pi * phi**2)
eta = 1 / (2 * phi**2 * alpha)
M0 = mpf("2.2374e-26")
r_HRM = mpf("5.2946e-11")
E_empirical = mpf("2.18e-18")

# HRM Filter Functions
def Q(n): return mpf('1') / ((n + mpf('1.01'))**2)
def S(n): return 1 - exp(-sqrt(n) / (phi * alpha))
def B(n): return 1 + exp(-((n - n_c)**2) / (2 * mpf('5')**2))
def Sigma(n): return 1 if n < n_c else 1 + (sin(n / alpha))**2 * (1 - exp(-(n - n_c) / mpf('15')))
def A(n): return M0 * (1 + alpha * n) * log(n + 1) / (phi * n) * sin(n / phi)
def M(n): return A(n) * Q(n) * S(n) * B(n) * Sigma(n)

def omega(E, M, r): return sqrt(E / (M * r**2) * eta).real
def f(w): return w / (2 * pi)
def T(n): return B(n) * Sigma(n)

def E_calc(M, r, w): return M * r**2 * w**2 / eta

# Analysis range
n_vals = list(range(1, 101))
n_start = n_vals[0]
n_end = n_vals[-1]
mass_vals = []
energy_vals = []
freq_vals = []
b_vals = []
sigma_vals = []
tuning_vals = []
mass_sum = mpf("0")

for n in n_vals:
    m_n = M(n)
    mass_sum += m_n
    w_n = omega(E_empirical, mass_sum, r_HRM)
    e_n = E_calc(mass_sum, r_HRM, w_n)
    mass_vals.append(float(mass_sum))
    energy_vals.append(float(e_n.real))
    freq_vals.append(float(f(w_n)))
    b_vals.append(float(B(n)))
    sigma_vals.append(float(Sigma(n)))
    tuning_vals.append(float(T(n)))

# Normalize all for plotting
normalize = lambda x: [v / max(x) for v in x]

mass_vals_norm = normalize(mass_vals)
energy_vals_norm = normalize(energy_vals)
freq_vals_norm = normalize(freq_vals)
b_vals_norm = normalize(b_vals)
sigma_vals_norm = normalize(sigma_vals)
tuning_vals_norm = normalize(tuning_vals)

# Output folder
output_dir = "HRM_Emergence_Reproducibility"
os.makedirs(output_dir, exist_ok=True)

# Plot
plt.figure(figsize=(12, 7))
plt.plot(n_vals, mass_vals_norm, label="Mass M(n)", color='red')
plt.plot(n_vals, energy_vals_norm, label="Energy E(n)", color='blue')
plt.plot(n_vals, freq_vals_norm, label="Spin Frequency f(n)", color='green')
plt.plot(n_vals, b_vals_norm, label="Bifurcation Boost B(n)", color='violet')
plt.plot(n_vals, sigma_vals_norm, label="Spin Amplification Σ(n)", linestyle='--', color='orange')
plt.plot(n_vals, tuning_vals_norm, label="Recursive Tuning Profile T(n)", color='black')

plt.xlabel("Recursion Depth n")
plt.ylabel("Relative Magnitude")
plt.title(f"HRM Emergence Signals | n = {n_start}–{n_end}")
plt.legend()
plt.grid(True)

plot_path = os.path.join(output_dir, f"emergence_convergence_plot_n{n_start}-n{n_end}.png")
plt.savefig(plot_path, dpi=300)
plt.close()
print(f"Plot saved to {plot_path}")

# Save CSV data
csv_path = os.path.join(output_dir, "emergence_signals.csv")
with open(csv_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["n", "Mass M(n)", "Energy E(n)", "Spin f(n)", "B(n)", "Sigma(n)", "Tuning T(n)"])
    for i, n in enumerate(n_vals):
        writer.writerow([
            n,
            mass_vals[i],
            energy_vals[i],
            freq_vals[i],
            b_vals[i],
            sigma_vals[i],
            tuning_vals[i]
        ])
print(f"CSV saved to {csv_path}")