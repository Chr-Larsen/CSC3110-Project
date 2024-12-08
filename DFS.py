import numpy as np

# Step 1: Parse the Input
def parse_input():
    """
    Get the graph details (vertices and adjacency matrix) from the user.
    """
        # Get the list of vertices from the user

    vertices = input("Enter the vertices as a space-separated list: ").split()
        # Get the dimensions of the adjacency matrix

    R = int(input("Enter the number of rows in the matrix: "))
    C = int(input("Enter the number of columns in the matrix: "))
    
    # Get the edge weights as a single line of input and convert to a list

    print("Enter the edge lengths for the adjacency matrix in a single line (separated by spaces):")
    edges = list(map(int, input().split()))
        # Check if the input matches the matrix dimensions


    if len(edges) != R * C:
        raise ValueError("The number of elements in the matrix does not match the specified dimensions.")
    # Reshape the list of edges into a 2D adjacency matrix

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
                     # If the neighbor is already in the stack, we found a cycle

                    cycle_start = stack.index(neighbor)# Find where the cycle starts
                    cycle = stack[cycle_start:]  # Extract the cycle
                    cycle.append(neighbor)  # Complete the cycle
                    sorted_cycle = sorted(cycle)# Sort the cycle to avoid duplicates
                    if sorted_cycle not in unique_cycles:# Check if the cycle is unique
                        unique_cycles.append(sorted_cycle)# Save unique cycle structure
                        cycles.append([vertices[i] for i in cycle])# Save cycle with vertex names
                elif not visited[neighbor]:
                     # If the neighbor is not visited, continue DFS
                    dfs(neighbor, stack, visited)
      # Remove the current node from the stack (backtracking step)
        stack.pop()  # Backtrack
# Initialize visited list for all vertices
    visited = [False] * len(vertices)
    cycles = [] # To store the detected cycles
    unique_cycles = []  # To avoid duplicate cycles (different starting points)
   # Run DFS from each node that hasn't been visited
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
