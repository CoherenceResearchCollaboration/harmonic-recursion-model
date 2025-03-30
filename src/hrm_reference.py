from mpmath import mp, mpf, sin, log
import matplotlib.pyplot as plt
from hrm_config import M0, phi, alpha

# Recursive coherence amplitude function A(n)
def A(n):
    return M0 * (1 + alpha * n) * log(n + 1) / (phi**n) * sin(n * phi)

# Simulation runner
def main():
    mp.dps = 100  # high precision
    ns = list(range(1, 101))
    amplitudes = [A(n) for n in ns]

    # Convert mpmath floats to native floats for plotting
    y = [float(a) for a in amplitudes]

    plt.plot(ns, y)
    plt.title("HRM Recursive Coherence Amplitude A(n)")
    plt.xlabel("Recursion Depth (n)")
    plt.ylabel("Amplitude A(n)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
