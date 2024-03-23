import boolean_sim
import random
import numpy as np
import coherent_parser
import topopath
import randomization
from scipy.spatial import distance
import matplotlib.pyplot as plt
def node_on(adj,onn, number_of_simulations):
    steadys=[]
    n=len(adj)    
    
    for i in range(number_of_simulations):
        nodes_state=boolean_sim.random_inputs(adj).copy()
        nodes_state[onn]=1
        t=0
        out=nodes_state.copy()
        timedist=[]
        timtaken=0
        while True:
            k=random.randint(0,n-1)
            if k!=onn:
                out = boolean_sim.evolve(nodes_state,adj,k)
            
            if boolean_sim.steady_check(out,adj):
                steadys.append(out)
                timedist.append(timtaken)
                timtaken=0
                break
                
            else :
                nodes_state=out
                timtaken+=1
            
            t+=1
            if t==1000:
                break
    return(steadys)





def node_removal():
    pass

def perturbation_propagation():
    pass

def arrange(ssf1,ssf2):
    ssf1a=[[], []]
    ssf2a=[[],[]]

    common=[]
    for i in ssf1[0]: 
        if i in ssf2[0] and i not in common:
            common.append(i)
    for i in ssf2[0]: 
        if i in ssf1[0] and i not in common:
            common.append(i)

    for i in common:
        ssf1a[0].append(i)
        ssf1a[1].append(ssf1[1][ssf1[0].index(i)])
        ssf2a[0].append(i)
        ssf2a[1].append(ssf2[1][ssf2[0].index(i)])
    
    for i in ssf1[0]:
        if i not in common:
            ssf1a[0].append(i)
            ssf1a[1].append(ssf1[1][ssf1[0].index(i)])
            
            ssf2a[0].append(i)
            ssf2a[1].append(0)
    
    for i in ssf2[0]:
        if i not in common:
            ssf2a[0].append(i)
            ssf2a[1].append(ssf2[1][ssf2[0].index(i)])

            ssf1a[0].append(i)
            ssf1a[1].append(0)

    return(ssf1a,ssf2a)

def jsd(li1,li2):
    return(distance.jensenshannon(li1,li2))

def ssf_li(ssf):
    ossf=[[],[]]
    ossf[1]=ssf[1]
    for i in ssf[0]:
        ossf[0].append(list(i))
    return(ossf)
def average_change_jsd_node_on(adj,nos):
    jsddist=[]
    n=len(adj)
    opt=ssf_li(boolean_sim.steady_state_frequency(boolean_sim.steady_states(adj,100),adj))
    
    for i in range(0,nos):
        k=random.randint(0,n-1)
        ssf=ssf_li(boolean_sim.steady_state_frequency(node_on(adj,k,100),adj))
        dat=arrange(opt,ssf)
        jsddist.append(jsd(dat[0][1],dat[1][1]))
        print(jsddist[i])
    
    return(np.mean(jsddist))

def node_on_rand_calc(adj,nos):
    jsdddist=[]
    for i in range(0,nos):
        mat=randomization.random_edge_exchange(adj,10)
        jsdddist.append(average_change_jsd_node_on(mat,10))
    return(jsdddist)
adj=coherent_parser.clustered_matrix_file(topopath.topofiles[2])[0]

li=node_on_rand_calc(adj,100)
dat=0.48159983556161734
plt.hist(li, alpha=0.5, color="blue")
plt.xlabel("Jsd obtained after keeping on random nodes ")
plt.ylabel("Frequencis")
plt.axvline(dat,color="r", linestyle="dashed",linewidth=1)
plt.show()