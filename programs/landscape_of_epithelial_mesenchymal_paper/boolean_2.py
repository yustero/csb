import Parser
import boolean_simulation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import random



def evolve_3(initial_nodes, adj):
    n=len(adj)
    zero=np.zeros(n)
    timer=0
    k_collect=[]
    while True:
        k = random.randint(0,n-1)
        effect_counter=0
        node_buffer=initial_nodes
        for i in range(0,n-1):
            effect_counter+= initial_nodes[i]*adj[i][k]
        if effect_counter>0:
            if initial_nodes[k] == 1:
                pass
            if initial_nodes[k]==-1:
                initial_nodes[k]=1
        if effect_counter == 0:
            pass
        if effect_counter < 0:
            if initial_nodes[k] == 1:
                initial_nodes[k]=-1
            if initial_nodes[k]== -1:
                pass
        if (node_buffer-initial_nodes==np.zeros(n)).all():
            if k not in k_collect:
                k_collect.append(k)
        else:
            k_collect=[]

        node_buffer=initial_nodes
        if len(k_collect)==n:
            
            return(initial_nodes)

        if timer==1000:
            return(None)
            break            
        
        timer+=1

def random_inputs(adj):
    nodes_initial=[]
    for i in range(len(adj)):
        k = random.choice([-1,1])
        nodes_initial.append(k)
    return(np.array(nodes_initial))

def steady_statesf(adj, number_of_simulations):
    steady_states=[]

    for i in range(0,number_of_simulations):
        ss = evolve_3(random_inputs(adj),adj)
        steady_states.append(ss)




    steady_statesli=[]

    for i in steady_states:
        steady_statesli.append(list(i)) 

    return(steady_statesli)

def steady_states_frequency_calc(steady_states):
    ssf=[[],[]]
    ss=[x for x in steady_states if x is not None]
    for i in ss: 
        if i not in ssf[0]:
            ssf[0].append(i)
            ssf[1].append(1)
        if i in ssf[0]:
            k= ssf[0].index(i)
            ssf[1][k]+=1
    return(ssf)

topofiles_path= glob.glob("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/landscape_of_epithelial_mesenchymal_paper/teams_data/Teams-main/TopoFiles/*topo")
topofiles=[x.split("/")[-1] for x in topofiles_path]
print(topofiles[1])
adj = Parser.adj_extract(topofiles[1])

ss = steady_statesf(adj,1000)

ssf=steady_states_frequency_calc(ss)
print(ssf)
print(len(ssf[0]))