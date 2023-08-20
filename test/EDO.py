import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define the function and its derivatives
x = sp.Symbol('x')
f = sp.Function('f')(x)
dfdx = f.diff(x)
d2fdx2 = f.diff(x, 2)

# Define the differential equation
ode = sp.Eq(d2fdx2 + 52*dfdx + (200**2)*f, 0)

# Define the initial conditions
f0 = sp.Symbol('f0')
dfdx0 = sp.Symbol('dfdx0')
ics = {f.subs(x, 0): 1.0714, dfdx.subs(x, 0): -1785}

# Solve the differential equation
sol = sp.dsolve(ode, f, ics=ics)

# Print the solution
print(sol)

# Convert the solution to a callable function
f_func = sp.lambdify(x, sol.rhs, 'numpy')

# Define the range of x values to plot
x_vals = np.linspace(0, 0.2, 1000)

# Evaluate the function at each x value
y_vals = f_func(x_vals)

# Plot the solution
plt.plot(x_vals, y_vals)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Solution to Differential Equation')
plt.grid(True)
plt.show()