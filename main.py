import pygame
from snake_game import SnakeGame
from genetic_algorithm import GeneticAlgorithm

if __name__ == '__main__':
    ga = GeneticAlgorithm()
    ga.run()
    best_individual = max(ga.population, key=lambda ind: ga.evaluate_fitness(ind))

    game = SnakeGame()
    while not game.game_over:
        pygame.event.pump()  # Process event queue to keep window responsive
        game.update_direction()
        game.step()
        game.draw()

    game.close()
