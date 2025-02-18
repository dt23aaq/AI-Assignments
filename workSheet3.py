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
