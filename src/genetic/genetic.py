from genetic.chromosome import Chromosome
from random import shuffle, randrange


class Genetic:
    def __init__(self, adjacency_matrix, k, population_size, limit, mutation_probability):
        self.adjacency_matrix = adjacency_matrix
        self.k = k
        self.population_size = population_size
        self.limit = limit
        self.current_population = []
        self.mutation_probability = mutation_probability
        self.iterations = 0
        self.population_archive = []

    def run(self):
        self.generate_initial_population()

        while self.check_for_solution_from_population() is None and self.iterations < self.limit:
            self.tournament_selection()
            self.breed_population()
            self.iterations += 1

        return self.check_for_solution_from_population().colorings or False

    def generate_initial_population(self):
        self.current_population = []
        for i in range(self.population_size):
            self.current_population.append(Chromosome.generate_chromosome(len(self.adjacency_matrix), self.k))

    def check_for_solution_from_population(self):
        for c in self.current_population:
            if c.calculate_fitness(self.adjacency_matrix):
                return c
        return None

    def breed_population(self):
        old_population = self.current_population
        self.current_population = []

        shuffle(old_population)

        # If the population happens to be odd for some weird reason, using a check for greater than one prevents us from
        # entering a case where the algorithm tries to breed more chromosomes than available.
        while len(old_population) > 1:
            first = old_population.pop()
            second = old_population.pop()
            self.current_population += self.crossover_and_mutation(first, second)

    def tournament_selection(self):
        old_population = self.current_population
        self.current_population = []

        shuffle(old_population)

        while len(old_population) > 1:
            first = old_population.pop()
            second = old_population.pop()

            if first.calculate_fitness() > second.calculate_fitness():
                self.current_population.append(second)
            else:
                self.current_population.append(first)

    def crossover_and_mutation(self, first, second):
        crossover_point = randrange(0, len(self.adjacency_matrix))

        first_half1 = first.colorings[:crossover_point]
        first_half2 = first.colorings[crossover_point:]

        second_half1 = second.colorings[:crossover_point]
        second_half2 = second.colorings[crossover_point:]

        children = [Chromosome(first_half1 + second_half2, self.k), Chromosome(second_half1 + first_half2, self.k)]
        for child in children:
            if randrange(0, int(self.mutation_probability * 100)) == 0:
                child.mutate(self.adjacency_matrix)
