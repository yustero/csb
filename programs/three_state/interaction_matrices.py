import topopath
import coherent_parser
import three_states_sim
import matplotlib.pyplot as plt
import boolean_siml
import numpy as np

def not_teamlike_interactions(int_mats, t1,adj):
    #int_mats is a list of interaction matrices
    #t2 is assumed to be n-t1
    n=len(adj)
    nfrust=[]

    for k in int_mats:
        frust1=0
        frust2=0
        for i in range(0,n):
            for j in range(0,n):
                if i<t1 and j<t1 :
                    if k[i][j] == -1:
                        frust1+=1
                if i>=t1 and j<t1:
                    if k[i][j]==-1:
                        frust1+=1

                if j>=t1 and i<t1:
                    if k[i][j]==1:
                        frust1+=1
                if i>=t1 and j>= t1:
                    if k[i][j]==1:
                        frust1+=1

        for i in range(0,n):
            for j in range(0,n):
                if i<t1 and j<t1 :
                    if k[i][j] == 1:
                        frust2+=1
                if i>=t1 and j<t1:
                    if k[i][j]==1:
                        frust2+=1

                if j>=t1 and i<t1:
                    if k[i][j]==-1:
                        frust2+=1
                if i>=t1 and j>= t1:
                    if k[i][j]==-1:
                        frust2+=1


        nfrust.append(min(frust1,frust2))
    return(nfrust)

def not_teamlike_cumul(state_trijs,t1,adj,time):
    no_team_data=[]
    mean_trijectory=[]
    for z in state_trijs:
    
        no_team_data.append(not_teamlike_interactions(three_states_sim.interaction_matrices(z,adj),t1,adj))

    for i in range(0,time):
        val=[]
        for j in no_team_data:
            if len(j)>=i+1:
                print(len(j),i)
                val.append(j[i])
        mean_trijectory.append(np.mean(val))
    return(mean_trijectory)
    

def edges(adj):
    n=len(adj)
    count=0
    for i in range(0,n):
        for j in range(0,n):
            if adj[i][j]!=0:
                count+=1
    return(count)
def nfrust(int_mats,adj):
    n=len(adj)
    nfrust=[]

    for k in int_mats:
        frust=0
        
        for i in range(0,n):
            for j in range(0,n):
                if k[i][j]<0:
                    frust+=1
        nfrust.append(frust)
    return(nfrust)

def normfrust(int_mats,adj):
    n=len(adj)
    
    nfrust=[]
    nedges=edges(adj)

    for k in int_mats:
        frust=0

        for i in range(0,n):
            for j in range(0,n):
                if k[i][j]<0:
                    frust+=1
        nfrust.append(frust/nedges)
    return(nfrust)


def frustrated_cumul(state_trijs,adj,time):
    frust_edges_data=[]
    mean_trijectory=[]
    for z in state_trijs:
    
        frust_edges_data.append(nfrust(three_states_sim.frustrated_matrices(z,adj),adj))

    for i in range(0,time):
        val=[]
        for j in frust_edges_data:
            if len(j)>=i+1:
                
                val.append(j[i])
        mean_trijectory.append(np.mean(val))
    return(mean_trijectory)

def norm_frustrated_cumul(state_trijs,adj,time):
    #This function gets you the frustration decay trijectories
    frust_edges_data=[]
    mean_trijectory=[]
    for z in state_trijs:
    
        frust_edges_data.append(normfrust(three_states_sim.frustrated_matrices(z,adj),adj))

    for i in range(0,time):
        val=[]
        for j in frust_edges_data:
            if len(j)>=i+1:
                
                val.append(j[i])
        mean_trijectory.append(np.mean(val))
    return(mean_trijectory)

def norm_frustrated_cumul_steady(states,adj):
    #this function doesn't get you trijectory but gets you the frustration values in the final steady states
    frust_edges_data=[]
    mean_trijectory=[]
    
    frust_edges_data= normfrust(three_states_sim.frustrated_matrices(states,adj),adj)

    return(frust_edges_data,np.mean(frust_edges_data))


def interaction_eigenval_trij(state_trijs,adj,time):
    pass


def num_eignval_dist(matrices):
    bigeigh_dist=[]
    for mat in matrices:
        count=0
        eignvals=np.linalg.eigh(mat)[0]
        
        for i in eignvals:
            
            if i>1 and i.imag ==0:
                count+=1
        bigeigh_dist.append(count)

    return(count)
k=2
network=coherent_parser.clustered_matrix_file(topopath.topofiles[k])

adj=network[0]
t1=len(network[1])



'''states=boolean_siml.steady_states_evol(adj,10)[1][0]
frust_dist=nfrust(three_states_sim.interaction_matrices(states,adj),adj)
time=[x for x in range(len(frust_dist))]
plt.plot(time, frust_dist)
plt.xlabel("time step")
plt.ylabel("Number of frustrated edges")
plt.title("Number of frustrated edges over simulation using ising formalism")
plt.show()
'''



#mats=three_states_sim.interaction_matrices(states,adj)
#print(nfrust(mats,t1,adj))

#The following code captures the number of "team like scores"

'''states=three_states_sim.steady_states_evol(adj,10)[1][0]
teamlike_dist=not_teamlike_interactions(three_states_sim.interaction_matrices(states,adj),t1,adj)
print(teamlike_dist[-1])
time=[x for x in range(len(teamlike_dist))]
plt.plot(time, teamlike_dist)
plt.xlabel("time step")
plt.ylabel("Number of rogue interactions")
plt.title("Number of rogue interactions over simulation using turnoff formalism")
plt.show()'''


'''#The following is about mean trijectory
states=three_states_sim.steady_states_evol(adj,1000)[1]

mean_frustrated_edges= frustrated_cumul(states,adj,120)

time=[x for x in range(len(mean_frustrated_edges))]
plt.plot(time, mean_frustrated_edges)
plt.xlabel("time step")
plt.ylabel("mean number of frustrated edges")
plt.title("mean number of frustrated edges over simulation using turnoff formalism")
plt.show()
'''
'''states=boolean_siml.steady_states_evol(adj,10)[1][0]
data=three_states_sim.interaction_matrices(states,adj)'''

