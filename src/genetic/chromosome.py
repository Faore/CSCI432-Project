from random import randrange, choice
import numpy as np


class Chromosome:
    def __init__(self, colorings, k):
        # List of colorings for each state
        self.colorings = colorings

        # Number of colors being used
        self.k = k

    @staticmethod
    def generate_chromosome(nodes, k):
        colorings = []
        for i in range(nodes):
            # Give state random color initially
            colorings.append(randrange(0, k))
        return Chromosome(colorings, k)

    def calculate_fitness(self, adjacency_matrix):
        conflicts = 0
        for node, color in enumerate(self.colorings):
            if not self.is_colorable(node, color, adjacency_matrix):
                conflicts += 1
        return conflicts

    def is_colorable(self, node, color, adjacency_matrix):
        for index, adjacent in enumerate(adjacency_matrix[node]):
            if adjacent and self.colorings[index] == color:
                return False
        return True

    def mutate(self, adjacency_matrix):
        for node, color in enumerate(self.colorings):
            if not self.is_colorable(node, color, adjacency_matrix):
                self.colorings[node] = list(range(0, self.k).remove(color))
