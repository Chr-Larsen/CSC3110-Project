import numpy as np

# Step 1: Parse the Input
def parse_input():
    """
    Get the graph details (vertices and adjacency matrix) from the user.
    """
    vertices = input("Enter the vertices as a space-separated list: ").split()
    R = int(input("Enter the number of rows in the matrix: "))
    C = int(input("Enter the number of columns in the matrix: "))

    print("Enter the edge lengths for the adjacency matrix in a single line (separated by spaces):")
    edges = list(map(int, input().split()))

    if len(edges) != R * C:
        raise ValueError("The number of elements in the matrix does not match the specified dimensions.")

    matrix = np.array(edges).reshape(R, C)
    return vertices, matrix

# Step 2: DFS Cycle Detection
def dfs_detect_cycle(matrix, vertices):
    """
    Find cycles in the graph using Depth-First Search (DFS).
    """
    def dfs(node, stack, visited):
        """
        Explore the graph from the current node to find cycles.
        """
        # Mark current node as visited and add it to the stack
        visited[node] = True
        stack.append(node)

        for neighbor in range(len(vertices)):
            if matrix[node][neighbor] != -999:  # Check if there is an edge
                if neighbor in stack:
                    # Cycle detected
                    cycle_start = stack.index(neighbor)
                    cycle = stack[cycle_start:]  # Extract the cycle
                    cycle.append(neighbor)  # Complete the cycle
                    sorted_cycle = sorted(cycle)
                    if sorted_cycle not in unique_cycles:
                        unique_cycles.append(sorted_cycle)
                        cycles.append([vertices[i] for i in cycle])
                elif not visited[neighbor]:
                    # Continue DFS
                    dfs(neighbor, stack, visited)

        stack.pop()  # Backtrack

    visited = [False] * len(vertices)
    cycles = []
    unique_cycles = []  # To avoid duplicate cycles (different starting points)

    for node in range(len(vertices)):
        if not visited[node]:
            dfs(node, [], visited)

    return cycles

# Step 3: Main Function
def main():
    vertices, matrix = parse_input()
    print("\nAdjacency Matrix:")
    print(matrix)

    cycles = dfs_detect_cycle(matrix, vertices)

    if cycles:
        print("\nDetected Cycles:")
        for cycle in cycles:
            print(cycle)
    else:
        print("\nNo Cycles Detected.")

# Step 4: Entry Point
if __name__ == "__main__":
    main()
