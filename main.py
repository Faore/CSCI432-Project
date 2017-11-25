# libraries
import pandas as pd
import numpy as np
# import networkx as nx
import matplotlib.pyplot as plt
import random
import json
import os
import re

from graphsystem.graph_import import *
from src.genetic.genetic import Genetic

'''This module runs the genetic algorithm and converts the result to dictionary of hex colors for each state.
   The dictionary is written to a html file which can be run in a browser to display the visualization.'''

# Dictionary mapping indices to states
num_to_states = {1: 'WA', 2:'OR', 3: 'CA', 4:'ID', 5: 'NV', 6:'AZ', 7: 'MT', 8: 'WY', 9: 'UT', 10: 'NM', 11: 'CO', 12: 'ND',
                 13:'SD', 14:'NE', 15:'KS', 16: 'OK', 17:'TX', 18:'MN', 19:'IA',20:'MO', 21:'AR', 22: 'LA', 23: 'WI',24:'IL',25:'KY',
                 26:'TN', 27:'MS', 28:'MI', 29:'IN', 30:'AL', 31:'OH',32:'WV', 33:'VA', 34:'NC',35:'SC',36:'GA',37:'FL',38:'PA',39:'MD',
                 40:'DE',41:'NJ',42:'NY',43:'VT',44:'NH',45:'MA',46:'CT',47:'RI',48:'ME'
                 }

# Create adjacency matrix from text file
adjacency_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'adjacency_list.txt')
adjacency_list = graph_import.adjacency_list_from_file(adjacency_file)
adjacency_matrix = graph_import.adjacency_matrix_from_file(adjacency_file)

# Colors to use in visualization
color_list = ['#1039DF', '#DF101D', '#E5EEF3', '#39A034']

# Run the GA, (adjacency, number of colors, population size, max generations, mutation probability)
alg = Genetic(adjacency_matrix, 4, 500, 100, 0.3)
result = alg.run()

# Create Visualization
if result is not None:
    soln_history = np.array(result)

    dictionary_colorings = {}
    for key, state in num_to_states.items():
        # Get color history for the current state
        state_colors = soln_history[:, key-1]

        # Map integers to colors
        hex_colorings = []
        for color in state_colors:
            hex_colorings.append(color_list[color])

        # Save color history for the current state
        dictionary_colorings[state] = hex_colorings

    json_data = json.dumps(dictionary_colorings)

    file = open("states.html", "r")
    file_str = file.read()
    file.close()

    file_str = re.sub("\/\/START:COLORS\n.*\n*\t*\/\/END:COLORS", "//START:COLORS\nvar colors = " + json_data + ";\n//END:COLORS", file_str)

    open("states.html", "w").write(file_str)
else:
    print("Solution not found!")


# origin = []
# destination = []
# for state in adjacency_list:
#     #print(num_to_states[state])
#     #origin.append(num_to_states[state])
#     dest = adjacency_list[state]
#     for j in range(len(dest)):
#         origin.append(num_to_states[state])
#         destination.append(num_to_states[dest[j]])
#
# #df = pd.DataFrame({'from': ['Au', 'Bs', 'Cd', 'Au'], 'to': ['D', 'Au', 'E', 'Cd']})
#
# # Build a dataframe with your connections,
# df = pd.DataFrame({'from': origin, 'to': destination})
#
# # And a data frame with characteristics for your nodes
# #carac = pd.DataFrame({'ID': ['Au', 'Bs', 'Cd', 'D', 'E'], 'myvalue': ['group1', 'group1', 'group2', 'group3', 'group3']})
#
# states =[]
# group_choices = [0,1,2,3]
# groupes = result
#
# for state in num_to_states:
#     states.append(num_to_states[state])
# #    groupes.append(random.choice(group_choices))
#
# carac = pd.DataFrame({'ID': states, 'myvalue': groupes})
#
#
# # Build your graph
# G = nx.from_pandas_dataframe(df, 'from', 'to', create_using=nx.Graph())
#
# # The order of the node for networkX is the following order:
# G.nodes()
# # Thus, we cannot give directly the 'myvalue' column to netowrkX, we need to arrange the order!
#
# # Here is the tricky part: I need to reorder carac to assign the good color to each node
# carac = carac.set_index('ID')
# carac = carac.reindex(G.nodes())
#
# # And I need to transform my categorical column in a numerical value: group1->1, group2->2...
# carac['myvalue'] = pd.Categorical(carac['myvalue'])
# carac['myvalue'].cat.codes
#
# pos= nx.spring_layout(G,scale=2)
#
# #pos = nx.random_layout(G)
#
#
# # Custom the nodes:
# nx.draw(G, with_labels=True, node_color=carac['myvalue'].cat.codes, cmap=plt.cm.Set1, node_size=150, pos= nx.spring_layout(G,scale=2))
#
#
# plt.show()