# Tehtävä 5.1.1 a
import numpy as np

# Matriisi A parametreilla x ja y
def matrix_A(x, y):
    return np.array([[x + y, 5], [-1, x - y]])

# Matriisit B ja C
B = np.array([[3, 2], [-3, 1]])
C = np.array([[3, 5], [-1, 1]])

# Tarkistetaan, voiko A olla yhtä suuri kuin B
def solve_for_B():
    A_matrix = np.array([[1, 1], [1, -1]])
    b_vector = np.array([3, 2])
    det_A = np.linalg.det(A_matrix)
    print(f"Determinantti A = B: {det_A}")
    if det_A != 0:
        return np.linalg.solve(A_matrix, b_vector)
    else:
        raise np.linalg.LinAlgError("Yhtälöryhmällä ei ole yksikäsitteistä ratkaisua.")

# Tarkistetaan, voiko A olla yhtä suuri kuin C
def solve_for_C():
    A_matrix = np.array([[1, 1], [1, -1]])
    b_vector = np.array([3, 1])
    det_A = np.linalg.det(A_matrix)
    print(f"Determinantti A = C: {det_A}")
    if det_A != 0:
        return np.linalg.solve(A_matrix, b_vector)
    else:
        raise np.linalg.LinAlgError("Yhtälöryhmällä ei ole yksikäsitteistä ratkaisua.")

try:
    x_B, y_B = solve_for_B()
    print(f"A = B on mahdollista, kun x = {x_B}, y = {y_B}")
except np.linalg.LinAlgError:
    print("A = B ei ole mahdollista.")

try:
    x_C, y_C = solve_for_C()
    print(f"A = C on mahdollista, kun x = {x_C}, y = {y_C}")
except np.linalg.LinAlgError:
    print("A = C ei ole mahdollista.")
