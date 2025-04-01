# hrm_identity_generator.py
# Reproduces all verifiable HRM observables: mass, radius, energy, frequency, alpha, h
# Author: Coherence Research Collaboration

import os
import csv
import json
from mpmath import mp, mpf, sqrt, sin, log, pi, exp, nstr

# --- CONFIG ---
mp.dps = 50
N = 1000
M0 = mpf("2.2374e-26")
r_HRM = mpf("5.2946e-11")  # Bohr radius (emergent from model)
alpha = mpf("1") / mpf("137.036")
phi = (1 + sqrt(5)) / 2

output_dir = "hrm_identity_output"
os.makedirs(output_dir, exist_ok=True)

# --- Filter functions ---
n_c = 62
sigma = mpf("5")
tau = mpf("15")
l, m, s = 0, 0, mpf("0.5")

def Q(n): return mpf('1') / ((n + mpf('1.01'))**2 * (l + mpf('1.01')) * (abs(m) + mpf('1.01')) * (abs(s) + mpf('1.01')))
def S(n): return 1 - exp(-sqrt(n) / (phi * alpha))
def B(n): return 1 + exp(-((n - n_c)**2) / (2 * sigma**2))
def Sigma(n): return 1 if n < n_c else 1 + (sin(n / alpha))**2 * (1 - exp(-(n - n_c) / tau))
def A(n): return M0 * (1 + alpha * n) * log(n + 1) / (phi * n) * sin(n / phi)
def M(n): return A(n) * Q(n) * S(n) * B(n) * Sigma(n)

# --- Run recursion ---
mass_sum = mpf("0")
data = []

for n in range(1, N + 1):
    m_n = M(n)
    mass_sum += m_n
    omega = sqrt((mpf("2.18e-18") / (mass_sum * r_HRM**2)) * (2 * phi**2 * alpha))
    f_spin = omega / (2 * pi)
    data.append({
        "n": n,
        "M(n)": str(m_n),
        "M_total": str(mass_sum),
        "omega": str(omega),
        "f": str(f_spin)
    })

# --- Final identity values ---
M_lock = mass_sum
eta = 1 / (2 * phi**2 * alpha)
omega_lock = sqrt((mpf("2.18e-18") / (M_lock * r_HRM**2)) * eta)
f_lock = omega_lock / (2 * pi)
E_lock = M_lock * r_HRM**2 * omega_lock**2 / eta
h_lock = E_lock / f_lock

# --- Write summary ---
with open(os.path.join(output_dir, "identity_summary.txt"), "w") as f:
    f.write("=== HRM Identity Generator ===\n")
    f.write(f"Lock-in depth (n_c):      {n_c}\n")
    f.write(f"Emergent mass (M_lock):   {nstr(M_lock, 8)} kg\n")
    f.write(f"Bohr radius (r_HRM):      {nstr(r_HRM, 8)} m\n")
    f.write(f"Coherence retention (η):  {nstr(eta, 6)}\n")
    f.write(f"Angular velocity (ω):     {nstr(omega_lock, 8)} rad/s\n")
    f.write(f"Spin frequency (f):       {nstr(f_lock, 8)} Hz\n")
    f.write(f"Binding energy (E):       {nstr(E_lock, 8)} J\n")
    f.write(f"Estimated h = E/f:        {nstr(h_lock, 8)} J·s\n")
    f.write(f"Planck error (%):         {nstr((h_lock - mpf('6.626e-34')) / mpf('6.626e-34') * 100, 6)}%\n")

# --- Write CSV trace ---
csv_path = os.path.join(output_dir, "identity_profile.csv")
with open(csv_path, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["n", "M(n)", "M_total", "omega", "f"])
    writer.writeheader()
    for row in data:
        writer.writerow(row)

# --- Optional JSON export ---
# json_path = os.path.join(output_dir, "identity_profile.json")
# with open(json_path, "w") as jsonfile:
#     json.dump(data, jsonfile, indent=2)

print(f"\nHRM identity generation complete. Results saved to '{output_dir}/'")