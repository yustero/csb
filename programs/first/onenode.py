import numpy as np
import random 
def subtract(a,b):
    output= np.zeros(len(a))
    for i in range(len(a)):
        output[i]= a[i]-b[i]
    return(output)

def evolve(nodes,adj):
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

        if counter == len(nodes)*len(nodes):
            
            check=nodes
            break
            check=nodes

















def evol(nodes,adj):
    for i in range(len(nodes)):

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

def evol2(nodes,adj):
    while True:
        i= random.randint(0,len(nodes)-1)
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


onenode_nodes =np.zeros(1)
onenode_adj = np.array([0])

onenode_selfact= np.zeros(1)
onenode_selfact_adj= np.array([1])

onenode_selfinh= np.zeros([1])
onenode_selfinh_adj = np.array([-1])

toggle_switch = np.array([1,1])
toggle_switch_adj= np.array(([0,-1],[-1,0]))

sample_1= np.array([1,0])
sample_1_adj= np.array(([1,1],[-1,-1]))

sample_2= np.array([1,1,1,1,1,1])
sample_2_adj=np.array(([0,1,1,-1,-1,-1],[1,0,1,-1,-1,-1],[1,1,0,-1,-1,-1],[-1,-1,-1,0,1,1],[-1,-1,-1,1,0,1],[-1,-1,-1,1,1,0]))

print("onenode")
evolve(onenode_nodes,onenode_adj)
print("onenode_selfactivation")
evolve(onenode_selfact,onenode_selfact_adj)

print("onenode_selfinhibition")
evolve(onenode_selfinh,onenode_selfinh_adj)

print("toggle_switch")
evolve(toggle_switch, toggle_switch_adj )

print("example of strong teams")
evolve(sample_2,sample_2_adj)

print("random_network_1")
evolve(sample_1,sample_1_adj)