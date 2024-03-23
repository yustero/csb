import nested_canalysing_first as ncf
import matplotlib.pyplot as plt
import sample_networks as snet
import numpy as np

#print(ncf.random_priority(ncf.in_nodes(snet.pure_1[0])))


data=snet.pure_1_same_team_priority
adj=data[0]
t1=data[1]
t2=data[2]


#prioritys=data[3]
prioritys=ncf.random_priority(adj)



steadys=ncf.steady_states(adj,1000,prioritys)
ssf=ncf.steady_state_frequency(steadys,adj)
for i in ssf[0]:
    print(i)
print(len(ssf[0]))

#print("same team: ",ncf.same_team_priority(adj,t1,t2))

#print("other team: ",ncf.opposite_team_priority(adj,t1,t2))


print(np.mean(ncf.random_score_distribution(adj,t1,t2,1000)))
print(np.mean(ncf.random_score_2_distribution(adj,t1,t2,1000)))
print(np.mean(ncf.team_score_distribution(steadys,t1,t2,adj)))
print(np.mean(ncf.team_score_2_distribution(steadys,t1,t2,adj)))


