from graphsystem.graph_import import *
from genetic.genetic import Genetic
from genetic.chromosome import Chromosome

adjacency_file = "../data/adjacency_list.txt"
adjacency_list = graph_import.adjacency_list_from_file(adjacency_file)
adjacency_matrix = graph_import.adjacency_matrix_from_file(adjacency_file)

print(Chromosome.generate_chromosome(10, 4).colorings)