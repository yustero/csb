import nteams
import boolean_siml
import numpy as np
import matplotlib.pyplot as plt
import random

def hybrid_score_3teams(states,adj,t1,t2):
    #In this function the last team isn't evaluated at all and only the expression levels of the two big teams are evaluated
    n=t1+t2 
    #Here n!=adj since we're looking at the network from a two teams perspective
    hybrid_scores=[]
    for i in states:        
        epi=0
        mes=0
    
        for j in range(0,n):
            if j<t1 and i[j]==1:
                epi+=1
            if j>=t1 and j<n and i[j]==1:
                mes+=1
                
        hybrid_scores.append(epi-mes)
        print(i, "epi:", epi, "mes:", mes)
    return(hybrid_scores)


def hybridness(ssf,t1,t2,adj):
    nstates=len(ssf[0])
    n=t1+t2
    hybrid_score=0
    hyb_score_dist=[]
    for i in range(0,nstates):
        epi_messcore=hybrid_score_3teams([ssf[0][i]],adj,t1,t2)[0]
        hybs=abs(epi_messcore)*ssf[1][i]/1000
        hybrid_score+=hybs
        hyb_score_dist.append(hybs)
    return(hybrid_score,hyb_score_dist)


def third_team_edge_rand(adj,t1,t2,t3,k):
    #Non useful swaps to make code easier to write
    n=len(adj)
    for count in range(0,k):
        i = random.randint(t1+t2-1,n-1)
        j = random.randint(0,n-1)
        adj[i][j]=adj[i][j]*-1
    for count in range(0,k):
        j = random.randint(t1+t2-1,n-1)
        i = random.randint(0,n-1)
        adj[i][j]=adj[i][j]*-1
    return(adj)

def third_team_edge_pos_oneway(adj,t1,t2,t3):
    n=len(adj)
    for i in range(0,n-t3):
        for j in range(t1+t2,n):
            adj[j][i]=-1*adj[j][i]
    return(adj)


def third_team_edge_pos_oneway_2(adj,t1,t2,t3):
    n=len(adj)
    #In this, the two teams activate instead of inhibit the third team. 
    for i in range(0,n-t3):
        for j in range(t1+t2,n):
            adj[i][j]=-1*adj[i][j]
    return(adj)

def third_team_edge_pos_twoway(adj,t1,t2,t3):
    n=len(adj)
    for i in range(0,n-t3):
        for j in range(t1+t2,n):
            adj[j][i]=-1*adj[j][i]
            adj[i][j]=-1*adj[i][j]
    return(adj)
'''
The program calculates hybridness with respect to two big teams. As we increase the desnity of the edges from the third team, we see an increase in the number of hybrid states. 

Now we need to run controls to see if just addition of non team like edges does anything. 

One control would be to introduce random edges 

Another control would be to flip the signs 



'''

'''density=nteams.density_mat_gen(2,0.5)
#adj=nteams.nteam_net(2,[5,5],density)[0]


#print(adj)
adj=[[1, 0, 1, 0, 1, -1, -1, -1, 0, 0], [0, 1, 1, 0, 1, -1, 0, -1, 0, -1], [0, 1, 0, 0, 0, -1, 0, 0, -1, 0], [0, 1, 1, 0, 1, -1, 0, 0, 0, 0], [1, 0, 0, 1, 0, -1, 0, -1, -1, 0], [-1, 0, 0, -1, -1, 0, 0, 0, 1, 1], [-1, 0, -1, -1, 0, 1, 0, 0, 1, 1], [-1, 0, 0, 0, -1, 1, 0, 1, 0, 0], [-1, 0, 0, 0, -1, 0, 0, 1, 1, 1], [0, 0, -1, 0, -1, 0, 0, 0, 1, 1]]

steadys=boolean_siml.steady_states(adj,1000)
ssf=boolean_siml.steady_state_frequency(steadys,adj)
print(ssf)
print(hybridness(ssf,5,5,adj))
#boolean_siml.bar_graph(ssf,"hello")
'''
'''
#This is the density plot 
hybrid_score=[]
dens=[]
for i in np.linspace(0,1,20):
    hybs_dist=[]
    for j in range(0,20):
        density=[[0.4,0.4,i],[0.3,0.3,i],[i,i,i]]
        adj=nteams.nteam_net(3,[5,5,1],density)[0]
        steayds=boolean_siml.steady_states(adj,1000)
        ssf=boolean_siml.steady_state_frequency(steayds,adj)
        hybs=hybridness(ssf,5,5,adj)[0]
        hybs_dist.append(hybs)
        print(i,hybs)

    hybrid_score.append(np.mean(hybs_dist))
    dens.append(i)

plt.scatter(dens,hybrid_score)
plt.xlabel("Density of third small team with one node")
plt.ylabel("Average hybridness of network wrt 2 big teams")
plt.show()
'''


