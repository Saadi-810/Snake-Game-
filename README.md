## Snake Game with Genetic Algorithm
This project implements a classic Snake game using Pygame, integrated with a genetic algorithm (GA) to evolve strategies for playing the game. The snake navigates a grid to eat food, growing longer with each food consumed, and the game ends if the snake collides with itself or the grid boundaries. The GA aims to evolve a sequence of actions to guide the snake, while A* pathfinding is used to move the snake toward food.
Features

# Snake Game
A grid-based Snake game implemented with Pygame, featuring a snake that grows when eating food and ends on collision.
A Pathfinding: The snake uses A algorithm to find the shortest path to food, ensuring optimal movement.
Genetic Algorithm: Evolves a population of action sequences (genomes) to guide the snake, with fitness based on game performance (food eaten and survival).
Visualization: Renders the game using Pygame, displaying the snake and food on a grid.

## Installation
Clone the Repository:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


Install Dependencies:Ensure Python 3.6+ is installed. Install required packages using pip:
```bash
pip install pygame numpy
```

Run the Game:Execute the main script to run the genetic algorithm and visualize the best individual's game:
```bash
python main.py
```
## Usage
- Run main.py to start the genetic algorithm, which evolves a population over 10 generations (configurable in genetic_algorithm.py).
- The GA evaluates each individual's fitness based on the Snake game's rewards: +1 for eating food, -1 for dying, 0 for moving.
- After evolution, the best individual (highest fitness) is used to play a visualized game using Pygame.
- The game window shows the snake (green, fading with length) moving toward food (red) on a 20x20 grid. The game runs at 10 FPS and ends on collision.

## File Structure

- vector.py: Defines a Vector class for 2D coordinates, used for snake positions, food, and directions.
- snake_game.py: Implements the Snake game with Pygame, including A* pathfinding to guide the snake to food.
- genetic_algorithm.py: Contains the genetic algorithm to evolve action sequences, with methods for fitness evaluation, selection, crossover, and mutation.
- main.py: Runs the GA and visualizes the best individual's game. (Note: Duplicates the main block in genetic_algorithm.py.)
- README.md: This file, providing project documentation.

## How It Works

### Genetic Algorithm:
- Initializes a population of 100 individuals, each a sequence of 100 actions (0, 1, or 2).
- Evaluates fitness by simulating the Snake game for each individual, accumulating rewards.
- Uses fitness-proportional selection, single-point crossover, and mutation (1% rate) to create new generations.
- Runs for 10 generations, printing the best fitness per generation.

### Snake Game:
- The snake moves on a 20x20 grid, starting at the center, with food placed randomly.
- A* pathfinding calculates the shortest path to food, updating the snake's direction.
- Rewards: +1 for eating food (grows snake, repositions food), -1 for collision (game over), 0 for normal moves.

### Visualization:
After GA evolution, the best individual's game is rendered with Pygame until the snake dies.

### Requirements
- Python 3.6+
- Pygame (pip install pygame)
- NumPy (pip install numpy)

# License
This project is licensed under the MIT License. See the LICENSE file for details.
Contributing
Contributions are welcome! Please submit a pull request or open an issue for bugs, improvements, or new features.
