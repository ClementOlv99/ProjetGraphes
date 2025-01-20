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
            if (elti[0] != eltj[0]) and (norme3([float(elti[1]), float(elti[2]), float(elti[3])], [float(eltj[1]), float(eltj[2]), float(eltj[3])]) <= range):
                G.add_edge(int(elti[0]), int(eltj[0]))

    return G

def affichage(G):

    node_positions = {node: (data['x'], data['y'], data['z']) for node, data in G.nodes(data=True)}

    # on plote le graphe en 3d
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # On affiche les Noeuds
    for node, (x, y, z) in node_positions.items():
        ax.scatter(x, y, z, label=f'Node {node}', s=100)

    # On affiche les arêtes
    for edge in G.edges():
        x_values = [node_positions[edge[0]][0], node_positions[edge[1]][0]]
        y_values = [node_positions[edge[0]][1], node_positions[edge[1]][1]]
        z_values = [node_positions[edge[0]][2], node_positions[edge[1]][2]]
        ax.plot(x_values, y_values, z_values, 'k-', alpha=0.6)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Essaim de satellites')

    plt.show()
    


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



def clusteringAvg(G):
    return nx.average_clustering(G)

def clusteringDistrib(G):
    return nx.clustering(G)

def nbCliques(G):
    return nx.number_of_cliques(G)

def nbComposantesConnexes(G):
    return nx.number_connected_components(G)

def cheminLePlusCourt(G):
    return nx.shortest_path(G)

def distributionCheminLePlusCourt(G):
    return nx.shortest_path_length(G)

def nbPlusCourtChemin(G):
    pcc = nx.shortest_path_length(G)
    pcc_list = []
    for source, target_dict in pcc.items():
        for target, length in target_dict.items():
            pcc_list.append((source, target, length))
    return pcc_list




   
        
    


G = CreerGraphe("topology_avg.csv")
affichage(G)
print(distribution_degré(G))
print(nbCliques(G))

