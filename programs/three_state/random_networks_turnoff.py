import topopath
import three_states_sim as tss 
import randomization
import coherent_parser
import boolean_siml as bs

k=2
network=coherent_parser.clustered_matrix_file(topopath.topofiles[k])
adj=network[0]
print(network[-1])
number_steady=[]

steadys=bs.steady_states(adj,1000)
ssf=bs.steady_state_frequency(steadys,adj)

print(len(ssf[0]),ssf)
number_steady.append(len(ssf[0]))
for i in range(0,100):
    adjr=randomization.random_edge_exchange(adj,15)
    steadys=bs.steady_states(adjr,1000)
    ssf=bs.steady_state_frequency(steadys,adjr)
    number_steady.append(len(ssf[0]))
    print(len(ssf[0]), ssf)
    print(number_steady)
    print("---------------------------")

print(number_steady)


#tss, 15 swaps : [2, 0, 4, 2, 0, 0, 0, 0, 2, 0, 16, 0, 4, 0, 6, 0, 0, 0, 20, 0, 0, 0, 2, 2, 6, 0, 12, 8, 6, 0, 2, 2, 4, 0, 6]
#bs, 15 swaps : [11, 68, 4, 78, 10, 12, 0, 14, 47, 39, 6, 8, 9, 38, 0, 23, 0, 12, 20, 64, 12, 8, 0, 0, 18, 8, 8, 6, 70, 31, 10, 24, 9, 87, 36, 8, 19, 0, 45, 15, 93, 18, 6, 4, 4, 0, 102, 12, 0, 4, 16, 20, 10]
#tss simulations take so long man. 