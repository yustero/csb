import artificial 
import input_space_map as isp
import coherent_parser
import topopath
import node_metrics

'''What to do? 
Establish that higher densities don't have hybrid nodes
Try to alternate densities between teams and stuff 
Quantify specific sparcities in biological networks
'''

for i in topopath.topofiles:
    data=coherent_parser.clustered_matrix_file(i)
    adj=data[0]

    print(i,node_metrics.edge_breakdown(adj),len(data[1]),len(data[2]))

d2=[0.24793388429752067, 0.05555555555555555, 0.17424242424242425, 0.21212121212121213]
d1=[0.26666666666666666, 0.35802469135802467, 0.0, 0.2222222222222222, 0.35185185185185186]
dgon=[0.20118343195266272, 0.44, 0.18461538461538463, 0.26153846153846155]
t1gon=13
t2gon=5

dsclc=[0.40828402366863903, 0.2875, 0.3769230769230769, 0.2884615384615384]
t1sc=13
t2sc=20

#adj=artificial.network(t1gon,t2gon,dgon[0],dgon[1],dgon[2],dgon[3])[0]
#nodes=[x for x in range(0,t1gon+t2gon)]

adj=artificial.network(t1sc,t2sc,dsclc[0],dsclc[1],dsclc[2],dsclc[3])[0]
nodes=[x for x in range(0,t1sc+t2sc)]
adj=artificial.network(t1sc,t2sc,d1[0],d1[1],d1[2],d1[3])[0]


dist=isp.overtime_incan_triple(adj,1000)
data=isp.incan_all_path_dist_graph_indeg_normal(dist,100,2,adj)

plot=isp.incan_dist_plot_all_nodes_static_colored(data,nodes)
#plot.title("{}_normalized incan".format(topopath.topofiles[n]))
plot.title("random artificial network with same density as gon.topo ")
plot.show()
