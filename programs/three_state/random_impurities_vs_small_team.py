import nteams
import boolean_siml
import matplotlib.pyplot as plt
import interaction_matrices
import copy
import random 
import numpy as np

#This program takes a 6,6 two teams network and a 6,5,1 three teams network with density 0.3 and then changes the density of the small team 
# and then adds the same number of impurities in the two team network
'''
This can have two cases
1. We randomly invert the same number of edges in the two teams
2. This feels like a better comparision since the number of edges remains the same, we randomly add same number of edges within the teams. 
'''

def add_impurity(adj,t1,nedges):
    n=len(adj)
    count=nedges
    
    output = copy.deepcopy(adj)
    while count!=0:
        a=random.randint(0,n-1)
        b=random.randint(0,n-1)
        if a<t1 and b < t1 and output[a][b]==0:
            output[a][b]=-1
            count+=-1
        if a>=t1 and b>=t1 and adj[a][b]==0:
            output[a][b]=-1
            count+=-1
    return(output)


mean_frust1=[]
mean_frust2=[]
dens=[]
for i in np.linspace(0.1,0.9,20):
    density1=nteams.density_mat_gen(2,i)
    
    
    frust1_dist=[]
    frust2_dist=[]

    for j in range(0,10):
        adj1=add_impurity(nteams.nteam_net(2,[6,6],density1)[0],6,np.floor(i*2*6))
        adj2=nteams.nteam_net(3,[6,6,1],[[0.3, 0.3, 0.3], [0.3, 0.3, 0.3], [i,i,i]])[0]

        steadys1=boolean_siml.steady_states(adj1,1000)
        steadys2=boolean_siml.steady_states(adj2,1000)

        data1=interaction_matrices.norm_frustrated_cumul_steady(steadys1,adj1)
        data2=interaction_matrices.norm_frustrated_cumul_steady(steadys2,adj2)

        frust_1=data1[0]
        frust_2=data2[0]

        frust1_dist.append(np.mean(frust_1))
        frust2_dist.append(np.mean(frust_2))
        print(np.mean(frust1_dist),np.mean(frust2_dist),i)
    
    mean_frust1.append(np.mean(frust1_dist))
    mean_frust2.append(np.mean(frust2_dist))
    dens.append(i)

plt.scatter(dens,mean_frust1,label="Two teams")
plt.scatter(dens,mean_frust2,label="Three teams")

plt.xlabel("Density")
plt.ylabel("Mean mean frustration")
plt.legend(loc="upper right")
plt.show()



