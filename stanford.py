import snap
import re
f = open('web-Stanford.txt', 'r')
#bajar enlace
#https://snap.stanford.edu/data/web-Stanford.txt.gz
read= f.readline()

total = re.search(r"Nodes: (\d+) Edges: (\d+)",read)

#total = re.search(r"(\d+) (\d+)",read)

G1 = snap.TUNGraph.New()
nodos= int(total.group(1))
edges=int(total.group(2))
for x in range(1,nodos+1):
	G1.AddNode(x)


print nodos
print edges

read= f.readline()
#print read
a=1
for line in f:
	an =line
	#print an
	pares = re.search(r"(\d+)\t(\d+)",an)
	n1= int(pares.group(1))
	n2=int(pares.group(2))
	G1.AddEdge(n1,n2)

#Genera un txt con los nodos
#snap.SaveEdgeList(G1, "test.txt", "Save as tab-separated list of edges")
cf = snap.GetClustCf(G1)
print cf