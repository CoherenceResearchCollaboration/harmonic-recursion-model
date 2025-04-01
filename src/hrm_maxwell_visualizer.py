# hrm_visualizer.py
# Recursive phase-space visualization inspired by HRM Maxwell analogies

import numpy as np
import matplotlib.pyplot as plt
import os

# Create output directory
output_dir = "hrm_maxwell_output"
os.makedirs(output_dir, exist_ok=True)

# === Common Grid ===
x = np.linspace(-10, 10, 800)
y = np.linspace(-10, 10, 800)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
theta = np.arctan2(Y, X)

# === Field Normalization ===
def normalize_field(f):
    f_min, f_max = np.min(f), np.max(f)
    return (f - f_min) / (f_max - f_min)

# === Panel 1: Gauss Analogy ===
def render_gauss_analogy(save=True):
    core = np.exp(-R**2 / 2.5)
    spiral = np.sin(3 * theta + R) * np.exp(-0.3 * R)
    field = normalize_field(core + 0.4 * spiral)

    plt.imshow(field, cmap="magma", extent=[-10, 10, -10, 10])
    plt.title("Recursive Curvature Memory (Gauss Analogy)")
    plt.axis("off")
    if save:
        plt.savefig(f"{output_dir}/panel_1_gauss.png", dpi=300, bbox_inches='tight')
        plt.close()

# === Panel 2: Ampère Analogy ===
def render_ampere_analogy(save=True):
    lobe = np.cos(5 * R - 2.5 * np.cos(2 * theta)) * np.exp(-0.2 * R)
    center = np.exp(-R**2 / 3.5)
    echo = np.sin(4 * R - 3 * theta) * np.exp(-0.05 * R)
    field = normalize_field(center + 0.5 * lobe + 0.4 * echo)

    plt.imshow(field, cmap="plasma", extent=[-10, 10, -10, 10])
    plt.title("Recursive Feedback Amplification (Ampère Analogy)")
    plt.axis("off")
    if save:
        plt.savefig(f"{output_dir}/panel_2_ampere.png", dpi=300, bbox_inches='tight')
        plt.close()

# === Panel 3: Faraday Analogy ===
def render_faraday_analogy(save=True):
    core = np.exp(-R**2 / 2.8)
    twist = np.sin(4 * theta + 1.5 * R) * np.exp(-0.2 * R)
    glow = np.exp(-0.1 * (R - 6)**2) * (1 + 0.3 * np.cos(2 * theta))
    burst = np.sin(3 * R - 0.5 * theta) * np.exp(-0.3 * (R - 5)**2)
    field = normalize_field(core + 0.5 * twist + 0.7 * glow + 0.4 * burst)

    plt.imshow(field, cmap="inferno", extent=[-10, 10, -10, 10])
    plt.title("Recursive Phase Twist & Photon Emission (Faraday Analogy)")
    plt.axis("off")
    if save:
        plt.savefig(f"{output_dir}/panel_3_faraday.png", dpi=300, bbox_inches='tight')
        plt.close()

# === Panel 4: No Monopole Analogy ===
def render_no_monopole_analogy(save=True):
    core = np.exp(-R**2 / 3.0)
    spin_memory = np.sin(6 * theta - 1.5 * R) * np.exp(-0.2 * R)
    echo = np.exp(-0.12 * (R - 4.5)**2) * (1 + 0.3 * np.cos(3 * theta))
    field = normalize_field(core + 0.5 * spin_memory + 0.5 * echo)

    plt.imshow(field, cmap="viridis", extent=[-10, 10, -10, 10])
    plt.title("Recursive Closure & Memory (No Monopole Analogy)")
    plt.axis("off")
    if save:
        plt.savefig(f"{output_dir}/panel_4_nomono.png", dpi=300, bbox_inches='tight')
        plt.close()

# === Optional: Generate All Panels ===
def generate_all_panels():
    render_gauss_analogy()
    render_ampere_analogy()
    render_faraday_analogy()
    render_no_monopole_analogy()
    print(f"All HRM panels rendered and saved to '{output_dir}/'.")

# Run when executed as script
if __name__ == "__main__":
    generate_all_panels()
