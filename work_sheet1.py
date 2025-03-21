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
        self.agentPosition = (rows // 2, cols // 2)
        # Place the agent (represented by 'A') in the grid
        self.grid[self.agentPosition[0]][self.agentPosition[1]] = 'A'

    def moveAgentWest(self):
        """
        Move the agent one step to the left (west). If the agent is at the western boundary,
        it will print a message and not move.
        """
        current_row, current_col = self.agentPosition  # Get the current position of the agent

        if current_col > 0:
            # Clear the current position
            self.grid[current_row][current_col] = ' '
            # Move west
            current_col -= 1
            # Mark the new position
            self.grid[current_row][current_col] = 'A'
            # Update the agent's position
            self.agentPosition = (current_row, current_col)
        else:
            print("Agent can't be moved to the west, agent is at the left of the grid.")

    def moveAgentWestBouncy(self):
        """
        Move the agent one step to the left (west). If the agent is at the western boundary,
        it will print a message and stay in the same position.
        """
        current_row, current_col = self.agentPosition  # Get the current position of the agent

        if current_col > 0:
            # Clear the current position
            self.grid[current_row][current_col] = ' '
            # Move west
            current_col -= 1
            # Mark the new position
            self.grid[current_row][current_col] = 'A'
            # Update the agent's position
            self.agentPosition = (current_row, current_col)
        else:
            print("Agent is at the western boundary, bouncing back.")

    def moveNorthAroundTheWorld(self):
        """
        Move the agent one step to the north (up). If the agent moves off the top edge,
        it will wrap around to the bottom of the grid.
        """
        current_row, current_col = self.agentPosition  # Get the current position of the agent
        # Move north (up)
        current_row -= 1
        # Wrap around if moving off the top edge
        if current_row < 0:
            current_row = self.rows - 1  # Wrap to the bottom
        # Clear the current position
        self.grid[self.agentPosition[0]][self.agentPosition[1]] = ' '
        # Mark the new position
        self.grid[current_row][current_col] = 'A'
        # Update the agent's position
        self.agentPosition = (current_row, current_col)

    def displayGrid(self):
        """
        Display the current state of the grid.
        """
        for row in self.grid:
            print(' '.join(row))  # Print each row of the grid
        print()  # Print a new line for better readability

    def moveAgent(self, direction):
        """
        Move the agent in the specified direction.
        Valid directions are 'up', 'down', 'left', and 'right'.
        """
        # Get the current position of the agent
        x, y = self.agentPosition
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
        self.agentPosition = (x, y)
        # Place the agent in the new position in the grid
        self.grid[x][y] = 'A'

# Create an instance of GridWorld
grid_world = GridWorld()

# Display the initial state of the grid
grid_world.displayGrid()

# Move the agent up and display the grid
grid_world.moveAgent('up')
grid_world.displayGrid()

# Move the agent left and display the grid
grid_world.moveAgent('left')
grid_world.displayGrid()