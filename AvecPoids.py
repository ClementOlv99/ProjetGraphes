import csv
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import *


def norme3(x, y):
    return sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2 + (x[2]-y[2])**2)


def CreerGraphe(nomFichier, range):

    data = []

    # On récupère les données du csv dans un tableau de string

    with open(nomFichier, newline='') as csvfile:

        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        for row in spamreader: 

            data.append(row[0].split(','))



    # On élimine la première ligne 

    data.pop(0)


    # On crée le graphe, on ajoute les noeud, puis les liens qui respecte la contrainte

    G = nx.Graph()

    for elti in data:
        G.add_node(int(elti[0]), x = float(elti[1]), y = float(elti[2]), z = float(elti[3]))
        for eltj in data:
            dist = norme3([float(elti[1]), float(elti[2]), float(elti[3])], [float(eltj[1]), float(eltj[2]), float(eltj[3])])
            if (elti[0] != eltj[0]) and  (dist <= range):
                G.add_weighted_edges_from((int(elti[0]), int(eltj[0]), dist))
    return G


def degré_moyen(G):
    return (G.number_of_edges()/G.number_of_nodes())


def distribution_degré(G):
    maxD = 0
    nb = G.number_of_nodes()

    for node in G.nodes():
        if G.degree(node) > maxD:
            maxD = G.degree(node)


    tab = [0 for i in range(maxD + 1)]

    for node in G.nodes():
        tab[G.degree(node)] += 1

    for i in range(len(tab)):
        tab[i] = tab[i]/nb
    
    return tab