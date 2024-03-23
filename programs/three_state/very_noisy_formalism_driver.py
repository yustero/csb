import topopath
import three_states_sim as tss
import very_noisy_formalism as vnf
import three_state_control as tsc
import coherent_parser

k=2

print(topopath.topofiles)

network=coherent_parser.clustered_matrix_file(topopath.topofiles[k])

adj=network[0]

steadys1=tss.steady_states(adj,1000)

steadys2=tsc.steady_states(adj,1000)

steadys3=vnf.steady_states(adj,1000)

ssf1=tss.steady_state_frequency(steadys1,adj)
ssf2=tsc.steady_state_frequency(steadys2,adj)
ssf3=vnf.steady_state_frequency(steadys3,adj)

print(len(ssf1[0]), len(ssf2[0]), len(ssf3[0]))

print(ssf1)
print(ssf2)
print(ssf3)