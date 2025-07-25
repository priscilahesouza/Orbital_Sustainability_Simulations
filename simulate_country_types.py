#Simulação Seção 4.2

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define parameters for each country type
country_types = {
    "Tipo 1": {"bar_U": 1.6, "U_P": 0.3},
    "Tipo 2": {"bar_U": 1.4, "U_P": 0.4},
    "Tipo 3": {"bar_U": 1.3, "U_P": 0.5},
    "Tipo 4": {"bar_U": 1.2, "U_P": 0.6},
}
U_C = 1.0
T_values = [3, 5, 10]
p_values = np.round(np.arange(0.4, 1.01, 0.05), 2)

# Function to compute the LHS and RHS of the incentive constraint
def incentive_condition(delta, bar_U, U_P, U_C, p, T):
    lhs = U_C
    rhs = (1 - delta) * bar_U + delta * (
        p * U_P * (1 - delta**T) +
        (1 - p) * bar_U * (1 - delta**T) +
        delta**T * U_C
    )
    return lhs - rhs

# Find delta_crit numerically
def find_delta_crit(bar_U, U_P, U_C, p, T):
    for delta in np.linspace(0.01, 0.999, 1000):
        if incentive_condition(delta, bar_U, U_P, U_C, p, T) >= 0:
            return round(delta, 3)
    return 1.0  # If no delta satisfies the condition, return 1

# Run simulation
results = []
for tipo, params in country_types.items():
    for T in T_values:
        for p in p_values:
            delta_crit = find_delta_crit(params["bar_U"], params["U_P"], U_C, p, T)
            results.append({
                "Tipo": tipo,
                "T": T,
                "p": p,
                "delta_crit": delta_crit
            })

# Save to CSV
df = pd.DataFrame(results)
df.to_csv("delta_crit_simulacao_estendida.csv", index=False)

# Group by Tipo and p to average over T
avg_df = df.groupby(["Tipo", "p"], as_index=False)["delta_crit"].mean()

# Plotting
plt.figure(figsize=(10, 6))
for tipo in avg_df["Tipo"].unique():
    subset = avg_df[avg_df["Tipo"] == tipo]
    plt.plot(subset["p"], subset["delta_crit"], label=tipo)

plt.axhline(1.0, color="gray", linestyle="--", linewidth=0.8)
plt.xlabel("Detection Probability (p)")
plt.ylabel("Critical Discount Factor (δ_crit)")
plt.title("δ_crit vs Detection Probability by Country Type (T averaged out)")
plt.legend(title="Country Type")
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_delta_crit_por_tipo.png")

