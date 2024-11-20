# Cycle Detection in Directed Graphs ( CSC3110-Project 5)
Team members: Christian Larsen, Deboshree Chowdhury, Tawheed Mokammel & Abrar Mohammed

## Overview
This project implements two algorithms, **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**, to detect cycles in directed graphs. The algorithms identify all cycles in the graph, represented as an adjacency matrix, and output them as ordered sequences of vertices.

The goal is to compare the two algorithms based on their strategies, complexity, and performance.

---

## Problem Statement
The task is to identify all cycles in a directed graph using two different traversal algorithms: BFS and DFS.

### Input
1. **Vertices**: A list of vertices (e.g., `A, B, C, D, E`).
2. **Adjacency Matrix**:
   - A 2D array representing edges between vertices.
   - A positive number indicates the edge weight.
   - `-999` indicates no edge exists between vertices (infinity).

### Output
- A list of cycles detected in the graph. Each cycle is an ordered sequence of vertices.

---

## Algorithms Implemented

### 1. Breadth-First Search (BFS)
- **Strategy**: Level-by-level traversal using a queue.
- **Approach**:
  - Start BFS from each unvisited vertex.
  - Track visited nodes and the current path.
  - Detect cycles by checking if a neighbor is already in the path.
- **Time Complexity**: \(O(V^2 + E \cdot V)\)
- **Space Complexity**: \(O(V)\)

### 2. Depth-First Search (DFS)
- **Strategy**: Recursive depth-first traversal using a stack.
- **Approach**:
  - Start DFS from each unvisited vertex.
  - Track visited nodes and the recursion stack.
  - Detect cycles by identifying nodes revisited in the same recursion path.
- **Time Complexity**: \(O(V^2 + E)\)
- **Space Complexity**: \(O(V)\)

---

## Key Differences Between BFS and DFS
| **Feature**          | **BFS**                              | **DFS**                              |
|-----------------------|--------------------------------------|--------------------------------------|
| **Traversal Method**  | Iterative (queue-based).             | Recursive (stack-based).             |
| **Cycle Detection**   | Checks if a neighbor is in the path. | Checks if a node is in the recursion stack. |
| **Space Complexity**  | \(O(V)\)                            | \(O(V)\)                            |
| **Use Case**          | Best for shallow graphs.            | Best for deeper graphs.              |




### Presentation powerpoint Slides
- https://waynestateprod-my.sharepoint.com/:p:/g/personal/hg9512_wayne_edu/ETIUk5ANM_JPicjfWYintEIBe1Tzj7LpT2ENJyFzT-ZXMQ?e=x5SPlC
