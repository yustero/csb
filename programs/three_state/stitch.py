import boolean_sim
import three_states_sim
import node_metrics
import matplotlib.pyplot as plt
import topopath
import coherent_parser
import hybrid_states
import numpy as np

dat=coherent_parser.clustered_matrix_file(topopath.topofiles[2])
adj=dat[0]
t1=len(dat[1])
t2=len(dat[2])
ti=45
data=boolean_sim.steady_states_time_regsig(adj,1000)[2]
n=len(adj)

end=60

mean_dist=[[] for x in range(0,n)]
var_dist=[[] for x in range(0,n)]
x_axis=[i for i in range(0,end,5)]
for i in range(0,end,5):    
    
    abs_sorted=[]
    sorted_data=boolean_sim.resig_sort(data,i,adj)
    
    for j in sorted_data:
        abs_sorted.append([abs(k) for k in j])
    for l in range(0,n):
        mean_dist[l].append(np.mean(abs_sorted[l]))
        var_dist[l].append(np.var(abs_sorted[l]))

for i in range(0,n):
    plt.plot(x_axis, var_dist[i], linestyle="-",marker="o", alpha=0.5,label="node{}".format(i) )
    

plt.legend(loc="upper left")
plt.xlabel("Time steps")
plt.ylabel("Variation")
plt.title("EMT Racipe2 evolution of canalising value")
plt.show()