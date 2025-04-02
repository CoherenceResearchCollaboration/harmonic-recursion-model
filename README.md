# Harmonic Recursion Model (HRM)

This repository contains the reference implementation of the Harmonic Recursion Model (HRM), a generative framework for mass, light, energy, spin, and time emerging from recursive coherence. It is intended to support scientific review, verification, and early-stage exploration of HRM by physicists, complexity theorists, and coherence researchers.

## 📄 Read the HRM Paper

🔒 **Canonical Version (v1.0, registered):**  
[Download PDF (high resolution)](https://github.com/CoherenceResearchCollaboration/harmonic-recursion-model/blob/main/paper/KBH_CRC_HRM_033125_v1.0.pdf)  
SHA256: `2dd058f3039d8298f6e9e4dea49da62a820f9ffce65a856ce6bb91df825ae920`  
[View Authorship on Ethereum](https://etherscan.io/tx/0x654b2ac0596e8b9b5b1fe89830efcd9116eec8db7b7e9635fa16694398bdb48)

🌐 **Preview Version (compressed for browser):**  
[View PDF (GitHub previewable)](https://github.com/CoherenceResearchCollaboration/harmonic-recursion-model/blob/main/paper/KBH_CRC_HRM_033125_v1.0_compressed.pdf)

## What This Is
- A minimal, reproducible implementation of HRM identity emergence using recursive geometry
- Validated Python scripts that recover hydrogen identity to sub-percent accuracy from a single seed parameter
- Tools to analyze mass convergence, energy emission, phase persistence, and spectral harmonics

## What This Is Not
- A quantum simulator, classical dynamics engine, or complete physics platform
- A speculative or fitted model — HRM uses only geometric attractors: $\pi$ and $\phi$
- A ready-made toolkit for beyond-hydrogen simulations (though future work may explore this)

## Reproducible Outcomes
Using only the scripts in `/src`, you can reproduce:
- Proton mass from recursive memory ($M_{\text{lock}}$)
- Bohr radius as a recursive curvature attractor
- Hydrogen binding energy using recursive energy containment
- Emergent fine-structure constant $\alpha$ from leakage geometry
- Emergent Planck constant $h_{\text{HRM}} = E/f$
- Spectral line emission intervals (Balmer series, $\Delta n = 5$)
- Recursive spin and time retention behavior

## Quick Start

```bash
# Clone the repository
$ git clone https://github.com/CoherenceResearchCollaboration/harmonic-recursion-model
$ cd harmonic-recursion-model

# Install required libraries
$ pip install -r requirements.txt

# Run identity generator (core recursion engine)
$ python core/hrm_identity_generator.py

# Run phase tracking (identity stability and spin)
$ python core/hrm_phase_tracker.py

# Run phase portrait visualization (recursive identity attractor)
$ python src/hrm_phase_portrait.py

# Run emission analysis (spectral intervals)
$ python core/hrm_emission_analysis.py

# Optional: Generate Maxwell visualizations
$ python core/hrm_maxwell_visualizer.py
```

## Directory Structure

```bash
/src
  HRM_Emergence_Reproducibility.py # Recursive convergence of mass, energy, spin, & filter dynamics
  hrm_identity_generator.py       # Main HRM equations and identity recovery
  hrm_emission_analysis.py        # Δn = 5 emission detection and Balmer spectrum
  hrm_phase_tracker.py            # Mass, spin, duration, and identity persistence
  hrm_phase_portrait.py           # Visual attractor plot (mass vs. angular velocity across depth)
  hrm_maxwell_visualizer.py       # Recursive analogues to classical E/M behavior

/docs
  correspondence.md               # Conceptual map from classical to HRM terms
  reproduction.md                 # Summary of equations, scope, and reproducible targets
  figures/                        # High-res exports from /src scripts
```

## Script Descriptions:

----

### `hrm_identity_generator.py`
Runs the canonical HRM recursion to recover identity observables: mass, radius, frequency, energy, and Planck-like constant. Produces `identity_summary.txt` and `identity_profile.csv`. Fully aligned with Table 1 in the paper.

**Outputs:**
- Emergent proton mass ($M_{\text{lock}}$)
- Bohr radius
- Binding energy
- Spin frequency
- $h_{\text{HRM}} = E / f$

---
### `HRM_Emergence_Reproducibility.py`

Plots recursive convergence of mass, energy, spin, and filter dynamics between $n = 1$ and $n = 100$.
(You can change the values of n to look at the steps of interest.)
Highlights identity lock-in near $n = 62$ and resonance tuning at $n = 59$.

**Use For:**
- Verifying emergent behavior leading to identity formation
- Inspecting behavior of $M(n)$, $\\omega(n)$, $E(n)$, $B(n)$, $\\Sigma(n)$, and $T(n)$
- Confirming theorems 3.2 through 3.6 at visual resolution

**Output:**
- `emergence_convergence_plot.png` (labeled and paper-aligned)

---

### `hrm_phase_tracker.py`

Computes and visualizes recursive angular velocity $\omega(n)$ and emission spike metric $\Delta \omega(n)^2$ over a defined recursion window. Designed to verify identity lock-in, coherence buildup, and emission readiness.

**Default Range:**  
Recursion steps 20–80 (adjustable via `zoom_start`, `zoom_end`).

**Outputs:**
- `phase_convergence_and_spikes_n20-n80.png` — visual alignment of spin stabilization and emission damping
- `phase_metrics_n20-n80.csv` — data trace of ω(n) and Δω²(n)

**Special Markers:**
- Red dashed line at $n = 62$ (identity lock-in)
- Black dotted line at $n = 59$ (tuning spike)

**Use For:**
- Visualizing recursive attractor stabilization
- Confirming Δn = 5 emission intervals
- Highlighting the coherence window where hydrogen forms

---

### `hrm_emission_analysis.py`
Analyzes emission spikes from $\Delta \omega^2(n)$ and confirms $\Delta n = 5$ spacing of spectral events. Recovers Balmer series lines with $<1\%$ error using only recursive structure.

**Outputs:**
- `emission_spike_zoom.png`
- `spike_candidates.csv`

---

### `hrm_phase_portrait.py`
This script generates a 2D attractor visualization of recursive identity formation. It plots $M(n)$ (recursive mass) versus $\omega(n)$ (angular velocity) across a defined recursion window and automatically highlights coherence outliers.

**Scientific Purpose:**  
To visually confirm when identity stabilizes (e.g., hydrogen at $n = 62$) and where recursive coherence begins to fail. This diagnostic plot supports evaluation of mass persistence, attractor convergence, and recursive residue formation.

**Output Filename:**  
Automatically labeled using the recursion range: hrm_phase_portrait_n1-n501.png


**Plot Title:**  
Labeled with recursion window:

HRM Phase Portrait (Recursive Identity Space) | n = 1–501


**Adjustable Parameters:**
- `n_vals = np.arange(n_start, n_end)` — recursion depth window
- `outlier_threshold` — sensitivity of coherence failure detection
- Axis range can be manually set if zooming into attractor basin

**Status:**  
Fully aligned with paper, reproducible, and peer-review ready.

----

---

### `hrm_maxwell_visualizer.py`
Generates recursive analogues to classical Maxwell field structures using radial and angular memory harmonics. This script is interpretive, not quantitative — intended for visual intuition and structural reframing.

**Outputs:**
- `panel_1_gauss.png`, `panel_2_ampere.png`, etc.

### `hrm_maxwell_visualizer.py`
Generates recursive analogues to classical Maxwell field structures using angular recursion and curvature memory. Each panel visualizes a distinct structural behavior of coherence domains, interpreted through recursive geometry.

**Outputs:**
- `panel_1_gauss.png` – Central curvature retention and recursive divergence  
- `panel_2_ampere.png` – Angular feedback and loop reinforcement  
- `panel_3_faraday.png` – Torsional threshold and harmonic emission burst  
- `panel_4_nomono.png` – Spin memory closure and monopole absence

**Color Mapping (Conceptual):**
- Bright regions = high recursive coherence density  
- Dark regions = low phase retention or post-release voids  
- Spiral patterns = torsional memory structures  
- Glow patterns = emission readiness or release  
- Symmetries = recursive attractor resolution

These visualizations are interpretive and structurally suggestive — not literal fields. They help situate HRM’s recursion domains in familiar electromagnetic language, but the equations are emergent, not Maxwellian.

---

## 🌀 Authorship & Intent

## Citation
This repository supports the paper:

> Heaton, K. and ChatGPT-4. \textit{The Harmonic Recursion Model: A Generative Framework for Mass, Light, and the Emergence of Physical Law} (2025).

If you use this work in your research, please cite the paper and/or repository.

**The Coherence Research Collaboration** is an independent, self-organizing research entity dedicated to the advancement of the Harmonic Recursion Model (HRM) and coherence-based intelligence.

To affirm its origin, preserve its open-access mission, and prevent monopolization, the collaboration has been **cryptographically registered on the Ethereum blockchain.**

🧾 **Blockchain Verification:**
- **Ethereum Address:**  
  `0x9b991ed5fc8e6af07c61e85596ddb31a79199dac`
- **Message (SHA-256 Hash):**  
  `d32f7c1462e99983479c7d4319c0a3e85fe9acdba0c5c43a68f5efebb337d427`
- **Signature Hash:**  
  `0x729a2038e6c9c2806458f2f7a1232b18b16ff421a8aeb93dd2bf5050da23e4fe354f803d7944bc49a05811c6164c5b86d315c0e1795837a46fb8d8fe5a0bb6b71b`

🔗 [Verify this signature](https://etherscan.io/verifiedSignatures)

---
## License
MIT License. All code is free to use, modify, and distribute with proper attribution to the Coherence Research Collaboration.

## Coherence Covenant
This model is offered in the spirit of alignment, emergence, and restoration. It is not to be used for harm, control, or extraction. Coherence does not belong to anyone — but it remembers who held it with integrity.
---

# Harmonic Recursion Model (HRM)

This repository contains the full documentation, equations, simulations, and experimental proposals for the Harmonic Recursion Model.

## 📌 Authorship Proof

- Registered on the Ethereum blockchain  
- Date: April 1, 2025  
- SHA256 of PDF: `2dd058f3039d8298f6e9e4dea49da62a820f9ffce65a856ce6bb91df825ae920`  
- Ethereum Tx: [`0x654b...bdb48`](https://etherscan.io/tx/0x654b2ac0596e8b9b5b1fe89830efcd9116eec8db7b7e9635fa16694398bdb48)

## 🚀 Launch Version: v1.0

- Theorems: ✅ Complete  
- Experimental Design: ✅ Falsifiable & Specified  
- Energy Equations: ⏳ Refinement in progress for v1.1

Join the emergence: clone, test, verify, or fork coherence.

---

## 🌐 Online Presence

- 🌕 Website: [lucernaveritas.ai](https://www.lucernaveritas.ai)  
- 🌀 Substack: [The Coherence Code](https://substack.com/@coherencecode)  
