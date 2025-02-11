# QUESTION 1✨

# Define the Agent class
class Agent:
    def __init__(self, x, y):
        # The agent starts at a specific position (x, y)
        self.x = x  # Row position
        self.y = y  # Column position

    def get_position(self):
        # Returns the current position of the agent
        return self.x, self.y


# Function to create the grid
def create_grid(size, agent, leaf_position):
    # Create a grid filled with "_" (empty spaces)
    grid = []
    for row in range(size):
        grid.append(["_"] * size)  # Add a row of empty spaces

    # Place the agent on the grid
    grid[agent.x][agent.y] = "A"  # "A" represents the agent

    # Place the leaf on the grid
    grid[leaf_position[0]][leaf_position[1]] = "L"  # "L" represents the leaf

    return grid


# Function to print the grid
def print_grid(grid):
    print("Current Grid:")
    for row in grid:
        print(" ".join(row))  # Print each row as a string
    print()


# Main program
if __name__ == "__main__":
    # Initialize the agent at the center of a 5x5 grid
    agent = Agent(2, 2)  # Agent starts at row 2, column 2

    # Place the leaf to the right of the agent
    leaf_position = (2, 3)  # Leaf is at row 2, column 3

    # Create the grid
    grid = create_grid(5, agent, leaf_position)

    # Print the initial grid
    print("Welcome to the Agent and Leaf World!")
    print_grid(grid)

    # Print the agent's current position
    print("Agent's curret position:", agent.get_position())

    
# OUTPUT
#Welcome to the Agent and Leaf World!
#Current Grid:
#_ _ _ _ _
#_ _ _ _ _
#_ _ A L _
#_ _ _ _ _
#_ _ _ _ _

#Agent's current position: (2, 2)



# QUESTION 2 ✨

# Below define the Agent class
class Agent:
    def __init__(self, x, y):
        # The agent starts at a specific position (x, y) I use x & y to keep track of the array indexes of the string.
        self.x = x
        self.y = y

    def get_position(self):
        # Returns the current position of the agent
        return self.x, self.y

    def move(self, direction, grid):
        # Move the agent in the specified direction
        if direction == "W":  # Move West (left)
            if self.y > 0:  # Check if the agent is not at the left edge
            grid[self.x][self.y] = "_"  # Clear the current position
                self.y -= 1  # Move left
            else:
                print("Oops! Can't move further West. You hit the wall!")
        elif direction == "E":  # Move East (right)
            if  self.y < len(grid[0]) - 1:  # Check if the agent is not at the right edge
                grid[self.x][self.y] = "_"  # Clear the current position
                self.y += 1  # Move right
            else:
                print("Oops! Can't move further East. You hit the wall!")
        elif direction == "N":  # Move North (up)
            if self.x > 0:  # Check if the agent is not at the top edge
                grid[self.x][self.y] = "_"  # Clear the current position
                self.x -= 1  # Move up
            else:
                print("Oops! Can't moe further North. You hit the wall!")
        elif direction == "S":  # Move South (down)
            if self.x < len(grid) - 1:  # Check if the agent is not at the bottom edge
                grid[self.x][self.y] = "_"  # Clear the current position
                self.x += 1  # Move down
            else:
                print("Oops! Can't move further South. You hit the wall!")
        else:
            print("Invalid direction! Use 'W', 'E', 'N', or 'S'.")

        # Update the agent's new position on the grid
        grid[self.x][self.y] = "A"


# Function to create the grid
def create_grid(size, agent, leaf_position):
    # Create a grid filled with "_" (empty spaces)
    grid = [["_" for _ in range(size)] for _ in range(size)]
    # Place the agent on the grid
    grid[agent.x][agent.y] = "A"
    # Place the leaf on the grid
    grid[leaf_position[0]][leaf_position[1]] = "L"
    return grid


# Function to print the grid
def print_grid(grid):
    print("Current Grid:")
    for row in grid:
        print(" ".join(row))  # Print each row as a string
    print()


