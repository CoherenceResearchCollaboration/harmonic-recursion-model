# HRM Emergence Reproducibility Script

This script (`HRM_Emergence_Reproducibility.py`) visualizes the convergence of mass, energy, spin, and coherence filters during hydrogen identity formation. It offers a high-resolution view from $n = 1$ to $n = 100$, showing the complete pre-lock-in ramp, tuning structure, and post-lock-in coherence behavior.

---

## What This Script Shows

This script generates a labeled plot showing the recursive behavior of:

- Mass accumulation $M(n)$
- Recursive energy $E(n)$
- Spin frequency $f(n)$
- Bifurcation tension $B(n)$
- Spin amplification $\Sigma(n)$
- Recursive tuning profile $T(n) = B(n) \cdot \Sigma(n)$

These observables collectively support Theorems 3.2 through 3.6 and demonstrate the recursive landscape leading to identity lock-in.

---

## Key Transitions and Lock-in Points

- **Tuning Onset:** $n \approx 59$  
- **Lock-in (Identity Stabilization):** $n = 62$  
- **Post-lock Oscillations:** Visible in $\Sigma(n)$ and $T(n)$

This range illustrates not just identity formation, but the **emergent harmonic readiness for emission** beyond lock-in.

---

## Usage

Run the script from the root of the repository:

```bash
python src/HRM_Emergence_Reproducibility.py

Outputs:

HRM_Emergence_Reproducibility/emergence_convergence_plot.png

HRM_Emergence_Reproducibility/emergence_signals.csv

Interpretive Note

This script is intended for scientific verification. It uses only the canonical HRM equations (Appendix C) and contains no fitted parameters. The quantities shown are emergent and reproducible using a single seed $M_0$.

No constants are assumed except $\pi$ and $\phi$. All other results — including $\alpha$, $h$, and emission structure — arise from recursive coherence.

Suggested Interpretation

The tuning profile $T(n)$ does not produce a spike — it produces a structured ramp and resonance arc. This distinguishes HRM from impulsive models of identity formation and highlights the role of recursive geometry in preparing coherence for retention and eventual emission.

---


