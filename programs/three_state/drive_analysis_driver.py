#This is supposed to be the driver of the program drive analysis.
#This is supposed to selectively turn off k nodes having low values and then compare it to random k nodes.

import selective_turnoff_increase as stf
import drive_analysis as dany
import random 
import topopath
import matplotlib.pyplot as plt 
import coherent_parser



'''#The below program takes a network from topopath.topofiles and then selects k nodes with low drive values and calculates the number of steady states obtained after applying turnoff formalism 
# to those k ndoes and compares it to applying turn off formalism to random k nodes. 
i=0
k=3
network= coherent_parser.clustered_matrix_file(topopath.topofiles[i])
adj=network[0]
nodes=network[-1]


data=dany.overtime_drive_3_state(adj,1000)
drive_data=dany.drive_all_path_dist_graph_indeg_normal(data,100,2,adj)

no_steady=[]

node_rank=dany.drive_order(dany.drive_rank(drive_data,nodes))

noisy_nodes=node_rank[0:3]

steadys=stf.steady_states(adj,1000,noisy_nodes)
ssf=stf.steady_state_frequency(steadys,adj)
nss0=len(ssf[0])
print(nss0)

no_steady.append(nss0)

n=len(adj)

nodes= [x for x in range(0,n)]



for i in range(0,100):
    noisy_buff=random.sample(nodes,3)
    steadys=stf.steady_states(adj,1000,noisy_buff)
    ssf=stf.steady_state_frequency(steadys,adj)
    no_steady.append(len(ssf[0]))
    print(noisy_buff,len(ssf[0]))

print(no_steady)


#emtracipe15 = [4, 8, 10, 7, 9, 10, 8, 4, 6, 6, 13, 7, 8, 8, 8, 9, 13, 7, 8, 5, 9, 8, 8, 9, 11, 11, 11, 5, 7, 12, 8, 10, 7, 10, 8, 7, 11, 8, 9, 21, 10, 5, 11, 4, 8, 6, 11, 7, 7, 8, 6, 7, 14, 11, 6, 12, 6, 5, 7, 6, 9, 7, 10, 9, 9, 6, 5, 9, 9, 12, 9, 4, 4, 11, 7, 11, 11, 8, 9, 6, 7, 11, 8, 6, 12, 8, 10, 7, 10, 6, 11, 9, 11, 10, 8, 12, 4, 4, 6, 4, 10]
'''


#The below program returns drive plots over simulations for certain networks 0,1 -1, -3


for i in [0,1,-1,-3]:
    network= coherent_parser.clustered_matrix_file_peri_included(topopath.topofiles[i])
    adj=network[0]
    nodes=network[-1]
    print(topopath.topofiles[i])

    data=dany.overtime_drive_3_state(adj,1000)
    drive_data=dany.drive_all_path_dist_graph_indeg_normal(data,100,2,adj)

    plt=dany.drive_dist_plot_all_nodes(drive_data,nodes)
    plt.title("Drive_analysis_{}".format(topopath.topofiles[i]))
    plt.show()