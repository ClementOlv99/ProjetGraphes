import csv
import networkx as nx
import matplotlib.pyplot as plt

data = []

with open('topology_avg.csv', newline='') as csvfile:

    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    for row in spamreader: 

        data.append(row[0].split(','))

data.pop(0)

G = nx.Graph()

for elti in data:
    G.add_node(int(elti[0]))

nx.draw(G)