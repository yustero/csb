''' I want to look at eigenvalues vs 
1. Number of steady states 
2. Team strength 
3. Number of hybrid states'''

import topopath
import randomization
import coherent_parser
import eigenvalue_analysis as ea
import boolean_siml
import boolonezero
import matplotlib.pyplot as plt
import three_states_sim as tss
import artificial
import numpy as np 
import nteams 

'''adj=coherent_parser.clustered_matrix_file(topopath.topofiles[2])[0]

steadys=tss.steady_states(adj,1000)
ssf=tss.steady_state_frequency_li(steadys,adj)
num=len(ssf[0])

neigs= ea.dim_eigenspace(adj)
print(num,neigs)
plt.scatter(num,neigs, color="r")
'''
'''for i in range(0,50):

    #adj=randomization.random_edge_exchange(adj,10)
    k=0.3
    adj=[]
    mat=artificial.network(8,8,k,k,k,k)[0]
    for i in mat:
        adj.append(list(i))
    steadys=tss.steady_states(adj,1000)
    ssf=tss.steady_state_frequency_li(steadys,adj)
    num=len(ssf[0])

    neigs= ea.dim_eigenspace(adj)
    print(num,neigs)
    plt.scatter(num,neigs)    

plt.title("Number of steady states vs number of eigval>1 for random matrices")
plt.xlabel("Number of steady states")
plt.ylabel("Number of eigenvalues greater than 1")
plt.show()
'''


'''eigns_avg=[]
density=[]
for i in np.linspace(0,1,200):
    density.append(i)
    
    eigs_dist=[]
    for j in range(0,100):
        adj=artificial.network(32,32,i,i,i,i)[0]
        eigs_dist.append(ea.dim_eigenspace(adj))
    eigns_avg.append(np.mean(eigs_dist))


plt.scatter(density,eigns_avg)
plt.xlabel("density")
plt.ylabel("Average eigenspace dimension")
plt.show()
'''


#This looks at the number of eigenvalues greater than one for random matrices

'''k=0.7
adj=artificial.network(8,8,k,k,k,k)[0]
eigns_avg=[]
num_edges_chanegd=[]
for i in range(0, 40):
    eig_dist=[]
    for j in range(0,100):
        radj=randomization.edge_change(adj,i)
        eig_dist.append(ea.dim_eigenspace(radj))
    
    eigns_avg.append(np.mean(eig_dist))
    num_edges_chanegd.append(i)


plt.scatter(num_edges_chanegd,eigns_avg)
plt.xlabel("Number of edges swapped/changed")
plt.ylabel("Average number of eigenvalues >1")
plt.show()
'''
'''eigns_avg=[]
number_edges=[]
for i in range(0, 240):
    eig_dist=[]
    for j in range(0,100):
        radj=randomization.rand_mat_n_e(16,i)
        eig_dist.append(ea.dim_eigenspace(radj))
    
    eigns_avg.append(np.mean(eig_dist))
    number_edges.append(i)


plt.scatter(number_edges,eigns_avg)
plt.xlabel("Number of edges")
plt.ylabel("Average number of eigenvalues >1")
plt.show()
'''


#Three teams


'''eigns_avg=[]
density=[]
for i in np.linspace(0,1,200):
    density.append(i)
    
    eigs_dist=[]
    for j in range(0,100):
        adj=nteams.nteam_net(3,[8,8,8],nteams.density_mat_gen(3,i))[0]
        print(adj)
        eigs_dist.append(ea.dim_eigenspace(adj))
    eigns_avg.append(np.mean(eigs_dist))


plt.scatter(density,eigns_avg)
plt.xlabel("density")
plt.ylabel("Average eigenspace dimension")
plt.title("Three teams of equal size")
plt.show()'''

#To see if teams structure provides greater number of eigenvalues. 

def outputs_for_nteams(n,density, size):
    teamsize=[size for i in range(0,n)]
    density_mat=nteams.density_mat_gen(n,density)
    return(n,teamsize,density_mat)

eigen_dist=[]
n_teams=[]
for n in range(2,10):
    outputs=outputs_for_nteams(n,0.95,4)
    n_teams.append(n)
    eigen=[]
    for i in range(0,10):
        adj=nteams.nteam_net(outputs[0],outputs[1],outputs[2])[0]
        print(adj)
        eigen.append(ea.dim_eigenspace(adj))
    eigen_dist.append(np.mean(eigen))

plt.scatter(n_teams,eigen_dist)
plt.xlabel("Number of teams")
plt.ylabel("Dimensionality of significant eigenspace")
plt.show()




