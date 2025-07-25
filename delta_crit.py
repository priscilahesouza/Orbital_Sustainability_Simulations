# Simulação Seção 4.1

import numpy as np
import matplotlib.pyplot as plt

# Define parameters
U_C = 1.0           # Cooperative payoff
U_bar = 1.5         # Short-term gain from deviation
U_P = 0.2           # Punishment payoff

# Define function to check sustainability condition
def is_sustainable(delta, p, T):
    lhs = U_C
    rhs = (1 - delta) * U_bar + delta * (
        p * U_P * (1 - delta**T) + (1 - p) * U_bar * (1 - delta**T) + delta**T * U_C
    )
    return lhs >= rhs

# Create parameter grids
delta_vals = np.linspace(0.85, 0.99, 100)
p_vals = np.linspace(0.1, 1.0, 100)
T_vals = [1, 3, 5, 10]

# Plot sustainability regions for different T values
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

for idx, T in enumerate(T_vals):
    sustainability = np.zeros((len(delta_vals), len(p_vals)))
    for i, delta in enumerate(delta_vals):
        for j, p in enumerate(p_vals):
            sustainability[i, j] = is_sustainable(delta, p, T)
    
    ax = axes[idx]
    X, Y = np.meshgrid(p_vals, delta_vals)
    c = ax.contourf(X, Y, sustainability, levels=[0, 0.5, 1], colors=["lightcoral", "lightgreen"])
    ax.set_title(f"Sustainability Region (T = {T})")
    ax.set_xlabel("Probability of Detection (p)")
    ax.set_ylabel("Discount Factor (δ)")
    ax.grid(True)

plt.tight_layout()
plt.show()

