import three_states_sim as tss
import boolean_siml as bsl
import networkx as nx
import matplotlib.pyplot as plt 
import input_space_map as ism
import random

def ring_lattice_edges(nodes,k):
#This function results in unique pairs of edges
    half = k//2
    n=len(nodes)
    for i, v in enumerate(nodes):
        for j in range(i+1,i+half+2):
            w=nodes[j%n]
            yield v,w

def make_ring_lattice(n,k):
    G=nx.Graph()
    nodes = range(n)
    G.add_nodes_from(nodes)
    edges=ring_lattice_edges(nodes,k)
    G.add_edges_from(edges)
    return G

'''G=make_ring_lattice(10,4)
nx.draw_circular(G,node_size=100)
plt.show()'''

def rewire(G,p):
    for v,w in G.edges():
        if random.random()<p:
            G.remove_edge(v,w)
            choices= set(G)- {v} - set(G[v])
            new_w=random.choice(list(choices))
            G.add_edge(v,new_w)

def watts_Strogatz_graph(n,k,p):
    G= make_ring_lattice(n,k)
    rewire(G,p)
    return(G)




#graph=make_ring_lattice(10,4)
#print(set(graph[0]))

n=10
k=4
ps=[0,0.5,1]
#fig = plt.figure(figsize=(10,3))

'''for i in range(3):
    ax=plt.subplot(1,3,i+1)
    G = watts_Strogatz_graph(n,k,ps[i])
    nx.draw_circular(G)
'''

def small_word_couple(g1,g2,n):
    def homo_connect(g1,g2,n):
        pass

g2=nx.Graph(id="check")
g2.add_nodes_from([1,2,3], team="t1")
g2.add_edges_from([(1,2),(2,3)], sign=1)
g2.add_edge(3,1, sign=-1)

ws=nx.watts_strogatz_graph(100,4,0.5)
print(ws.edges)
nx.draw(ws,label=True)
plt.show()
