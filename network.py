import networkx as nx
import matplotlib.pyplot as plt

DG = nx.DiGraph()

nodes = ['S', 'A', 'B', 'C', 'E']
positiones = {
    'S': (0, 0),
    'A': (1, 0),
    'C': (2, 1),
    'B': (2, -1),
    'E': (3, 0)
}

edges = [('S', 'A'), ('A', 'B'), ('A', 'C'), ('C', 'E'), ('B', 'E')]
weights = {('S', 'A'): 1,
           ('A', 'B'): 2,
           ('A', 'C'): 1,
           ('C', 'E'): 2,
           ('B', 'E'): 2}

DG.add_nodes_from(nodes)
DG.add_edges_from(edges)

for node, pos in positiones.items():
    DG.nodes[node]['pos'] = pos
for edge, weight in weights.items():
    DG.edges[edge]['weight'] = weight

path = nx.dijkstra_path(DG, source='S', target='E')

print(path)
edge_labels = nx.get_edge_attributes(DG, 'weight')
nx.draw(DG, positiones, with_labels=True)
nx.draw_networkx_edge_labels(DG, positiones, edge_labels=edge_labels)
plt.show()
