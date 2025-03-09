import numpy as np  # Import numpy

# Define the matrix D
D = np.array([[3, 2, 0, -4],
              [5, 6, 7, 1],
              [0, -5, -1, 0],
              [1, 3, 4, 2]])

# Compute the determinant to check if the matrix is invertible
det_D = np.linalg.det(D)

if np.isclose(det_D, 0):  # Check if determinant is approximately zero
    print("Matrix D is singular and does not have an inverse.")
else:
    # Compute the inverse
    D_inv = np.linalg.inv(D)

    # Print the inverse rounded to 4 decimal places
    print("Inverse of matrix D:")
    print(np.round(D_inv, 2))
