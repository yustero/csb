import non_absolute_drive as nad
import topopath
import matplotlib.pyplot as plt 
import coherent_parser
import artificial

i=4
d=0.3
network= coherent_parser.clustered_matrix_file(topopath.topofiles[i])
network=artificial.network(8,8,d,d,d,d)
nodes=network[1]+network[2]
adj=network[0]



data=nad.overtime_drive_3_state(adj,1)
drive_data=nad.drive_all_path_dist_graph_indeg_normal(data,30,2,adj)

print(len(network[1]))
plt=nad.drive_dist_plot_all_nodes(drive_data,nodes)
plt.title("Non absolute drive for 1 trijectory")
plt.xlabel("Time")
plt.ylabel("non abs drive")
plt.show()