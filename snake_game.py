import pygame
import random
import heapq
from vector import Vector

class SnakeGame:
    def __init__(self, grid_size=20, scale=20):
        self.grid = Vector(grid_size, grid_size)
        self.scale = scale
        self.snake = [Vector(grid_size // 2, grid_size // 2)]
        self.food = self.random_food_position()
        self.direction = Vector(0, -1)
        self.score = 0
        self.game_over = False
        self.path = []

        pygame.init()
        self.screen = pygame.display.set_mode((self.grid.x * self.scale, self.grid.y * self.scale))
        self.clock = pygame.time.Clock()

    def random_food_position(self):
        empty_positions = {Vector(x, y) for x in range(self.grid.x) for y in range(self.grid.y)} - set(self.snake)
        return random.choice(list(empty_positions))

    def neighbors(self, node):
        directions = [Vector(0, 1), Vector(1, 0), Vector(0, -1), Vector(-1, 0)]
        result = []
        for direction in directions:
            neighbor = node + direction
            if 0 <= neighbor.x < self.grid.x and 0 <= neighbor.y < self.grid.y and neighbor not in self.snake:
                result.append(neighbor)
        return result

    def heuristic(self, a, b):
        return abs(a.x - b.x) + abs(a.y - b.y)

    def a_star(self, start, goal):
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, goal)}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.reverse()
                return path

            for neighbor in self.neighbors(current):
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + self.heuristic(neighbor, goal)
                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return []

    def step(self):
        if self.path:
            next_position = self.path.pop(0)
            self.direction = Vector(next_position.x - self.snake[0].x, next_position.y - self.snake[0].y)

        new_head = self.snake[0] + self.direction

        if new_head in self.snake or new_head.x < 0 or new_head.x >= self.grid.x or new_head.y < 0 or new_head.y >= self.grid.y:
            self.game_over = True
            return -1  # Penalty for dying

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.food = self.random_food_position()
            self.path = self.a_star(self.snake[0], self.food)  # Recalculate path to new food
            return 1  # Reward for eating food
        else:
            self.snake.pop()
            return 0

    def update_direction(self):
        if not self.path:
            self.path = self.a_star(self.snake[0], self.food)

    def draw(self):
        self.screen.fill((0, 0, 0))
        for i, part in enumerate(self.snake):
            color = max(0, 255 - i * 10)
            pygame.draw.rect(self.screen, (0, color, 0), (part.x * self.scale, part.y * self.scale, self.scale, self.scale))
        pygame.draw.rect(self.screen, (255, 0, 0), (self.food.x * self.scale, self.food.y * self.scale, self.scale, self.scale))
        pygame.display.flip()
        self.clock.tick(10)

    def close(self):
        pygame.quit()
