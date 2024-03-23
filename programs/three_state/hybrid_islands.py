#Have to characterize hybrid states on the basis of their basin size. 
# Through which all nodes does information pass through when a hybrid node is perturbed
# Regenerate the perturbation diagram properly
'''What do I mean when I want to identify hybrid islands?

There are three kinds of results from hybrid node preturbations 
- It jumps to the opposite hybrid state
- It doesn't result in a steady state
- It goes back to the same state
I don't know if some perturbation results in jumping to an entirely different hybrid state

One way to define islands could be that given a certain configuration you can find set of nodes which can be perturbed 
and information doesn't really propagate while in the other set of nodes perturbation can result in propagation of information

'''


import coherent_parser
import numpy as np 
import pandas as pd
import boolean_sim
import three_states_sim
import hybrid_states
import randomization
import topopath
import node_metrics
import boolean_siml
import matplotlib.pyplot as plt

def non_hybrid_perturb(adj,histates,t1,t2, opt_states):
    n=len(adj)
    ns=len(histates)

    same=0
    optimum=0
    switch=0
    other=0
    
    def minusl(li):
        out=[]
        for i in li:
            out.append(-1*li)
        return(out)


    nonhyb=hybrid_states.non_hybrid_nodes(adj,histates,t1,t2)

    for i in range(0,ns):
        for j in nonhyb[i]:
            for k in range(0,n):
                out=boolean_sim.node_perturb(histates[i],adj,j)
                histates[i]=list(histates[i])
                print(out,list(histates[i]))
                if len(out)!=0:    
                    if list(out[0])==histates[i]:
                        same+=1
                    elif list(out[0])==minusl([histates[i]]):
                        other+=1
                        switch+=1

                    elif list(out[0])== opt_states[0] or list(out[0])== opt_states[1]:
                        optimum+=1
                        other+=1
                    else:
                        other+=1
                else:
                    other+=1
    return(same,optimum,switch,other)


def hybrid_perturb(adj,histates,t1,t2,opt_states):
    n=len(adj)
    ns=len(histates)

    same=0
    optimum=0
    switch=0
    other=0
    
    def minusl(li):
        out=[]
        for i in li:
            out.append(-1*li)
        return(out)




    hyb=hybrid_states.hybrid_nodes(adj,histates,t1,t2)

    for i in range(0,ns):
        for j in hyb[i]:
            for k in range(0,n):
                out=boolean_sim.node_perturb(histates[i],adj,j)
                histates[i]=list(histates[i])
                print(out,list(histates[i]))
                if len(out)!=0:    
                    if list(out[0])==histates[i]:
                        same+=1
                    elif list(out[0])==minusl([histates[i]]):
                        other+=1
                        switch+=1

                    elif list(out[0])== opt_states[0] or list(out[0])== opt_states[1]:
                        optimum+=1
                        other+=1
                    else:
                        other+=1
                else:
                    other+=1
    return(same,optimum,switch,other)


def island(state,node,adj):
    n=len(adj)
    node_state=state.copy()
    node_state[node]=node_state[node]*-1
    isnodes=[]
    for i in range(0,n):
        dat=boolean_sim.nodes_involved(node_state)[1]
        if  len(dat[1])!=0 and dat[1] not in isnodes:
            isnodes.append(dat[1])
    return(isnodes)

def noisy_perturb(adj,states,t1,t2):
    n=len(adj)
    ns=len(states)
    
    inv_nodes=[]
    hyb=hybrid_states.hybrid_nodes(adj,states,t1,t2)

    for i in range(0,ns):
        inv_nodes.append([])
        for j in hyb[i]:
            for k in range(0,n):
                node_flip=node_metrics.node_flip(states[i],j)
                inv_nodes[i].append(boolean_sim.nodes_involved(node_flip,adj)[-1])
    
    return(inv_nodes,hyb)



i=2
dat=coherent_parser.clustered_matrix_file(topopath.topofiles[i])
adj=dat[0]
t1=len(dat[1])
t2=len(dat[2])
print(adj)
steadys=boolean_sim.steady_states(adj,1000)
ssf=boolean_sim.steady_state_frequency(steadys,adj)

hybd=hybrid_states.opt_hybrid_states(ssf,adj,t1,t2)
dat=noisy_perturb(adj,hybd[1],t1,t2)
print(topopath.topofiles[i])

def uniql(li):
    out=[]
    for i in li:
        if i not in out: 
            out.append(i)
    return(out)
n=len(dat[0])
non_hybp=0
hybi=0
for i in range(0,n):
    for j in dat[0][i] :
        out=[]
        if len(uniql(j)) > 0: 
            for k in uniql(j):
                if k not in  dat[1][i]: 
                    out.append(k)
        if len(out)==0:
            hybi+=1  
        if len(out)!=0:
            non_hybp+=1
            #print(out,dat[1][i])
    #print("----------------------------")
print(non_hybp,hybi)
#Why am i getting states which do not converge to anything? The network isn't supposed to have long range thingies i guess maybe