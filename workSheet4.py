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
# Task 2: Agent for Spanning Tree
###################
class Agent:
    def __init__(self, start_node, graph):
        self.current_node = start_node
        self.graph = graph
        self.spanning_tree_nodes = set()
        self.spanning_tree_edges = set()
        self.spanning_tree_nodes.add(start_node)

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

###################
# Task 3: Agent with Lowest-Edge Selection
###################
    def choose_lowest_edge_preserving_tree(self):
        """
        Chooses the edge with the lowest value that preserves the tree properties.
        Returns the chosen edge (as a tuple) or None if no valid edge is found.
        """
        edges = self.sense_edges_leaving_current_node()
        lowest_edge = None
        lowest_weight = float('inf')

        for neighbor, weight in edges:
            # Check if adding this edge would create a cycle
            if neighbor not in self.spanning_tree_nodes:
                if weight < lowest_weight:
                    lowest_weight = weight
                    lowest_edge = (self.current_node, neighbor, weight)

        return lowest_edge

###################
# Main Program
###################
if __name__ == "__main__":
    # Task 1: Dijkstra's Algorithm
    start_node = 'v1'
    target_node = 'v5'
    path, distance = dijkstra(start_node, target_node, graph)
    print(f"Task 1: Shortest path from {start_node} to {target_node}: {path}")
    print(f"Task 1: Total distance: {distance}\n")

    # Task 2: Agent for Spanning Tree
    agent = Agent(start_node, graph)
    print("Task 2: Current node:", agent.sense_current_node_name())
    print("Task 2: Edges leaving current node:", agent.sense_edges_leaving_current_node())

    # Move to v2 and add to spanning tree
    agent.move_to_node('v2')
    agent.add_to_spanning_tree('v2', ('v1', 'v2'))
    print("Task 2: Current node:", agent.sense_current_node_name())
    print("Task 2: Edges leaving current node:", agent.sense_edges_leaving_current_node())

    # Move to v4 and add to spanning tree
    agent.move_to_node('v4')
    agent.add_to_spanning_tree('v4', ('v2', 'v4'))
    print("Task 2: Current node:", agent.sense_current_node_name())
    print("Task 2: Edges leaving current node:", agent.sense_edges_leaving_current_node())

    # Print spanning tree nodes and edges
    print("Task 2: Spanning tree nodes:", agent.get_spanning_tree_nodes())
    print("Task 2: Spanning tree edges:", agent.get_spanning_tree_edges(), "\n")

    # Task 3: Agent with Lowest-Edge Selection
    lowest_edge = agent.choose_lowest_edge_preserving_tree()
    if lowest_edge:
        print("Task 3: Lowest edge preserving tree properties:", lowest_edge)
        # Add the edge to the spanning tree and move to the new node
        agent.add_to_spanning_tree(lowest_edge[1], (lowest_edge[0], lowest_edge[1]))
        agent.move_to_node(lowest_edge[1])
    else:
        print("Task 3: No valid edge found.")

    # Print spanning tree nodes and edges
    print("Task 3: Spanning tree nodes:", agent.get_spanning_tree_nodes())
    print("Task 3: Spanning tree edges:", agent.get_spanning_tree_edges())
