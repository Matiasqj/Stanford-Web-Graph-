import snap
import re
from scipy import stats
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
item = []
listaParaIndicesDirigidos = []
i=0
f = open ("PRankHDirigido.txt", "w")
for itema in PRankHDirigido:
	#print itema
	temp =[]
	temp.append(PRankHDirigido[itema])
	temp.append(i+1)
	item.append(temp)
	## PARA EL INDICE
	listaParaIndicesDirigidos.append(PRankHDirigido[itema])
	f.write(str(i+1) + " "+ str(PRankHDirigido[itema]) + "\n")
	i=i+1
f.close()
item2 = []
listaParaIndicesNODirigidos = []
i=0
f = open ("PRankHNodirigido.txt", "w")
for itema in PRankHNodirigido:
	#print itema
	temp =[]
	temp.append(PRankHNodirigido[itema])
	temp.append(i+1)
	item2.append(temp)
	## PARA EL INDICE
	listaParaIndicesNODirigidos.append(PRankHNodirigido[itema])
 	f.write(str(i+1) + " "+ str(PRankHNodirigido[itema]) + "\n")
	i=i+1
f.close()
print "Terminado.\n"

tau, p_value = stats.kendalltau(listaParaIndicesDirigidos, listaParaIndicesNODirigidos)

print tau, p_value


tau, p_value = stats.spearmanr(listaParaIndicesDirigidos, listaParaIndicesNODirigidos)

print tau, p_value


item.sort(reverse=True)
item2.sort(reverse=True)

##print item
##print item2

item3 = []
listaParaIndicesDirigidos = []
i=0
f = open ("PRankHDirigidoOrdenado.txt", "w")
for itema in item:
	#print itema
	temp =[]
	temp.append(itema[0])
	temp.append(itema[1])
	item3.append(temp)
	listaParaIndicesDirigidos.append(itema[1])
	f.write(str(itema[0]) + " "+ str(itema[1]) + "\n")
	i=i+1
f.close()
item4 = []
listaParaIndicesNODirigidos = []
i=0
f = open ("PRankHNodirigidoDesordenado.txt", "w")
for itema in item2:
	#print itema
	temp =[]
	temp.append(itema[0])
	temp.append(itema[1])
	item4.append(temp)
	listaParaIndicesNODirigidos.append(itema[1])
 	f.write(str(itema[0]) + " "+ str(item[1]) + "\n")
	i=i+1
f.close()
print "Terminado.\n"



tau, p_value = stats.kendalltau(listaParaIndicesDirigidos, listaParaIndicesNODirigidos)

print tau, p_value


tau, p_value = stats.spearmanr(listaParaIndicesDirigidos, listaParaIndicesNODirigidos)

print tau, p_value



