class graph_import:

    adjacency_list = {}

    def import_graph_from_file(self, path):
        file = open(path, 'r')
        for line in file:
            s = line.split(":")
            p = s[1].split(",")
            self.adjacency_list[int(s[0])] = []
            for i in p:
                self.adjacency_list[int(s[0])].append(int(i))
        print(self.adjacency_list)