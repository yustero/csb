import topopath
import matplotlib.pyplot as plt 
import probablistic_turn_off as pto
import coherent_parser
import numpy as np

k=2
print(topopath.topofiles)

network=coherent_parser.clustered_matrix_file(topopath.topofiles[k])

adj=network[0]
print(adj)
prob_range=list(np.linspace(0,1,10))
nsteady=[]

for i in range(0,len(prob_range)):
    steadys=pto.steady_states(adj,1000,prob_range[i])

    ssf=pto.steady_state_frequency(steadys,adj)
    nsteady.append(len(ssf[0]))
    print(len(ssf[0]), prob_range[i])
plt.scatter(nsteady,prob_range)
plt.xlabel("Number of steady states ")
plt.ylabel("Probability of turn off")
plt.title("Probablistic _turn_off_{}".format(topopath.topofiles[k]))
plt.show()