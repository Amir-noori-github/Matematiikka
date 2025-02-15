# Tehtävä 5.1.1 2
import numpy as np

# Luodaan 3x3-matriisi i - j
A = np.array([[i - j for j in range(1, 4)] for i in range(1, 4)])

print("Matriisi A:")
print(A)
