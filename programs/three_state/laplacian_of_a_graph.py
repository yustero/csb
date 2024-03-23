import nteams
import numpy as np 


def degree(adj,k):
    n=len(adj)
    outdeg=0
    indeg=0
    for i in range(0,n):
        if adj[i][k]!=0:
            outdeg+=1
        if adj[k][i]!=0:
            indeg+=1
    return(outdeg+indeg)

def signed_laplacian(adj):
    n=len(adj)
    output=[]
    edge=[0 for i in range(0,n)]
    for i in range(0,n):
        output.append(edge.copy())
    
    for i in range(0,n):
        for j in range(0,n):
            if i==j:
                output[i][j]=degree(adj,i)
            if i!=j:
                output[i][j]=-adj[i][j]
    return(output)

density2=nteams.density_mat_gen(2,0.3)
density3=nteams.density_mat_gen(3,0.3)
density4=nteams.density_mat_gen(4,0.3)

adj2=nteams.nteam_net(2,[6,6],density2)[0]
adj3=nteams.nteam_net(3,[4,4,4],density3)[0]
adj4=nteams.nteam_net(4,[3,3,3,3],density4)
print(np.min(np.linalg.eig(adj2)[0]))
print(np.min(np.linalg.eig(adj3)[0]))
print(np.min(np.linalg.eig(adj4)[0]))