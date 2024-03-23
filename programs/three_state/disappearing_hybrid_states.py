import topopath
import three_states_sim
import boolean_siml
import coherent_parser

k=8
network=coherent_parser.clustered_matrix_file(topopath.topofiles[k])
print(topopath.topofiles[k])
adj=network[0]
nodes=network[-1]

steadys=boolean_siml.steady_states(adj,1000)
ssf=boolean_siml.steady_state_frequency(steadys,adj)

boolean_states=ssf[0]




for i in range(len(ssf[0])):
    print(ssf[0][i], ":", ssf[1][i])

print("----------------")
data=three_states_sim.steady_states_time_ext_steady(adj,boolean_states)
for i in range(len(data[0])):
    print(data[0][i], data[1][i])