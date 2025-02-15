#Tehtävä 8.1.3 v1
import numpy as np
from sympy import symbols, Eq, solve

# Määritellään kerroinmatriisi ja vektorimatriisi
A = np.array([[1, 1, 1], [2, 1, -1], [4, 3, 1]])
b = np.array([3, 2, 5])

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
eq1 = Eq(x + y + z, 3)
eq2 = Eq(2*x + y - z, 2)
eq3 = Eq(4*x + 3*y + z, 5)

sol = solve((eq1, eq2, eq3), (x, y, z))
print("Ratkaisu SymPyllä:", sol)
