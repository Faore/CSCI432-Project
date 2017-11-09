import numpy as np

class graph_import:

    @staticmethod
    def adjacency_list_from_file(path):
        file = open(path, 'r')
        adjacency_list = {}
        for line in file:
            s = line.split(":")
            p = s[1].split(",")
            adjacency_list[int(s[0])] = []
            for i in p:
                adjacency_list[int(s[0])].append(int(i))
        print(adjacency_list)
        return adjacency_list

    @staticmethod
    def adjacency_matrix_from_file(path):
        adjacency_matrix = (np.zeros((48, 48), dtype=int))
        i = 0
        np.set_printoptions(threshold=np.inf)
        with open('adjacency_list.txt', 'r') as f:

            for i in range(48):

                line = f.readline()
                line = line.split(':')[1].replace('\n', '').replace(' ', '')
                line = line.split(',')
                # print(line)
                j = 0
                for vertex in range(len(line)):
                    adjacency_matrix[i, int(line[j]) - 1] = 1
                    j = j + 1
        return adjacency_matrix