#----------------------------------------------------------------------------------------------------------
#Team size plots follow

'''hybrid_score=[]
third_team_size=[]
for i in range(0,10):
    hybs_dist=[]
    for j in range(0,20):
        density=[[0.4,0.4,0.4],[0.4,0.4,0.4],[0.4,0.4,0.4]]
        adj=nteams.nteam_net(3,[5,5,i],density)[0]
        steayds=boolean_siml.steady_states(adj,1000)
        ssf=boolean_siml.steady_state_frequency(steayds,adj)
        hybs=hybridness(ssf,5,5,adj)[0]
        hybs_dist.append(hybs)
        print(i,hybs)

    hybrid_score.append(np.mean(hybs_dist))
    third_team_size.append(i)

plt.scatter(third_team_size,hybrid_score)
plt.xlabel("Size of third team with 0.4 density")
plt.ylabel("Average hybridness of network wrt frst two teams")
plt.show()
'''


#Control case 1: Random swaps (not all useful)

'''hybrid_score=[]
third_team_size=[]
for i in range(0,10):
    hybs_dist=[]
    for j in range(0,20):
        density=[[0.4,0.4,0.4],[0.4,0.4,0.4],[0.4,0.4,0.4]]
        adj= third_team_edge_rand(nteams.nteam_net(3,[5,5,i],density)[0], 5,5,i,30)
        steayds=boolean_siml.steady_states(adj,1000)
        ssf=boolean_siml.steady_state_frequency(steayds,adj)
        hybs=hybridness(ssf,5,5,adj)[0]
        hybs_dist.append(hybs)
        print(i,hybs)

    hybrid_score.append(np.mean(hybs_dist))
    third_team_size.append(i)

plt.scatter(third_team_size,hybrid_score)
plt.xlabel("Size of third team with 0.4 density")
plt.ylabel("Average hybridness of network wrt frst two teams")
plt.show()
'''

#Control case 2: changing inhibitions coming out of third team to activations/ inhibitions coming from two teams to third team from inhibitions to activation//

hybrid_score=[]
third_team_size=[]
for i in range(0,10):
    hybs_dist=[]
    for j in range(0,20):
        density=[[0.4,0.4,0.4],[0.4,0.4,0.4],[0.4,0.4,0.4]]
        adj= third_team_edge_pos_oneway_2(nteams.nteam_net(3,[5,5,i],density)[0], 5,5,i)
        steayds=boolean_siml.steady_states(adj,1000)
        ssf=boolean_siml.steady_state_frequency(steayds,adj)
        hybs=hybridness(ssf,5,5,adj)[0]
        hybs_dist.append(hybs)
        print(i,hybs)

    hybrid_score.append(np.mean(hybs_dist))
    third_team_size.append(i)

plt.scatter(third_team_size,hybrid_score)
plt.xlabel("Size of third team with 0.4 density")
plt.ylabel("Average hybridness of network wrt frst two teams")
plt.show()





