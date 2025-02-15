 # Tehtävä 8.1.1 v)
import numpy as np
from sympy import symbols, Eq, solve

# Määritellään kerroinmatriisi ja vektorimatriisi
A = np.array([[2, -3], [7, 1]])
b = np.array([5, 3])

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
x, y = symbols('x y')
eq1 = Eq(2*x - 3*y, 5)
eq2 = Eq(7*x + y, 3)

sol = solve((eq1, eq2), (x, y))
print("Ratkaisu SymPyllä:", sol)
