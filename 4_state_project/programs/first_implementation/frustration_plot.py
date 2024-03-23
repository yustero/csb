import multi_rules
import coherent_parser
import matplotlib.pyplot as plt
import topopath
import numpy as np
import randomization

'''  Definition of frustration should change for multi state formalism

In the old definition, an edge is frustrated when S_i* adj[i,j] * S_j is negative and you have only one value for this in case the product is negative that is -1

But in multi level formalism even when the product is positive the edge could be slightly frustrated when both nodes are, lets say at 0.5 instead of 1, the edge would be slightly ineffective.

Hence another way to measure frustration is to subtract the product from its most effective value, i.e 1

in this case the values possible would be 

1-1 (product is 1) = 0
1-(0.5) (product is 0.5) = 0.5

1-0.25( product is 0.25) = 0.75

1-( -0.25) (product is -0.25) = 1.25

1-(-0.5) (product is -0.5) = 1.5

1-(-1) (product is -1) = 2

We can then maybe normalize this by dividing by 2

But in this one, the gaps aren't uniform. Theres a jump from 0 to 0.5 by 0.5 but the next jump is by 0.25 to 0.75 
'''
n=2
print(topopath.topofiles)
file=topopath.topofiles[n]
print(topopath.topofiles)
data=coherent_parser.clustered_matrix_file(file)
adj=data[0]


def mean_frustration(steadys,adj):
    frusts=[]
    for i in steadys:
        frusts.append(multi_rules.frustration(i,adj))
    return(np.mean(frusts))

def frustration_plot(adj):
    steadys0=multi_rules.steady_states(adj,1000)
#Team strength and mean frustration of biological network    
    mf0=mean_frustration(steadys0,adj)
    ts0=coherent_parser.team_strength_file(adj)
    
    plt.scatter(ts0,mf0, color="r")
    
    rand_frustration=[]
    rand_teamstrength=[]
    
    for i in range(0,100):
        radj=randomization.random_edge_exchange(adj,5)
        steadys=multi_rules.steady_states(adj,100)

        rand_frustration.append(mean_frustration(steadys,adj))
        rand_teamstrength.append(coherent_parser.team_strength_file(radj))

        print(rand_frustration[i],rand_teamstrength[i])    

    print(len(rand_frustration), len(rand_frustration))
    plt.scatter(rand_teamstrength,rand_frustration)

    plt.title("Frustration vs Team Strength for multi level boolean formalism")
    plt.xlabel("Team Strength")
    plt.ylabel("Frustration")

    return(plt)

plt=frustration_plot(adj)

plt.show()



