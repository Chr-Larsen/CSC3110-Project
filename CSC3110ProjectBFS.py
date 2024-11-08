import numpy as np

R = int(input("Enter number of rows in matrix:"))
C = int(input("Enter number of columns in matrix"))

print("Enter the edge lengths for the adjacency matrix in a single line (separated by a space): ")

#User input of edges between vertices in adjacency matrix
edges = list(map(int, input().split()))

#prints the matrix
matrix = np.array(edges).reshape(R, C)
print(matrix)