# Orbital Sustainability Simulations

This repository contains Python code and figures for the simulations presented in the paper *"Sustaining Cooperation in Orbital Commons: A Repeated Game Approach with Finite Punishment"*.

## Structure

- `code/`: Python scripts used to generate simulation results and figures.
- `figures/`: Output plots used in the paper.
- `data/`: Simulation results in CSV format.

## Simulations

### Section 4.1 – Extended Simulation

- Script: `code/delta_crit.py`
- Output: `figures/delta_crit.png`

### Section 4.1 – 3D Visualization of δ_crit

- Script: `code/plot_3d_delta_crit.py`
- Output: `figures/grafico_3d_delta_crit.png`

### Section 4.2 – Sensitivity to $U^C_i$

- Script: `code/sensitivity_uc_variation.py`
- Output: `figures/sensitivity_uc_variation.png`

### Section 4.3 – Strategic Heterogeneity

- Script: `code/simulate_country_types.py`
- Output: `figures/grafico_delta_crit_por_tipo.png`
- Data: `data/delta_crit_simulation_extended.csv`




## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
