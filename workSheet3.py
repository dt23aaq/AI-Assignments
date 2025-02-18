import random

# Task 1: Basic Agent Movement
world_task1 = [
    ["north", "north", "north", "north", "west"],
    ["north", "north", "north", "north", "west"],
    ["north", "north", "goal", "west", "west"],
    ["north", "north", "south", "south", "south"],
    ["east", "east", "south", "south", "south"]
]

class Agent:
    def __init__(self, x, y):
        self.x = x  # Row position
        self.y = y  # Column position

    def perceive_label(self, world):
        return world[self.x][self.y]

    def move(self, direction):
        if direction == "north":
            self.x -= 1
        elif direction == "south":
            self.x += 1
        elif direction == "east":
            self.y += 1
        elif direction == "west":
            self.y -= 1

def main():
    agent = Agent(2, 2)
    while True:
        current_label = agent.perceive_label(world_task1)
        if current_label == "goal":
            break
        agent.move(current_label)
        if agent.x < 0 or agent.x >= 5 or agent.y < 0 or agent.y >= 5:
            break

# Task 2: Mini Controller
def mini_controller(agent, world):
    while True:
        label = agent.perceive_label(world)
        if label == "goal":
            break
        agent.move(label)
        if agent.x < 0 or agent.x >= 5 or agent.y < 0 or agent.y >= 5:
            break

# Task 3: Hierarchical Controller
def hierarchical_controller(agent, world):
    while True:
        goal_label = agent.perceive_label(world)
        if goal_label == "goal":
            break
        direction_label = agent.perceive_label(world)
        agent.move(direction_label)
        if agent.x < 0 or agent.x >= 5 or agent.y < 0 or agent.y >= 5:
            break

# Task 4: Random Movement
world_size = 5
world_task4 = [[None for _ in range(world_size)] for _ in range(world_size)]
corners = [(0, 0), (0, world_size - 1), (world_size - 1, 0), (world_size - 1, world_size - 1)]
goal_position = random.choice(corners)
world_task4[goal_position[0]][goal_position[1]] = "goal"

print("Task 4: World with goal:")
for row in world_task4:
    print(row)

class RandomAgent(Agent):
    def move_random(self):
        directions = ["north", "south", "east", "west"]
        direction = random.choice(directions)
        if direction == "north":
            self.x -= 1
        elif direction == "south":
            self.x += 1
        elif direction == "east":
            self.y += 1
        elif direction == "west":
            self.y -= 1

def get_random_position():
    while True:
        x = random.randint(0, world_size - 1)
        y = random.randint(0, world_size - 1)
        if (x, y) != goal_position:
            return x, y

def random_movement_controller(agent, world):
    steps = 0
    while True:
        steps += 1
        goal_label = agent.perceive_label(world)
        if goal_label == "goal":
            break
        agent.move_random()
        if agent.x < 0 or agent.x >= world_size or agent.y < 0 or agent.y >= world_size:
            break

# Run all tasks
if __name__ == "__main__":
    # Task 1
    main()

    # Task 2
    agent_task2 = Agent(2, 2)
    mini_controller(agent_task2, world_task1)

    # Task 3
    agent_task3 = Agent(2, 2)
    hierarchical_controller(agent_task3, world_task1)

    # Task 4
    agent_task4 = RandomAgent(*get_random_position())
    random_movement_controller(agent_task4, world_task4)