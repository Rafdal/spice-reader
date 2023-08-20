import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from libs.utils import searchMaxMinInRange

# Define the function
x = sp.Symbol('x')
# f = 100e-6 * (-26 * sp.exp(-26 * x) * (10 * sp.cos(198.3 * x) + 1.312 * sp.sin(198.3 * x)) + sp.exp(-26 * x) * (-1983.03 * sp.sin(198.3 * x) + 260 * sp.cos(198.3 * x)))
    # 100*10^(-6) (-26 ℯ^(-26 x) (1.07143 cos(198.3 x)-8.865 sen(198.3 x))+ℯ^(-26 x) (-212.467 sen(198.3 x)-1757.9 cos(198.3 x)))
f = 100e-6 * (-26 * sp.exp(-26 * x) * (1.07143 * sp.cos(198.3 * x) - 8.865 * sp.sin(198.3 * x)) + sp.exp(-26 * x) * (-212.467 * sp.sin(198.3 * x) - 1757.9 * sp.cos(198.3 * x)))

# Compute the derivative with respect to x
dfdx = sp.diff(f, x)

# Convert the SymPy expressions to NumPy functions
f_np = sp.lambdify(x, f, 'numpy')
dfdx_np = sp.lambdify(x, dfdx, 'numpy')

# Generate x values
x_vals = np.linspace(0, 0.2, 4000)

# Evaluate the functions at each x value
f_vals = f_np(x_vals)
dfdx_vals = dfdx_np(x_vals) * (-0.25)

# Plot the functions
fig, ax = plt.subplots(figsize=(8, 6))

ax2 = ax.twinx()

ax2.plot(x_vals, f_vals, c='red', linewidth=1.5, alpha=1.0, label='Corriente C [A]')

ax.plot(x_vals, dfdx_vals, c='blue', linewidth=1.5, alpha=1.0, label='Tension L [V]')

_, _ = searchMaxMinInRange(x_vals, f_vals, 0.0, 0.01, returnAxis='y', ax=ax2, c='r', text = "up", ignore = None)

_, _ = searchMaxMinInRange(x_vals, dfdx_vals, 0.001, 0.025, returnAxis='y', ignore = None, ax=ax, c='b', text = "down")


ax.set_xlabel('Tiempo [s]')
ax.set_ylabel('Tension [V]')
ax2.set_ylabel('Corriente [A]')

ax.grid(True, which='both', axis='both')

ax.legend(loc='upper right')
ax2.legend(loc='lower right')

# Show the plot
plt.show()