"""
Initialize the GridWorld with a specified number of rows and columns.
        The agent starts in the middle of the grid.
"""
class GridWorld:

    def move_agent_west(self):
        """
        Move the agent one step to the left (west).
        """
        x, y = self.agent_position
        if y > 0:  # Ensure the agent doesn't move out of bounds
            self.grid[x][y] = ' '  # Clear the current position
            y -= 1  # Move left
            self.grid[x][y] = 'A'  # Place the agent in the new position
            self.agent_position = (x, y)  # Update the agent's position

    def __init__(self, rows=5, cols=5):
        self.rows = rows
        self.cols = cols
        self.grid = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.agent_position = (rows // 2, cols // 2)
        self.grid[self.agent_position[0]][self.agent_position[1]] = 'A'

    def display_grid(self):
        """
        Display the current state of the grid.
        """
        for row in self.grid:
            print(' '.join(row))
        print()

    def move_agent(self, direction):
        """
        Move the agent in the specified direction.
        Valid directions are 'up', 'down', 'left', and 'right'.
        """
        x, y = self.agent_position
        self.grid[x][y] = ' '

        if direction == 'up' and x > 0:
            x -= 1
        elif direction == 'down' and x < self.rows - 1:
            x += 1
        elif direction == 'left' and y > 0:
            y -= 1
        elif direction == 'right' and y < self.cols - 1:
            y += 1

        self.agentPosition = (x, y)
        self.grid[x][y] = 'A'

## This function
grid_world = GridWorld()
grid_world.display_grid()
grid_world.move_agent('up')
grid_world.display_grid()
grid_world.move_agent('left')
grid_world.display_grid()