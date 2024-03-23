

def interaction_matrix(state, adj):
    n=len(adj)
    int_mat=[]
    for i in range(0,n):
        int=[]
        for j in range(0,n):
            int.append(state[i]*adj[j])
        int_mat.append(int_mat)
    return(int_mat)

