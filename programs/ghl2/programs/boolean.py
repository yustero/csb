import random
import numpy as np
import parser



   


def subtract(a,b):
    output= np.zeros(len(a))
    for i in range(len(a)):
        output[i]= a[i]-b[i]
    return(output)

def inli(a,b):
    for i in b:
        if (i==a):
            return(True)
def notli(a,b):
    counter =0
    for i in b:
        if (i==a):
            counter+=1
    if counter ==0:
        return(True)

def fevolve(nodes,adj):
    counter = 0
    while True:
        i= random.randint(0,len(nodes)-1)
        check=nodes
        for j in range(len(nodes)):
            if nodes[i]== 0: 
                pass
            
            
            if nodes[i]== 1:
                if adj[i][j] == 1:
                    if nodes[j]== 1:
                        pass
                    if nodes[j]==0:
                        nodes[j]=1
                        print(nodes)
                
                
                if adj[i][j]==-1:
                    if nodes[j]==1:
                        nodes[j]= 0
                        print(nodes)
                    if nodes[j]==0:
                        pass
                
                
                if adj[i][j]==0:
                    pass
            
            
            
            
            if (subtract(nodes,check)== np.zeros(len(nodes))).any():
                #print((subtract(nodes,check == np.zeros(len(nodes)))).any())
                counter+=1

        if counter == len(nodes):
            print(counter)
            check=nodes
            break



nodes_initial=np.array([-1,1,1,])

def evolve(nodes_initial,adj):
    timestep=0
    nodes_states=nodes_initial
    counter=0

    while True:
        zero=np.zeros(len(nodes_initial))
        k= random.randint(0,len(nodes_states)-1)
        state_calc=0
        check=nodes_states
        for i in range(0,len(nodes_initial)):
            state_calc+= nodes_states[i] * adj[i][k]

        if state_calc>0:

            if nodes_states[k] ==1:
                pass
            if nodes_states[k]== -1:

                nodes_states[k] = 1
        if state_calc<0:
            if nodes_states[k] == -1:
                pass
            if nodes_states[k]== 1:

                nodes_states[k] = -1
        timestep+=1
        if timestep == 10000:
            break
        if (subtract(check,nodes_states)== zero).any():
            counter+=1
        if counter == 100:
            return(nodes_states)
            break
        
        check=nodes_states



sample_2= np.array([1,1,1,1,1,1])
sample_2_adj=np.array(([0,1,1,-1,-1,-1],[1,0,1,-1,-1,-1],[1,1,0,-1,-1,-1],[-1,-1,-1,0,1,1],[-1,-1,-1,1,0,1],[-1,-1,-1,1,1,0]))

evolve(sample_2,sample_2_adj)

def random_inputs(adj):
    nodes_initial=[]
    for i in range(len(adj)):
        k = random.choice([-1,1])
        nodes_initial.append(k)
    return(np.array(nodes_initial))

steady_states=[]
for i in range(0,1000):
    steady_states.append(evolve(random_inputs(sample_2_adj),sample_2_adj))
print(steady_states)

steady_statesli=[]

for i in steady_states:
    steady_statesli.append(list(i)) 


ssf=[[],[]]
for i in steady_statesli:
    if notli(i,ssf[0]):
        ssf[0].append(i)
        ssf[1].append(1)
    if inli(i,ssf[0]):
        k= ssf[0].index(i)
        ssf[1][k]+=1
print(ssf)
