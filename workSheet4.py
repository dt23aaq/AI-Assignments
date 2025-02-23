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