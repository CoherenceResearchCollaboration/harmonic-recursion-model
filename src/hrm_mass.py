"""
hrm_mass.py — Harmonic Recursion Model
Generates and plots the recursive mass attractor curve M(n),
showing lock-in of hydrogen identity near n = 62.

Outputs:
- hrm_mass_data.csv — tabulated M(n)
- hrm_mass_plot.png — visual plot of M(n)
"""

from mpmath import mp, mpf, sin, log, exp
import matplotlib.pyplot as plt
import csv
from hrm_config import M0, phi, alpha

# Set global precision for all mpmath operations
mp.dps = 50  # Safe, fast precision. Increase if needed for deeper recursion.

# --- Recursive Components ---

def A(n):
    """Coherence amplitude at recursion depth n."""
    return M0 * (1 + alpha * n) * log(n + 1) / (phi**n) * sin(n * phi)

def Q(n):
    """Phase-lock filter: suppresses early recursion leakage."""
    return 1 - exp(-alpha * n)

def B(n):
    """Bifurcation tension: angular instability driver."""
    return abs(sin(n / phi))

def S(n):
    """Damping factor: softens over-recursion energy."""
    return exp(-alpha * n / 2)

def Sigma(n):
    """Amplification ripple: boosts coherence after lock-in."""
    return 1 + 0.05 * sin(n * phi / 2)

def M(n):
    """Recursive mass profile, composed of A(n) and filters."""
    return A(n) * Q(n) * B(n) * S(n) * Sigma(n)

# --- Main computation and plot routine ---

def main():
    ns = list(range(1, 101))  # Recursion depth steps (n = 1 to 100)
    masses = []

    for n in ns:
        try:
            m = M(n)
            masses.append(float(m))  # Convert mpmath value to float
        except Exception as e:
            print(f"⚠️ Error at n={n}: {e}")
            masses.append(0.0)  # Fallback value on failure

    # --- Plot the attractor curve ---
    plt.plot(ns, masses, label="Recursive Mass M(n)")
    plt.axvline(x=62, color="red", linestyle="--", label="Hydrogen lock-in (n=62)")
    plt.title("HRM Recursive Mass Emergence")
    plt.xlabel("Recursion Depth (n)")
    plt.ylabel("Mass M(n)")
    plt.grid(True)
    plt.legend()

    # --- Save output data ---
    with open("hrm_mass_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "M(n)"])
        for n, m in zip(ns, masses):
            writer.writerow([n, m])

    plt.savefig("hrm_mass_plot.png")
    print("✅ Saved: hrm_mass_data.csv and hrm_mass_plot.png")

    # --- Display the plot (blocks until closed) ---
    plt.show()

# --- Script entry point ---
if __name__ == "__main__":
    main()
