import matplotlib.pyplot as plt 
import nteams
import boolean_siml
import numpy as np 
import boolonezero
import three_states_sim
#Two plots, one is number of steady states with respect to team size and one is number of steady states with respect to density


'''teamsize=[]
nsteady=[]
for i in range(2,15):
    density=nteams.density_mat_gen(3,0.3)
    nsteady_dist=[]
    for j in range(0,20):
        adj=nteams.nteam_net(3,[i, i, i], density)[0]
        steadys=boolean_siml.steady_states(adj,1000)
        ssf=boolean_siml.steady_state_frequency(steadys,adj)
        nsteady_dist.append(len(ssf[0]))
        print(len(ssf[0]))
    nsteady.append(np.mean(nsteady_dist))
    teamsize.append(i)
plt.scatter(teamsize,nsteady)
plt.xlabel("Team size")
plt.ylabel("Number of steady states")
plt.title("Average number of steady states for three teams with density 0.3 ")
plt.show()
'''


#Now the following plot is about density, we choose a certain team size and then look at number of steady states

density_val=[]

den_range=np.linspace(0.7,1,100)

nomsteady=[]

for i in den_range:
    density=nteams.density_mat_gen(2,i)
    nsteady_dist=[]
    for j in range(0,10):
        adj=nteams.nteam_net(2,[5,5], density)[0]
        steadys=three_states_sim.steady_states(adj,1000)
        ssf=boolean_siml.steady_state_frequency(steadys,adj)
        nsteady_dist.append(len(ssf[0]))
        print(i,len(ssf[0]))
    nomsteady.append(np.mean(nsteady_dist))
    density_val.append(i)
    
    
plt.scatter(density_val,nomsteady)
plt.xlabel("Density")
plt.ylabel("Number of steady states")
plt.title("Average number of steady states for two teams with team size 5 ")
plt.show()
