import random
import numpy as np







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

        if counter == len(nodes):
            print(counter)
            check=nodes
            break
