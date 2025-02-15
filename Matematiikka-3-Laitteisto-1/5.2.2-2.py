# Tehtävä 5.2.2 2
import numpy as np

# Annetut matriisit
A = np.array([
    [-1, 1, -3],
    [-1, 5, 2],
    [-4, 2, 1]
])

B = np.array([
    [-2, 2, -3],
    [-7, 4, 3],
    [4, 6, 1]
])

# Lasketaan A - B
A_minus_B = A - B

# Lasketaan B - A
B_minus_A = B - A

# Lasketaan 2A + 5B
result = 2 * A + 5 * B

# Tulostetaan tulokset
print("A - B =\n", A_minus_B)
print("B - A =\n", B_minus_A)
print("2A + 5B =\n", result)
