# Tehtävä 8.1.2 v)
import numpy as np
from sympy import symbols, Eq, solve

# Määritellään kerroinmatriisi ja vektorimatriisi
A = np.array([[3, -1, 5], [7, 2, 3], [4, 1, -7]])
b = np.array([2, 9, 5])

# Lasketaan determinantti
det_A = np.linalg.det(A)
print(f"Determinantti: {det_A}")

if det_A != 0:
    # Ratkaistaan yhtälöryhmä matriisilaskennan avulla
    solution = np.linalg.solve(A, b)
    print("Ratkaisu:", solution)
else:
    print("Yhtälöryhmällä ei ole yksikäsitteistä ratkaisua.")

# Vaihtoehtoinen ratkaisu SymPyllä
x, y, z = symbols('x y z')
eq1 = Eq(3*x - y + 5*z, 2)
eq2 = Eq(7*x + 2*y + 3*z, 9)
eq3 = Eq(4*x + y - 7*z, 5)

sol = solve((eq1, eq2, eq3), (x, y, z))
print("Ratkaisu SymPyllä:", sol)