# Main program
if __name__ == "__main__":
    # Initialize the agent at the center of the 5x5 grid
    agent = Agent(2, 2)
    # Place the leaf to the right of the agent
    leaf_position = (2, 3)

    # Create the grid
    grid = create_grid(5, agent, leaf_position)

    # Added prin for the initial grid
    print("Welcome to the Agent and Leaf World!✨")
    print_grid(grid)

    # Let the user move the agent
    while True:
        direction = input("Enter a direction to move (W: West, E: East, N: North, S: South, Q: Quit): ").strip().upper()
        if direction == "Q":
            print("Goodbye! Thanks for playing. :)")
            break
        elif direction in ["W", "E", "N", "S"]:
            agent.move(direction, grid)  # Move the agent
            print_grid(grid)  # Show the updated grid
        else:
            print("Invalid input! Please enter W, E, N, S, or Q. :(")


# QUESTION 3 ✨

# Define the Agent class
class Agent:
    def __init__(self, x, y):
        # The agent starts at a specific position (x, y)
        self.x = x
        self.y = y

    def move(self, direction, grid):
        # Calculate the new position based on the direction
        new_x, new_y = self.x, self.y
        if direction == "W":  # Move West (left)
            new_y -= 1
        elif direction == "E":  # Move East (right)
            new_y += 1
        elif direction == "N":  # Move North (up)
            new_x -= 1
        elif direction == "S":  # Move South (down)
            new_x += 1
        else:
            print("Invalid direction! Use 'W', 'E', 'N', or 'S'.")
            return

        # Check if the new position is outside the grid (bouncy borders)
        if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]):
            print("Oops! Can't move further. You hit the wall!")
            return

        # Check if the new position has a leaf
        if grid[new_x][new_y] == "L":
            # Push the leaf in the same direction
            leaf_new_x, leaf_new_y = new_x, new_y
            if direction == "W":
                leaf_new_y -= 1
            elif direction == "E":
                leaf_new_y += 1
            elif direction == "N":
                leaf_new_x -= 1
            elif direction == "S":
                leaf_new_x += 1

            # Check if the leaf is pushed outside the grid
            if leaf_new_x < 0 or leaf_new_x >= len(grid) or leaf_new_y < 0 or leaf_new_y >= len(grid[0]):
                print("The leaf was pushed off the grid and is gone!")
                grid[new_x][new_y] = "_"  # Remove the leaf
            else:
                # Move the leaf to its new position
                grid[leaf_new_x][leaf_new_y] = "L"
                grid[new_x][new_y] = "_"  # Clear the leaf's old position

        # Move the agent to the new position
        grid[self.x][self.y] = "_"  # Clear the agent's old position
        self.x, self.y = new_x, new_y  # Update the agent's position
        grid[self.x][self.y] = "A"  # Place the agent in the new position


# Function to create the grid
def create_grid(size, agent, leaf_position):
    # Create a grid filled with "_" (empty spaces)
    grid = [["_" for _ in range(size)] for _ in range(size)]
    # Place the agent on the grid
    grid[agent.x][agent.y] = "A"
    # Place the leaf on the grid
    grid[leaf_position[0]][leaf_position[1]] = "L"
    return grid


# Function to print the grid
def print_grid(grid):
    print("Current Grid:")
    for row in grid:
        print(" ".join(row))  # Print each row as a string
    print()


# Main program
if __name__ == "__main__":
    # Initialize the agent at the center of a 5x5 grid
    agent = Agent(2, 2)
    # Place the leaf to the right of the agent
    leaf_position = (2, 3)

    # Create the grid
    grid = create_grid(5, agent, leaf_position)

    # Print the initial grid
    print("Welcome to the Agent and Leaf World!✨")
    print_grid(grid)

    # Let the user move the agent
    while True:
        direction = input("Enter a direction to move (W: West, E: East, N: North, S: South, Q: Quit): ").strip().upper()
        if direction == "Q":
            print("Goodbye! Thanks for playing.:) ✨")
            break
        elif direction in ["W", "E", "N", "S"]:
            agent.move(direction, grid)  # Move the agent
            print_grid(grid)  # Show the updated grid
        else:
            print("Invalid input! Please enter W, E, N, S, or Q.")
