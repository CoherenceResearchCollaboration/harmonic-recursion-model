# hrm_emission_analysis.py
# Detects spectral spike structure and estimates Planck's constant
# Based on Δω(n)^2 torsion metrics

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Parameters
input_csv = "hrm_recursion_dynamics/phase_metrics.csv"
output_dir = "hrm_recursion_dynamics"
zoom_range = (40, 100)
threshold_factor = 1.2  # spike threshold: % above local median

# Load data
df = pd.read_csv(input_csv)
n = df["n"].values
domega_sq = df["Δω²"].values
phase = df["phase"].values
omega = df["omega"].values
mass = df["M_total"].astype(float).values

# Limit to zoom region
mask = (n >= zoom_range[0]) & (n <= zoom_range[1])
n_zoom = n[mask]
domega_zoom = domega_sq[mask]

# Compute dynamic threshold
local_median = np.median(domega_zoom)
threshold = local_median * threshold_factor

# Detect spikes
spike_indices = np.where(domega_zoom > threshold)[0]
spike_n = n_zoom[spike_indices]
spike_f = np.array([float(omega[i]) / (2 * np.pi) for i in spike_indices])
spike_E = np.full_like(spike_f, 2.18e-18)  # use empirical hydrogen E
spike_h = spike_E / spike_f  # E = h f

# Save spike data
spike_csv = os.path.join(output_dir, "spike_candidates.csv")
pd.DataFrame({
    "n": spike_n,
    "frequency_Hz": spike_f,
    "estimated_h": spike_h
}).to_csv(spike_csv, index=False)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(n_zoom, domega_zoom, color='orange', label="Δω(n)²")
plt.axhline(threshold, color='red', linestyle='--', label=f"Threshold ({threshold_factor}× median)")
for depth in [62, 57, 52, 47, 42]:
    if zoom_range[0] <= depth <= zoom_range[1]:
        plt.axvline(depth, color='blue', linestyle=':', label=f"Δn = 5 marker" if depth == 62 else "")
for s in spike_n:
    plt.axvline(s, color='black', linestyle='--', alpha=0.3)
plt.xlabel("Recursion Depth n")
plt.ylabel("Δω(n)²")
plt.title("Zoomed Emission Spike Scan (n = 40–100)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "emission_spike_zoom.png"), dpi=300)
plt.close()

print(f"Analysis complete. Spikes written to '{spike_csv}' and plot saved.")