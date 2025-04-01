# Reproducibility Summary (Appendices C–E)

This document summarizes the reproducible elements of the Harmonic Recursion Model (HRM) as described in Appendices C, D, and E of the original paper. These equations and outputs are verified using the Python scripts found in `/core/`. No external constants (beyond $\pi$ and $\phi$) are required.

---

## Core Emergent Quantities
From a single seed parameter $M_0$, you can reproduce:

| Quantity         | Output                          | Accuracy vs Empirical | Where Proven           |
|------------------|----------------------------------|------------------------|------------------------|
| Proton Mass      | $M_{\text{lock}} \approx 1.6726 \times 10^{-27}$ kg | $<0.01\%$                | Theorem 3.2           |
| Bohr Radius      | $r \approx 5.29 \times 10^{-11}$ m           | $<0.1\%$                 | Theorem 3.6           |
| Binding Energy   | $E \approx 2.18 \times 10^{-18}$ J           | $\sim 1\%$ (after $\eta$)  | Theorem 3.4           |
| Fine-Structure $\alpha$ | $\alpha \approx 1/137.2$ (emergent)    | $\sim 0.2\%$               | Theorem 3.4           |
| Planck Constant  | $h_{\text{HRM}} = E/f \approx 3.9 \times 10^{-33}$ J\cdot s | Within 1 order of magnitude | Theorem 3.4, 3.5      |
| Spectral Lines   | $\Delta n = 5$ harmonic emissions | $<1\%$ (H-$\alpha$ through H-$\delta$) | Theorem 3.7  |
| Spin Frequency   | $f \approx 5.55 \times 10^{14}$ Hz | $<1\%$                | Theorem 3.6           |

---

## Required Environment
- Python 3.8+
- `mpmath` for arbitrary precision
- Recursion depth $n \geq 1000$
- Precision $\geq$ 50 decimal digits

Install with:
```bash
pip install -r requirements.txt
```

---

## Recommended Scripts
| Script | Purpose |
|--------|---------|
| `hrm_identity_generator.py` | Compute mass, energy, frequency, and $h_{\text{HRM}}$ |
| `hrm_phase_tracker.py` | Analyze identity stability, spin, and persistence |
| `hrm_emission_analysis.py` | Detect harmonic emissions ($\Delta n = 5$) |
| `hrm_maxwell_visualizer.py` | Visualize HRM analogues to classical field structure |

---

## Licensing and Attribution
MIT License. If used in academic work, cite:

> Heaton, K. & ChatGPT-4. \textit{The Harmonic Recursion Model: A Generative Framework for Mass, Light, and the Emergence of Physical Law} (2025)

---

## Integrity Note
Do not attempt to simplify, truncate, or linearize the equations. HRM relies on recursive depth, phase interference, and filter convergence. Null attractors and incoherence are expected if fidelity is broken.

All successful reproductions must use the equations in Appendix C, with full filtering and coherence structure preserved.