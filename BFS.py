#Deboshree Chowdhury & Christian Larsen 

import numpy as np
from collections import deque

# Step 1: Input Parsing (integrates the existing code)
def parse_input():
    # Input the vertices
    vertices = input("Enter the vertices as a space-separated list: ").split()
    
    # Input adjacency matrix dimensions
    R = int(input("Enter number of rows in the matrix: "))
    C = int(input("Enter number of columns in the matrix: "))
    
    # Input edge weights
    print("Enter the edge lengths for the adjacency matrix in a single line (separated by spaces):")
    edges = list(map(int, input().split()))
    
    # Convert input into a 2D adjacency matrix
    matrix = np.array(edges).reshape(R, C)
    return vertices, matrix

# Step 2: BFS Cycle Detection
def bfs_detect_cycle(matrix, vertices):
    num_vertices = len(vertices)
    visited = [False] * num_vertices
    queue = deque()
    cycles = []

    for start in range(num_vertices):  # Start BFS from each vertex
        if not visited[start]:
            path = []  # Track the current path
            queue.append((start, [start]))  # (current vertex, path)

            while queue:
                current, path = queue.popleft()
                visited[current] = True

                for neighbor in range(num_vertices):
                    if matrix[current][neighbor] != -999:  # Edge exists
                        if neighbor in path:
                            # Cycle detected
                            cycle = path[path.index(neighbor):] + [neighbor]
                            cycles.append([vertices[i] for i in cycle])
                        elif not visited[neighbor]:
                            queue.append((neighbor, path + [neighbor]))

    # Print all detected cycles
    if cycles:
        print("Detected cycles:")
        for cycle in cycles:
            print(cycle)
    else:
        print("No cycles detected.")

# Step 3: Main Function
def main():
    # Parse the input
    vertices, matrix = parse_input()
    
    # Print the adjacency matrix for verification
    print("Adjacency Matrix:")
    print(matrix)
    
    # Detect cycles using BFS
    bfs_detect_cycle(matrix, vertices)

# Step 4: Entry Point
if __name__ == "__main__":
    main()
