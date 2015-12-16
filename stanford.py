import snap
import re
f = open('web-Stanford.txt', 'r')
#bajar enlace
#https://snap.stanford.edu/data/web-Stanford.txt.gz
read= f.readline()

total = re.search(r"Nodes: (\d+) Edges: (\d+)",read)

#total = re.search(r"(\d+) (\d+)",read)

G1 = snap.TNGraph.New()
G2 = snap.TUNGraph.New()
nodos= int(total.group(1))
edges=int(total.group(2))
for x in range(1,nodos+1):
	G1.AddNode(x)
	G2.AddNode(x)

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
	G1.AddEdge(n1,n2)
	G2.AddEdge(n1,n2)

#Genera un txt con los nodos
#snap.SaveEdgeList(G1, "test.txt", "Save as tab-separated list of edges")
##cf = snap.GetClustCf(G1)
##print cf

PRankHDirigido = snap.TIntFltH()
PRankHNodirigido = snap.TIntFltH()
snap.GetPageRank(G1, PRankHDirigido)
snap.GetPageRank(G2,PRankHNodirigido)
#item = []
i=0
f = open ("PRankHDirigido.txt", "w")
for itema in PRankHDirigido:
	#print itema
	#temp =[]
	#temp.append(PRankHDirigido[itema])
	#temp.append(i+1)
	#item.append(temp)
	f.write(str(i+1) + " "+ str(PRankHDirigido[itema]) + "\n")
	i=i+1
f.close()
#item2 = []
i=0
f = open ("PRankHNodirigido.txt", "w")
for itema in PRankHNodirigido:
	#print itema
	#temp =[]
	#temp.append(PRankHNodirigido[itema])
	#temp.append(i+1)
	#item2.append(temp)
 	f.write(str(i+1) + " "+ str(PRankHNodirigido[itema]) + "\n")
	i=i+1
f.close()
print "Terminado.\n"
#print item
#print item2

#item.sort(reverse=True)
#i=11
#j=0
#for valor in item:
#	j=j+1
#	if(j<i):
#		print valor
#	else:
#		break
