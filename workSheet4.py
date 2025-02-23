import heapq

# Define the graph using a dictionary for simplicity
graph = {
    'v1': {'v2': 1},
    'v2': {'v1': 1, 'v3': 2, 'v4': 3, 'v6': 6},
    'v3': {'v2': 2, 'v4': 4},
    'v4': {'v2': 3, 'v3': 4, 'v5': 5, 'v6': 7},
    'v5': {'v4': 5},
    'v6': {'v2': 6, 'v4': 7}
}

###################
# Task 1: Dijkstra's Algorithm
###################
def dijkstra(start, target, graph):
    """
    Finds the shortest path from `start` to `target` using Dijkstra's algorithm.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    heap = [(0, start)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_node == target:
            break

        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(heap, (new_distance, neighbor))

    # Reconstruct the path
    path = []
    current = target
    while current:
        path.append(current)
        current = previous[current]

    return path[::-1], distances[target]

###################
# Task 2-4: Agent with Memory
###################
class Agent:
    def __init__(self, start_node, graph):
        self.current_node = start_node
        self.graph = graph
        self.spanning_tree_nodes = set()
        self.spanning_tree_edges = set()
        self.spanning_tree_nodes.add(start_node)

        # Memory: Priority queue to store candidate edges (weight, node1, node2)
        self.candidate_edges = []
        self._initialize_candidate_edges()

    def _initialize_candidate_edges(self):
        """
        Initialize candidate edges with edges from the start node.
        """
        for neighbor, weight in self.graph[self.current_node].items():
            heapq.heappush(self.candidate_edges, (weight, self.current_node, neighbor))

    def sense_current_node_name(self):
        """
        Returns the name of the current node.
        """
        return self.current_node

    def sense_edges_leaving_current_node(self):
        """
        Returns a list of edges leaving the current node.
        """
        return [(neighbor, weight) for neighbor, weight in self.graph[self.current_node].items()]

    def add_to_spanning_tree(self, node, edge):
        """
        Adds a node and edge to the spanning tree.
        """
        self.spanning_tree_nodes.add(node)
        self.spanning_tree_edges.add(edge)

    def get_spanning_tree_nodes(self):
        """
        Returns the nodes in the spanning tree.
        """
        return self.spanning_tree_nodes

    def get_spanning_tree_edges(self):
        """
        Returns the edges in the spanning tree.
        """
        return self.spanning_tree_edges

    def move_to_node(self, node):
        """
        Moves the agent to a new node.
        """
        self.current_node = node

    def choose_lowest_edge_preserving_tree(self):
        """
        Chooses the edge with the lowest value that preserves the tree properties.
        Returns the chosen edge (as a tuple) or None if no valid edge is found.
        """
        while self.candidate_edges:
            weight, node1, node2 = heapq.heappop(self.candidate_edges)

            # Check if adding this edge would create a cycle
            if node2 not in self.spanning_tree_nodes:
                return (node1, node2, weight)

        return None

    def expand_candidate_edges(self):
        """
        Expands the candidate edges by adding edges from the current node.
        """
        for neighbor, weight in self.graph[self.current_node].items():
            if neighbor not in self.spanning_tree_nodes:
                heapq.heappush(self.candidate_edges, (weight, self.current_node, neighbor))

    def get_candidate_edges(self):
        """
        Returns the current candidate edges.
        """
        return self.candidate_edges

###################
# Main Program
###################
if __name__ == "__main__":
    # Task 1: Dijkstra's Algorithm
    start_node = 'v1'
    target_node = 'v5'
    path, distance = dijkstra(start_node, target_node, graph)
    print(f"Shortest path from {start_node} to {target_node}: {path}")
    print(f"Total distance: {distance}\n")

    # Task 2-4: Agent with Memory
    agent = Agent(start_node, graph)
    print("Current node:", agent.sense_current_node_name())
    print("Edges leaving current node:", agent.sense_edges_leaving_current_node())
    print("Initial candidate edges:", agent.get_candidate_edges())

    # Move to v2 and add to spanning tree
    lowest_edge = agent.choose_lowest_edge_preserving_tree()
    if lowest_edge:
        print("Lowest edge preserving tree properties:", lowest_edge)
        agent.add_to_spanning_tree(lowest_edge[1], (lowest_edge[0], lowest_edge[1]))
        agent.move_to_node(lowest_edge[1])
        agent.expand_candidate_edges()
    else:
        print("No valid edge found.")

    print("Current node:", agent.sense_current_node_name())
    print("Edges leaving current node:", agent.sense_edges_leaving_current_node())
    print("Updated candidate edges:", agent.get_candidate_edges())

    # Move to v4 and add to spanning tree
    lowest_edge = agent.choose_lowest_edge_preserving_tree()
    if lowest_edge:
        print("Lowest edge preserving tree properties:", lowest_edge)
        agent.add_to_spanning_tree(lowest_edge[1], (lowest_edge[0], lowest_edge[1]))
        agent.move_to_node(lowest_edge[1])
        agent.expand_candidate_edges()
    else:
        print("No valid edge found.")

    print("Current node:", agent.sense_current_node_name())
    print("Edges leaving current node:", agent.sense_edges_leaving_current_node())
    print("Updated candidate edges:", agent.get_candidate_edges())

    # Print spanning tree nodes and edges
    print("Spanning tree nodes:", agent.get_spanning_tree_nodes())
    print("Spanning tree edges:", agent.get_spanning_tree_edges())