import numpy as np

A = np.array([
    [2, 3, 1],
    [1, -1, 2],
    [3, 4, 1]
])

B = np.array([13, 7, 22])

X = np.linalg.solve(A, B)

print("x =", round(X[0]))
print("y =", round(X[1]))
print("z =", round(X[2]))
