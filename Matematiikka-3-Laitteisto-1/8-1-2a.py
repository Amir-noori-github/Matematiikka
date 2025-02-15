# Tehtävä 8.1.2 a)
import numpy as np
from sympy import symbols, Eq, solve

# Määritellään kerroinmatriisi ja vektorimatriisi
A = np.array([[2, 1, -3], [-3, -1, 2], [5, 2, -4]])
b = np.array([5, -7, 12])

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
eq1 = Eq(2*x + y - 3*z, 5)
eq2 = Eq(-3*x - y + 2*z, -7)
eq3 = Eq(5*x + 2*y - 4*z, 12)

sol = solve((eq1, eq2, eq3), (x, y, z))
print("Ratkaisu SymPyllä:", sol)
