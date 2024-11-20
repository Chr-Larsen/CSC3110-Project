# Tawheed Mokammel and Abrar Mohammed

import numpy as np

# Step 1: Parse the Input
def parse_input():
    """
    Get the graph details (vertices and adjacency matrix) from the user.
    """
    # Ask for the list of vertices (space-separated)
    vertices = input("Enter the vertices as a space-separated list: ").split()

    # Ask for the size of the adjacency matrix (rows and columns)
    R = int(input("Enter the number of rows in the matrix: "))
    C = int(input("Enter the number of columns in the matrix: "))

    # Ask for the matrix values (all values in a single line, separated by spaces)
    print("Enter the edge lengths for the adjacency matrix in a single line (separated by spaces):")
    edges = list(map(int, input().split()))

    # Convert the list into a 2D array (matrix format)
    matrix = np.array(edges).reshape(R, C)
    return vertices, matrix


# Step 2: DFS Cycle Detection
def dfs_detect_cycle(matrix, vertices):
    """
    Find cycles in the graph using Depth-First Search (DFS).
    """

    def dfs(node, visited, stack):
        """
        Explore the graph from the current node to find cycles.
        """
        # Mark the current node as visited and add it to the current path (stack)
        visited[node] = True
        stack.append(node)

        # Look at all possible neighbors (connections) of the current node
        for neighbor in range(len(vertices)):
            if matrix[node][neighbor] != -999:  # If there is an edge to a neighbor
                if not visited[neighbor]:  # If the neighbor has not been visited yet
                    dfs(neighbor, visited, stack)  # Continue DFS with the neighbor
                elif neighbor in stack:  # If the neighbor is already in the current path
                    # A cycle is found! Extract the cycle from the stack
                    cycle_start = stack.index(neighbor)
                    cycle = stack[cycle_start:] + [neighbor]  # Add the start node to close the cycle
                    if cycle not in cycles:  # Avoid duplicates
                        cycles.append([vertices[i] for i in cycle])  # Save the cycle with vertex names

        # Remove the current node from the path (backtracking)
        stack.pop()

    # Total number of vertices
    num_vertices = len(vertices)
    # Keep track of visited nodes
    visited = [False] * num_vertices
    # Store all the cycles found
    cycles = []

    # Start DFS from every vertex to make sure we find all cycles
    for start in range(num_vertices):
        if not visited[start]:  # If this vertex hasn’t been visited yet
            dfs(start, visited, [])

    # Print the cycles if any are found
    if cycles:
        print("Detected cycles:")
        for cycle in cycles:
            print(cycle)
    else:
        print("No cycles detected.")  # Let the user know if no cycles exist


# Step 3: Main Function
def main():

    # Get the input from the user (vertices and adjacency matrix)
    vertices, matrix = parse_input()

    # Print the adjacency matrix so the user can see it
    print("Adjacency Matrix:")
    print(matrix)

    # Find cycles in the graph
    dfs_detect_cycle(matrix, vertices)


# Step 4: Entry Point
if __name__ == "__main__":

    main()
