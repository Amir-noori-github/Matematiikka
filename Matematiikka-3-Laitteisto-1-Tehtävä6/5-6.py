import numpy as np

# Define the coefficient matrix A
A = np.array([[7, -3, -1],
              [-4, 9, 2],
              [1, -2, 0]])

# Define the constant matrix B
B = np.array([6, 5, -8])

# Calculate the inverse of A
A_inv = np.linalg.inv(A)

# Solve for X by multiplying A_inv and B
X = np.dot(A_inv, B)

# Print the solution
print("Solution:")
print("x =", X[0])
print("y =", X[1])
print("z =", X[2])