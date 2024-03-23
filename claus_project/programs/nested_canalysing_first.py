#Implementing whatever's written in notes.py

import random 
import csv
import pandas as pd
import priorities as pri
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


#t1 and t2 represent the list having indices of both the teams


pries=pri.priorities

adj=[[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0], [1, 1, 1, -1, 0, 1, 0, 1, 0, -1, 0, 0, 0, 0, -1], [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0, -1, 0, 0, -1, 0, 0], [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, -1, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, -1, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, -1, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, -1, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, -1, 0, -1, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0]]
t1=[0, 1, 2, 3, 4, 5, 6, 7, 8]
t2=[9, 10, 11, 12, 13, 14]

def in_nodes(adj):
    #This outputts a list having indices of nodes having an outgoing edge into the node having i'th index in the list 
    n=len(adj)
    
    in_nodes=[[] for x in range(0,n)]

    for i in range(0,n):
        for j in range(0,n):
            if adj[i][j]!=0:
                in_nodes[j].append(i)

    

    return(in_nodes)

def random_priority(in_nodes):

    priorities=[]
    for i in in_nodes:
        n=len(i)

        priority=[x for x in range(0,n)]
        
        random.shuffle(priority)
        #this shuffle function changes the original list      
        
        priorities.append(priority.copy())
    return(priorities)


def evolve(state,adj,node,prioritys):
    order=prioritys[node]

    n=len(adj)
    l=len(order)
    for i in range(0,l):
        if state[order[i]]==1:
            if adj[order[i]][node]==1:
                state[node]=1
                break
            if adj[order[i]][node]==-1:
                state[node]=0
                break
    return(state)

def team_score_distribution(states,t1,t2,adj):
    n=len(adj)
    scores=[]
    for i in states:
        score=0
        for j in range(0,n):
            if j in t1 and i[j]==1:
                score+=1
            if j in t1 and i[j]==0:
                score+=-1

            if j in t2 and i[j]==1:
                score+=-1
            if j in t2 and i[j]==0:
                score+=1
        scores.append(abs(score))
    return(scores)

def team_score_2_distribution(states,t1,t2,adj):
    n=len(adj)
    scores=[]
    for i in states:
        episcore=0
        mescore=0
        for j in range(0,n):
            if j in t1 and i[j]==1:
                episcore+=1


            if j in t2 and i[j]==1:
                mescore+=1

        scores.append(abs(episcore-mescore))
    return(scores)




    
#############################################################################3


def steady_check(nodes,adj,prioritys):
    n=len(adj)
    count=0
    for i in range(0,n):
        if evolve(nodes,adj,i,prioritys)[i]!= nodes[i]:
           
           count+=1
        
    if count==0:
        return(True)
    else:
        return(False)

def steady_check_nodes(nodes,adj):
    #if the state is not steady state it resluts in nodes which evolve and are affected
    n=len(adj)
    changed_nodes=[]
    count=0
    for i in range(0,n):
        if evolve(nodes,adj,i)[i]!= nodes[i]:
            count+=1
            changed_nodes.append(i)
            
        
    if count==0:
        return(True,changed_nodes)
    else:
        return(False,changed_nodes)




def random_inputs(adj):
    n=len(adj)
    nodes_initial= [0 for i in range(0,n)]
    for i in range(n):
        k = random.choice([0,1])
        nodes_initial[i]=k
    return(nodes_initial)


#Random score function is here to test with background inputs
def random_score_distribution(adj,t1,t2,nsim):
    states=[]
    for i in range(0,nsim):
        states.append(random_inputs(adj))
    return(team_score_distribution(states,t1,t2,adj))

def random_score_2_distribution(adj,t1,t2,nsim):
    states=[]
    for i in range(0,nsim):
        states.append(random_inputs(adj))
    return(team_score_2_distribution(states,t1,t2,adj))


def steady_states(adj, number_of_simulations,prioritys):
    steadys=[]
    n=len(adj)    
    
    for i in range(number_of_simulations):
        nodes_state=random_inputs(adj).copy()
        
        t=0
        timedist=[]
        timtaken=0
        while True:
            k=random.randint(0,n-1)
            
            out = evolve(nodes_state,adj,k,prioritys)
            if steady_check(out,adj,prioritys):
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



