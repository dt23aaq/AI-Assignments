class GridWorld:
    def __init__(self, rows=5, cols=5):
        """
        Initialize the GridWorld with a specified number of rows and columns.
        The agent starts in the middle of the grid.
        """
        self.rows = rows  # Number of rows in the grid
        self.cols = cols  # Number of columns in the grid
        # Create a grid filled with empty spaces
        self.grid = [[' ' for _ in range(cols)] for _ in range(rows)]
        # Set the initial position of the agent in the middle of the grid
        self.agent_position = (rows // 2, cols // 2)
        # Place the agent (represented by 'A') in the grid
        self.grid[self.agent_position[0]][self.agent_position[1]] = 'A'

    def display_grid(self):
        """
        Display the current state of the grid.
        """
        for row in self.grid:
            print(' '.join(row))  # Print each row of the grid
        print()  # Print a new line for better readability

    def move_agent(self, direction):
        """
        Move the agent in the specified direction.
        Valid directions are 'up', 'down', 'left', and 'right'.
        """
        # Get the current position of the agent
        x, y = self.agent_position
        # Clear the current position of the agent in the grid
        self.grid[x][y] = ' '

        # Move the agent based on the specified direction
        if direction == 'up' and x > 0:  # Move up if not at the top edge
            x -= 1
        elif direction == 'down' and x < self.rows - 1:  # Move down if not at the bottom edge
            x += 1
        elif direction == 'left' and y > 0:  # Move left if not at the left edge
            y -= 1
        elif direction == 'right' and y < self.cols - 1:  # Move right if not at the right edge
            y += 1

        # Update the agent's position
        self.agent_position = (x, y)
        # Place the agent in the new position in the grid
        self.grid[x][y] = 'A'

# Create an instance of GridWorld
grid_world = GridWorld()

# Display the initial state of the grid
grid_world.display_grid()

# Move the agent up and display the grid
grid_world.move_agent('up')
grid_world.display_grid()

# Move the agent left and display the grid
grid_world.move_agent('left')
grid_world.display_grid()