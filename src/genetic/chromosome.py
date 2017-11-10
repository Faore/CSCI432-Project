from random import randrange, choice


class Chromosome:

    def __init__(self, colorings, k):
        self.colorings = colorings
        self.k = k

    @staticmethod
    def generate_chromosome(nodes, k):
        colorings = []
        for i in range(nodes):
            colorings.append(randrange(0, k))
        return Chromosome(colorings, k)

    def calculate_fitness(self, adjacency_matrix):
        conflicts = 0;
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
                self.colorings[node] = choice(list(range(0, self.k)).remove(color))
