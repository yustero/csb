import artificial
import multi_rules as mr
import multi_state_turnoff as mst
import matplotlib.pyplot as plt 
import numpy as np 

#The following list has the number of steady states obtained via ising and then obtained via turn_off 



def numpy_to_li(adj):
    network=[]
    for i in adj:
        network.append(list(i))
    return(network)

def indegree(adj):
    n=len(adj)
    indeg_dist=[]

    for i in range(0,n):
        indeg=0
        for j in range(0,n):
            if adj[j][i]!=0:
                indeg+=1
        indeg_dist.append(indeg)
    return(indeg_dist)

def nonzerocheck(adj):
    indeg_dist=indegree(adj)
    score=0
    for i in indeg_dist:
        if i==0:
            score+=1
    if score>0:
        return(False)
    if score==0:
        return(True)

mstli=[]
msli=[]


for i in range(0,100):

    adj=numpy_to_li(artificial.network(8,8,0.3,0.3,0.3,0.3)[0])
    if nonzerocheck(adj):
        steadys=mr.steady_states(adj,1000)
        ssf=mr.steady_state_frequency(steadys,adj)

        steadytss=mst.steady_states(adj,1000)
        ssftss=mst.steady_state_frequency(steadytss,adj)
        
        print(len(ssf[0]), len(ssftss[0]))
        mstli.append( len(ssftss[0]))
        msli.append(len(ssf[0]))

plt.scatter(mstli,msli)
plt.ylabel("Number of solutions with multi level ")
plt.xlabel("Number of solutions with multi level turn off")
plt.title("Density 0.3 , t1=t2=8")
plt.show()

