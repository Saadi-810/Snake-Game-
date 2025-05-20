import numpy as np
from snake_game import SnakeGame

class GeneticAlgorithm:
    def __init__(self, population_size=100, mutation_rate=0.01, genome_length=100):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.genome_length = genome_length
        self.population = [np.random.choice([0, 1, 2], size=genome_length) for _ in range(population_size)]

    def evaluate_fitness(self, individual):
        game = SnakeGame()
        fitness = 0
        for action in individual:
            reward = game.step()
            if reward == -1:
                break
            fitness += reward
        return fitness

    def select_parents(self):
        fitness_scores = np.array([self.evaluate_fitness(individual) for individual in self.population])
        total_fitness = np.sum(fitness_scores)
        if total_fitness == 0:
            probs = np.ones(len(self.population)) / len(self.population)
        else:
            probs = fitness_scores / total_fitness
        parents_indices = np.random.choice(len(self.population), size=self.population_size, p=probs)
        return [self.population[i] for i in parents_indices]

    def crossover(self, parent1, parent2):
        point = np.random.randint(1, len(parent1))
        return np.concatenate((parent1[:point], parent2[point:]))

    def mutate(self, individual):
        for i in range(len(individual)):
            if np.random.rand() < self.mutation_rate:
                individual[i] = np.random.choice([0, 1, 2])
        return individual

    def create_next_generation(self):
        parents = self.select_parents()
        next_generation = []
        for i in range(0, self.population_size, 2):
            parent1, parent2 = parents[i], parents[i+1]
            child1, child2 = self.crossover(parent1, parent2), self.crossover(parent2, parent1)
            next_generation.extend([self.mutate(child1), self.mutate(child2)])
        self.population = next_generation

    def run(self, generations=10):
        for generation in range(generations):
            print(f'Generation {generation+1}')
            self.create_next_generation()
            best_fitness = max([self.evaluate_fitness(individual) for individual in self.population])
            print(f'Best fitness: {best_fitness}')

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
