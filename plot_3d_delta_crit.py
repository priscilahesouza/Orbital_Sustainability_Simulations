import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parâmetros fixos para simulações
p_values = np.linspace(0.4, 1.0, 13)
T_values = [3, 5, 10]
UC_values = [1.0, 1.2, 1.4]
UB = 1.5  # ganho de desvio
UP = 0.2  # payoff sob punição

# Função para calcular delta crítico
def compute_delta_crit(UC, UB, UP, p, T):
    for delta in np.linspace(0.01, 0.999, 1000):
        lhs = UC
        rhs = (1 - delta) * UB + delta * (
            p * UP * (1 - delta**T) +
            (1 - p) * UB * (1 - delta**T) +
            delta**T * UC
        )
        if lhs >= rhs:
            return delta
    return 1.0  # Fora da faixa sustentável

# Construção de grade para gráfico 3D (p, T, delta_crit) para UC = 1.0
P_grid, T_grid = np.meshgrid(p_values, T_values)
delta_grid = np.zeros_like(P_grid)

for i in range(P_grid.shape[0]):
    for j in range(P_grid.shape[1]):
        delta_grid[i, j] = compute_delta_crit(UC=1.0, UB=UB, UP=UP,
                                              p=P_grid[i, j], T=T_grid[i, j])

# Gráfico de superfície 3D
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(P_grid, T_grid, delta_grid, cmap='viridis', edgecolor='k', alpha=0.9)
ax.set_title('Critical Discount Factor as a Function of $p$ and $T$ (for $U^C = 1.0$)', fontsize=11)
ax.set_xlabel('Detection Probability $p$')
ax.set_ylabel('Punishment Duration $T$')
ax.set_zlabel('Critical Discount Factor $\\delta^{crit}$')
plt.tight_layout()
plt.show()
