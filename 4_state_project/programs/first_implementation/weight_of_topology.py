import random 
import copy 
import artificial
import matplotlib.pyplot as plt




def edge_inversion(adj,k):
    n=len(adj)
    rand2=copy.deepcopy(adj)
    i=0
    while i<k:
        a=random.randint(0,n-1)
        b=random.randint(0,n-1)
        if rand2[a][b]!=0:
            rand2[a][b]=rand2[a][b]* (-1)
            i+=1 
    return(rand2)

#The following plot is number of edge sign change vs steady_states. One could also plot team strength vs number of steady states. 
#Another plot I could generate would be epithellial mes score vs team strength and show that even at low team strengths we get terminal states. 

d=0.3
network=artificial.network(8,8,d,d,d,d)[0]

