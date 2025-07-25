import matplotlib.pyplot as plt
import numpy as np

# Parâmetros
p_vals = np.linspace(0.4, 1.0, 13)
UC_vals = [1.0, 1.2, 1.4]
T_fixed = 5
UB = 1.5
UP = 0.2

# Cálculo
delta_curves = {UC: [] for UC in UC_vals}
for UC in UC_vals:
    for p in p_vals:
        for delta in np.linspace(0.01, 0.999, 1000):
            lhs = UC
            rhs = (1 - delta) * UB + delta * (
                p * UP * (1 - delta**T_fixed) + (1 - p) * UB * (1 - delta**T_fixed) + delta**T_fixed * UC
            )
            if lhs >= rhs:
                delta_curves[UC].append(delta)
                break
        else:
            delta_curves[UC].append(1.0)

# Plot
plt.figure(figsize=(10, 6))
for UC in UC_vals:
    plt.plot(p_vals, delta_curves[UC], label=f'$U^C_i = {UC}$')

plt.xlabel('Detection Probability $p$')
plt.ylabel('Critical Discount Factor $\delta^{\\text{crit}}$')
plt.title('Sensitivity of $\delta^{\\text{crit}}$ to $U^C_i$ (T = 5)')
plt.legend()
plt.grid(True)
plt.ylim(0, 1.0)
plt.tight_layout()
plt.show()
