import snap
import networkx as nx
import matplotlib.pyplot as plt
import re
from scipy import stats
f = open('web-Stanford.txt', 'r')
#bajar enlace
#https://snap.stanford.edu/data/web-Stanford.txt.gz
read= f.readline()

total = re.search(r"Nodes: (\d+) Edges: (\d+)",read)


nodos= int(total.group(1))
edges=int(total.group(2))



G=nx.Graph()

print "Numero de nodos ",nodos
print "Numero de aristas ", edges

read= f.readline()
#print read
a=1
for line in f:
	an =line
	#print an
	pares = re.search(r"(\d+)\t(\d+)",an)
	n1= int(pares.group(1))
	n2=int(pares.group(2))
	G.add_edge(n1,n2)

elarge=[(u,v) for (u,v,d) in G.edges(data=True)]

pos=nx.spring_layout(G) # positions for all nodes

# nodes
nx.draw_networkx_nodes(G,pos,node_size=700)

# edges
nx.draw_networkx_edges(G,pos,edgelist=elarge,
                    width=6)

# labels
nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

plt.axis('off')
plt.savefig("weighted_graph.png") # save as png
plt.show() # display
