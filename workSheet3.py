# Task 1
# Define the 5x5 grid world with directional labels
world = [
    ["north", "north", "north", "north", "west"],
    ["north", "north", "north", "north", "west"],
    ["north", "north", "goal", "west", "west"],
    ["north", "north", "south", "south", "south"],
    ["east", "east", "south", "south", "south"]
]

class Agent:
    def __init__(self, x, y):
        """
        Initialize the agent with a starting position (x, y).
        """
        self.x = x  # Row position
        self.y = y  # Column position

    def perceive_label(self, world):
        """
        Returns the label of the current position in the grid.
        """
        return world[self.x][self.y]

    def move(self, direction):
        """
        Moves the agent in the specified direction.
        """
        if direction == "north":
            self.x -= 1  # Move up
        elif direction == "south":
            self.x += 1  # Move down
        elif direction == "east":
            self.y += 1  # Move right
        elif direction == "west":
            self.y -= 1  # Move left

# Main function to control the agent's behavior
def main():
    # Initialize the agent at the center of the grid
    agent = Agent(2, 2)
    while True:
        #current position
        current_label = agent.perceive_label(world)
        #reached the goal
        if current_label == "goal":
            break
        agent.move(current_label)

        # Check if the agent has moved out of the grid
        if agent.x < 0 or agent.x >= 5 or agent.y < 0 or agent.y >= 5:
            break

# Run the program
if __name__ == "__main__":
    main()

# Task 2
def mini_controller(agent, world):
    """
    Controls the agent's behavior:
    1. Perceives the label at the current position.
    2. Stops if the label is "goal".
    3. Moves in the direction of the label otherwise.
    """
    while True:
        label = agent.perceive_label(world)  # Step 1: Perceive label
        if label == "goal":  # Step 2: Check if label is goal
            break
        agent.move(label)  # Step 3: Move in the direction of the label
        # Optional: Stop if agent moves out of the grid
        if agent.x < 0 or agent.x >= 5 or agent.y < 0 or agent.y >= 5:
            break
agent = Agent(2, 2)

mini_controller(agent, world)

# Task 3
def hierarchical_controller(agent, world):
    """
    Controls the agent's behavior:
    1. Checks if the goal is reached.
    2. If not, follows the direction label.
    """
    while True:
        # Step 1: Check if the goal is reached
        goal_label = agent.perceive_goal(world)
        if goal_label == "goal":
            print("Goal reached! Agent stops.")
            break

        # Step 2: Follow the direction label
        direction_label = agent.perceive_direction(world)
        agent.move(direction_label)

        # Optional: Stop if agent moves out of the grid
        if agent.x < 0 or agent.x >= 5 or agent.y < 0 or agent.y >= 5:
            break

agent = Agent(2, 2)

hierarchical_controller(agent, world)