import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

G = nx.grid_2d_graph(2, 2)  # 5x5 grid
H = G.to_directed()

# print the adjacency list
#for line in nx.generate_adjlist(G):
#    print(line)
# write edgelist to grid.edgelist

# Returns adjacency matrix of a graph
A = nx.adjacency_matrix(G)
B = nx.adjacency_matrix(H)

print("Adjacency matrix: ")
''' print(A.todense())

print(B.todense()) '''

print("Edges: ")
print("")
print(G.edges)
#print(H.edges)

''' print("A^3:")
print(np.nonzero(A.todense())) '''

''' print("Cycles:")
print(nx.find_cycle(G)) '''


''' nx.write_edgelist(G, path="grid.edgelist", delimiter=":")
# read edgelist from grid.edgelist
H = nx.read_edgelist(path="grid.edgelist", delimiter=":") '''

nx.draw(G)
plt.show()