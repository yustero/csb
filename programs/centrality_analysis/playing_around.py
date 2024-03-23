import random
import copy 
import randomization
import boolean_sim
import matplotlib.pyplot as plt
import numpy as np
import glob
import Parser
import team_influence

def swap(adj,p):
    n= len(adj)
    out_mat= copy.deepcopy(adj)
    if random.random()< p:
        a= random.randint(0,n-1)
        b = random.randint(0,n-1)
        c = random.randint(0,n-1)
        d = random.randint(0,n-1)
        buffer = out_mat[a][b]
        out_mat[a][b]=out_mat[c][d]
        out_mat[c][d]=adj[a][b]
    return(out_mat)



def n_swaps(adj,p,n):
    k=copy.deepcopy(adj)
    for i in range(0,n):
        k=swap(k,p)
    return(p)


path1="/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/centrality_analysis/topofiles"
filedat=glob.glob(path1+"/*topo")
topofiles=[x.split("/")[-1] for x in filedat]

tim_d=[]
no_sol=[]


no_of_sim=100

file=topofiles[2]
adj_initial=Parser.adj_extract_core(file)
adj1=team_influence.updated_matrix_from_adj(adj_initial,file)
steady_t1=boolean_sim.steady_states_time(adj1,no_of_sim)
ssf1=boolean_sim.steady_state_frequency(steady_t1[0],adj1)


'''tim_d.append(np.mean(steady_t1[1]))
no_sol.append(no_of_sim - sum(ssf1[1]))
for i in range(0,100):

    mat=randomization.random_edge_exchange(adj1,10)

    k =boolean_sim.steady_states_time(mat,no_of_sim)

    ssf=boolean_sim.steady_state_frequency(k[0],mat)
    
    tim_d.append(np.mean(k[1]))
    print(tim_d)
    no_sol.append(no_of_sim-sum(ssf[1]))

print(tim_d[0],no_sol[0])
plt.hist(tim_d, bins=30)
plt.axvline(tim_d[0], color='r', linestyle='dashed', linewidth=1)
#plt.hist(no_sol)
#plt.axvline(no_sol[0], color='r', linestyle='dashed', linewidth=1)
plt.savefig("100 simulations_hist_time_dist_racipe2.png")
print(no_sol[0])

plt.show()
#boolean_sim.bar_graph(ssf,"hello")'''
'''
nodes=20
time_dist=[]
no_of_nodes=[]
for i in range(0,nodes**2):
    mat=randomization.rand_mat_n_e(20,i)
    k=boolean_sim.steady_states_time(mat,100)
    
    time_dist.append(np.mean(k[1]))
    no_of_nodes.append(i)
    print(i)
plt.scatter(no_of_nodes,time_dist)
plt.show()'''

adj=[[0,1,-1,0],[1,0,-1,0],[-1,0,0,1],[-1,0,1,0]]
adju=[[0,1,-1,0],[1,0,0,-1],[-1,0,0,1],[0,-1,1,0]]
kad=boolean_sim.steady_states(adj,1000)
kau=boolean_sim.steady_states(adju,1000)
ssfa=boolean_sim.steady_state_frequency(kad,adj)
ssfu=boolean_sim.steady_state_frequency(kau,adju)
boolean_sim.bar_graph(ssfa,"jello")
boolean_sim.bar_graph(ssfu,"hello")
