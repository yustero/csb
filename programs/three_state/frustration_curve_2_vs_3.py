import three_states_sim
import interaction_matrices
import boolean_siml
import boolonezero
import matplotlib.pyplot as plt 
import fitting_to_frustration_overtime
import nteams
import numpy as np 

#We generate a 12 node network with 0.3 density first having two teams and then having three teams

den1=nteams.density_mat_gen(2,1)
adj1=nteams.nteam_net(2,[5,5],den1)[0]

den2=nteams.density_mat_gen(3,1)
adj2=nteams.nteam_net(3,[5,5,5],den2)[0]

den3=nteams.density_mat_gen(4,1)
adj3=nteams.nteam_net(4,[5,5,5,5],den3)[0]

den4=nteams.density_mat_gen(5,1)
adj4=nteams.nteam_net(5,[5,5,5,5,5],den4)[0]

den5=nteams.density_mat_gen(6,1)
adj5=nteams.nteam_net(6,[5,5,5,5,5,5],den5)[0]

den6=nteams.density_mat_gen(7,1)
adj6=nteams.nteam_net(7,[5,5,5,5,5,5,5],den6)[0]

den7=nteams.density_mat_gen(8,1)
adj7=nteams.nteam_net(8,[5,5,5,5,5,5,5,5],den7)[0]

steadys1=boolean_siml.steady_states(adj1,1000)
steadys2=boolean_siml.steady_states(adj2,1000)
steadys3=boolean_siml.steady_states(adj3,1000)
steadys4=boolean_siml.steady_states(adj4,1000)
steadys5=boolean_siml.steady_states(adj5,1000)
steadys6=boolean_siml.steady_states(adj6,1000)
steadys7=boolean_siml.steady_states(adj7,1000)



data1=interaction_matrices.norm_frustrated_cumul_steady(steadys1,adj1)
data2=interaction_matrices.norm_frustrated_cumul_steady(steadys2,adj2)
data3=interaction_matrices.norm_frustrated_cumul_steady(steadys3,adj3)
data4=interaction_matrices.norm_frustrated_cumul_steady(steadys4,adj4)
data5=interaction_matrices.norm_frustrated_cumul_steady(steadys5,adj5)
data6=interaction_matrices.norm_frustrated_cumul_steady(steadys6,adj6)
data7=interaction_matrices.norm_frustrated_cumul_steady(steadys7,adj7)

print(data1[0],data2[0],data3[0],data4[0],data5[0],data6[0])

frust1_dist=data1[0]
frust2_dist=data2[0]
frust3_dist=data3[0]
frust4_dist=data4[0]
frust5_dist=data5[0]
frust6_dist=data6[0]
frust7_dist=data7[0]

bins = np.linspace(0,1,100)
plt.hist(frust1_dist,bins,label="2 teams" ,alpha =0.8)
plt.hist(frust2_dist,bins, label="3 teams", alpha=0.8)
plt.hist(frust3_dist,bins,label="4 teams", alpha =0.8)
plt.hist(frust4_dist,bins,label="5 teams", alpha =0.8)
plt.hist(frust5_dist,bins,label="6 teams", alpha =0.8)

plt.xlabel("Frustration")
plt.ylabel("Frequency")
plt.legend(loc="upper right")
plt.show()



#This plot is for introducing a third team into two teams and tracing mean frustration as we increase its size. 

'''density=nteams.density_mat_gen(3,0.3)
mean_frust=[]
third_team_size=[]
for i in range(0,12):
    frust_dist=[]
    
    for j in range(0,10):
        adj=nteams.nteam_net(3,[6,6,i],density)[0]
        steadys=boolean_siml.steady_states(adj,1000)
        frust_dist.append(interaction_matrices.norm_frustrated_cumul_steady(steadys,adj)[1])
        print(frust_dist[j],i)
    mean_frust.append(np.mean(frust_dist))
    third_team_size.append(i)

plt.scatter(third_team_size,mean_frust)
plt.xlabel("Size of third team")
plt.ylabel("Mean frustration with d=0.3") 
plt.show() 
'''

#Now we try team size and varying density 


'''mean_frust=[]
third_team_density=[]
for i in np.linspace(0,1,20):
    density=[[0.3, 0.3, 0.3], [0.3, 0.3, 0.3], [i,i,i]]
    frust_dist=[]
    
    for j in range(0,10):
        adj=nteams.nteam_net(3,[6,6,6],density)[0]
        print(density)
        steadys=boolean_siml.steady_states(adj,1000)
        frust_dist.append(interaction_matrices.norm_frustrated_cumul_steady(steadys,adj)[1])
        print(frust_dist[j],i)
    mean_frust.append(np.mean(frust_dist))
    third_team_density.append(i)

plt.scatter(third_team_density,mean_frust)
plt.xlabel("Density of third team")
plt.ylabel("Mean frustration with three equal sized teams with varying density") 
plt.show()   
'''