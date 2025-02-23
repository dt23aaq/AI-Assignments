import heapq

# Define the graph
class Node:
    def __init__(self, name):
        self.name = name
        self.adjacent = {}  # Key: neighbor node, Value: edge weight
        self.distance = float('inf')
        self.previous = None

    def __lt__(self, other):
        return self.distance < other.distance
# Create nodes
v1 = Node('v1')
v2 = Node('v2')
v3 = Node('v3')
v4 = Node('v4')
v5 = Node('v5')
v6 = Node('v6')

# Add edges with weights
v1.adjacent = {v2: 1}
v2.adjacent = {v1: 1, v3: 2, v4: 3, v6: 6}
v3.adjacent = {v2: 2, v4: 4}
v4.adjacent = {v2: 3, v3: 4, v5: 5, v6: 7}
v5.adjacent = {v4: 5}
v6.adjacent = {v2: 6, v4: 7}