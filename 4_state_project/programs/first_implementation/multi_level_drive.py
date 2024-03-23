import multi_rules
import topopath
import coherent_parser

print(topopath.topofiles)

network=coherent_parser.clustered_matrix_file(topopath.topofiles[4])
adj=network[0]

print(adj)
steadys=multi_rules.steady_states(adj,10000)
ssf=multi_rules.steady_state_frequency(steadys,adj)

print(ssf)

count=0
for i in ssf[1]:
    count+=i
print("Num steady:", count)