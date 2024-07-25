import sympy as sp
# this program differentiates the equation x**2 - x -2 to 2*x - 1
x = sp.symbols('x')
f = x**2 - x - 2
df = sp.diff(f, x)
print(df)
