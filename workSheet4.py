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

# Dijkstra's algorithm
def dijkstra(start, target):
    heap = []
    start.distance = 0
    heapq.heappush(heap, start)

    while heap:
        current_node = heapq.heappop(heap)

        if current_node == target:
            break

        for neighbor, weight in current_node.adjacent.items():
            new_distance = current_node.distance + weight

            if new_distance < neighbor.distance:
                neighbor.distance = new_distance
                neighbor.previous = current_node
                heapq.heappush(heap, neighbor)

    # Reconstruct the path
    path = []
    current = target
    while current:
        path.append(current.name)
        current = current.previous

    return path[::-1], target.distance

# Run Dijkstra's algorithm from v1 to v5
start_node = v1
target_node = v5
path, distance = dijkstra(start_node, target_node)

class Agent:
    def __init__(self, start_node):
        self.current_node = start_node
        self.spanning_tree_nodes = set()
        self.spanning_tree_edges = set()
        self.spanning_tree_nodes.add(start_node.name)

    def sense_current_node_name(self):
        return self.current_node.name

    def sense_edges_leaving_current_node(self):
        return [(neighbor.name, weight) for neighbor, weight in self.current_node.adjacent.items()]

    def add_to_spanning_tree(self, node, edge):
        self.spanning_tree_nodes.add(node.name)
        self.spanning_tree_edges.add(edge)

    def get_spanning_tree_nodes(self):
        return self.spanning_tree_nodes

    def get_spanning_tree_edges(self):
        return self.spanning_tree_edges

    def move_to_node(self, node):
        self.current_node = node

# Define the graph
class Node:
    def __init__(self, name):
        self.name = name
        self.adjacent = {}  # Key: neighbor node, Value: edge weight

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

# Initialize the agent at v1
agent = Agent(v1)

print("Current node:", agent.sense_current_node_name())
print("Edges leaving current node:", agent.sense_edges_leaving_current_node())

# Move to v2 and add to spanning tree
agent.move_to_node(v2)
agent.add_to_spanning_tree(v2, ('v1', 'v2'))
print("Current node:", agent.sense_current_node_name())
print("Edges leaving current node:", agent.sense_edges_leaving_current_node())

# Move to v4 and add to spanning tree
agent.move_to_node(v4)
agent.add_to_spanning_tree(v4, ('v2', 'v4'))
print("Current node:", agent.sense_current_node_name())
print("Edges leaving current node:", agent.sense_edges_leaving_current_node())

# Print spanning tree nodes and edges
print("Spanning tree nodes:", agent.get_spanning_tree_nodes())
print("Spanning tree edges:", agent.get_spanning_tree_edges())

class Agent:
    def __init__(self, start_node, graph):
        self.current_node = start_node
        self.graph = graph
        self.spanning_tree_nodes = set()
        self.spanning_tree_edges = set()
        self.spanning_tree_nodes.add(start_node)

    def sense_current_node_name(self):
        return self.current_node

    def sense_edges_leaving_current_node(self):
        return self.graph[self.current_node]

    def add_to_spanning_tree(self, node, edge):
        self.spanning_tree_nodes.add(node)
        self.spanning_tree_edges.add(edge)

    def get_spanning_tree_nodes(self):
        return self.spanning_tree_nodes

    def get_spanning_tree_edges(self):
        return self.spanning_tree_edges

    def move_to_node(self, node):
        self.current_node = node

    def choose_lowest_edge_preserving_tree(self):
        """
        Chooses the edge with the lowest value that preserves the tree properties.
        Returns the chosen edge (as a tuple) or None if no valid edge is found.
        """
        edges = self.sense_edges_leaving_current_node()
        lowest_edge = None
        lowest_weight = float('inf')

        for neighbor, weight in edges.items():
            # Check if adding this edge would create a cycle
            if neighbor not in self.spanning_tree_nodes:
                if weight < lowest_weight:
                    lowest_weight = weight
                    lowest_edge = (self.current_node, neighbor, weight)

        return lowest_edge

# Define the graph using a dictionary
graph = {
    'v1': {'v2': 1},
    'v2': {'v1': 1, 'v3': 2, 'v4': 3, 'v6': 6},
    'v3': {'v2': 2, 'v4': 4},
    'v4': {'v2': 3, 'v3': 4, 'v5': 5, 'v6': 7},
    'v5': {'v4': 5},
    'v6': {'v2': 6, 'v4': 7}
}

# Initialize the agent at 'v1'
agent = Agent('v1', graph)

# Example usage
print("Current node:", agent.sense_current_node_name())
print("Edges leaving current node:", agent.sense_edges_leaving_current_node())

# Choose the lowest edge preserving tree properties
lowest_edge = agent.choose_lowest_edge_preserving_tree()
if lowest_edge:
    print("Lowest edge preserving tree properties:", lowest_edge)
    # Add the edge to the spanning tree and move to the new node
    agent.add_to_spanning_tree(lowest_edge[1], (lowest_edge[0], lowest_edge[1]))
    agent.move_to_node(lowest_edge[1])
else:
    print("No valid edge found.")

# Print spanning tree nodes and edges
print("Spanning tree nodes:", agent.get_spanning_tree_nodes())
print("Spanning tree edges:", agent.get_spanning_tree_edges())