def steady_state_frequency(steadys,adj):
    
    n=len(adj)
    sf=[[],[]]
    stn=len(steadys)
    for i in range(0,stn):
        if steadys[i] not in sf[0]:
            sf[0].append(steadys[i])
            sf[1].append(1)
        elif steadys[i] in sf[0]:
            m=sf[0].index(steadys[i])
            sf[1][m]+=1
    return(sf)




def bar_graph(ssf, image_name):
    frequencies=ssf[1]
    steadystates_plot=[]
    for i in ssf[0]:
        steadystates_plot.append("{}".format(i))
    print(steadystates_plot,frequencies)

    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(steadystates_plot, frequencies, color ='blue',
            width = 0.4)
    
    plt.xlabel("steady states")
    plt.ylabel("Frequencies")
    plt.title("Number of simulations: 1000")
    fig.autofmt_xdate()
    #plt.savefig("{}{}".format(image_name,".png"))
    plt.show()
    print("ayeaye!")



def bar_graph_2(ssf):
    frequencies=ssf[1]
    steadystates_plot=[]
    for i in ssf[0]:
        steadystates_plot.append("{}".format(i))
    print(steadystates_plot,frequencies)

    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(steadystates_plot, frequencies, color ='blue',
            width = 0.4)
    
    plt.xlabel("steady states")
    plt.ylabel("Frequencies")
    
    fig.autofmt_xdate()
    
    return(plt)

####################################################3333
def outdegree_distribution(adj):
    n=len(adj)
    outdeg=[]
    for i in range(0,n):
        out=0
        for j in range(0,n):
            if adj[i][j]!=0:
                out+=1
        outdeg.append(out)
    return(outdeg)

def outdeg_order(adj):
    #This function arranges the nodes in decending order of their outdegree
    ord=list(np.argsort(outdegree_distribution(adj)))
    ord.reverse()
    return(ord)

def out_deg_priority(adj):
    ''' The function takes in a network and assigns a priority order to each node's ncf such that the relative ordering of nodes is same as that of them in the 
        list having outdegree in decreasing order
    '''

    def in_nodes(adj,k):
        #this function returns list of nodes having inputs to k'th node
        n=len(adj)
        inputs=[] 
        for i in range(0,n):
            if adj[i][k]!=0:
                inputs.append(i)
        return(inputs)

    n=len(adj)
    priorities=[]

    global_order=outdeg_order(adj)

    for i in range(0,n):
        order=[]
        innodes=in_nodes(adj,i)
        for j in global_order:
            if j in innodes:
                order.append(j)
        priorities.append(order)

    return(priorities)        

def random_priority(adj):
    #This function gets a random global priority order 

    n=len(adj)
    global_order=[x for x in range(0,n)]
    random.shuffle(global_order)


    def in_nodes(adj,k):
        #this function returns list of nodes having inputs to k'th node
        n=len(adj)
        inputs=[] 
        for i in range(0,n):
            if adj[i][k]!=0:
                inputs.append(i)
        return(inputs)

    priorities=[]
    for i in range(0,n):
        order=[]
        innodes=in_nodes(adj,i)
        for j in global_order:
            if j in innodes:
                order.append(j)
        priorities.append(order)

    return(priorities)        

def same_team_priority(adj,t1,t2):
    n=len(adj)
    t1n=len(t1)
    t2n=len(t2)
    t1p=[x for x in range(0,t1n)]
    t2p=[x for x in range(t1n,n)]
    random.shuffle(t1p)
    random.shuffle(t2p)
    priority=t1p+t2p
    return(priority)

def opposite_team_priority(adj,t1,t2):
    n=len(adj)
    t1n=len(t1)
    t2n=len(t2)
    t1p=[x for x in range(0,t1n)]
    t2p=[x for x in range(t1n,n)]
    random.shuffle(t1p)
    random.shuffle(t2p)
    priority=t2p+t1p
    return(priority)

