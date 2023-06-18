from sympy import symbols, Eq, solve

x = symbols('x')
eq1 = Eq(x**2-5*x+6)

sol = solve(eq1)

print(sol)
