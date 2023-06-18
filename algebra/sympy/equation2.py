from sympy import symbols, Eq, solve

y = symbols('y')
eq1 = Eq(y + 3 + 8)

sol = solve(eq1)

print(sol)
