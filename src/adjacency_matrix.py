import numpy as np

adjacency_matrix = (np.zeros((48,48), dtype= int))
i=0
np.set_printoptions(threshold=np.inf)
with open('adjacency_list.txt','r') as f:

   for i in range(48):

    line = f.readline()
    line = line.split(':')[1].replace('\n','').replace(' ','')
    line = line.split(',')
    #print(line)
    j=0
    for vertex in range(len(line)):
        adjacency_matrix[i,int(line[j])-1] = 1
        j = j + 1

print(adjacency_matrix)