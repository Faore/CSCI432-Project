from graphsystem.graph_import import *
from genetic.genetic import Genetic
import json
import re

num_to_states = {1: 'WA', 2:'OR', 3: 'CA', 4:'ID', 5: 'NV', 6:'AZ', 7: 'MT', 8: 'WY', 9: 'UT', 10: 'NM', 11: 'CO', 12: 'ND',
                 13:'SD', 14:'NE', 15:'KS', 16: 'OK', 17:'TX', 18:'MN', 19:'IA',20:'MO', 21:'AR', 22: 'LA', 23: 'WI',24:'IL',25:'KY',
                 26:'TN', 27:'MS', 28:'MI', 29:'IN', 30:'AL', 31:'OH',32:'WV', 33:'VA', 34:'NC',35:'SC',36:'GA',37:'FL',38:'PA',39:'MD',
                 40:'DE',41:'NJ',42:'NY',43:'VT',44:'NH',45:'MA',46:'CT',47:'RI',48:'ME'
                 }

adjacency_file = "../data/adjacency_list.txt"
adjacency_list = graph_import.adjacency_list_from_file(adjacency_file)
adjacency_matrix = graph_import.adjacency_matrix_from_file(adjacency_file)

color_list = ['#28B69A', '#B428B6', '#B62844', '#B2B628', '#CB4B16', '#DC322F', '#6C71C4', '#859900', '#2869B6', '#42B628']

alg = Genetic(adjacency_matrix, 4, 100, 100, 0.3)
result = alg.run()
print(result)

hex_colorings = []

if result is not None:
    for n in result:
        hex_colorings.append(color_list[n])
    #print(hex_colorings)
    dictionary_colorings = {}


    for i, col in enumerate(hex_colorings):
        dictionary_colorings[num_to_states[i+1]] = [col]

    json_data = json.dumps(dictionary_colorings)

    file = open("states.html", "r")
    file_str = file.read()
    file.close()

    file_str = re.sub("\/\/START:COLORS\n.*\n*\t*\/\/END:COLORS", "//START:COLORS\nvar colors = " + json_data + ";\n//END:COLORS", file_str)

    open("states.html", "w").write(file_str)
else:
    print("Solution not found!")