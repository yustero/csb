import random 
import copy 
import artificial
import matplotlib.pyplot as plt
import three_states_sim
import boolean_siml
import randomization
import numpy as np
import coherent_parser

def edge_inversion(adj,k):
    n=len(adj)
    rand2=copy.deepcopy(adj)
    i=0
    while i<k:
        a=random.randint(0,n-1)
        b=random.randint(0,n-1)
        if rand2[a][b]!=0:
            rand2[a][b]=rand2[a][b]* (-1)
            i+=1 
    return(rand2)

#The following plot is number of edge sign change vs steady_states. One could also plot team strength vs number of steady states. 
#Another plot I could generate would be epithellial mes score vs team strength and show that even at low team strengths we get terminal states. 

d=0.3
adj=artificial.network(8,8,d,d,d,d)[0]

'''nsteady=[]
rand=[]
for i in range(0,20):
    radj=randomization.random_edge_exchange(adj,i)
    steadys=three_states_sim.steady_states(radj,1000)
    ssf=three_states_sim.steady_state_frequency_li(steadys,radj)
    nsteady.append(len(ssf[0]))
    rand.append(i)
    print(nsteady[i],rand[i])

plt.scatter(rand,nsteady)
plt.xlabel("Number of edge sign change")
plt.ylabel("Number of steady states")
plt.title("Number of steady states vs number of frustrated edges")
plt.show()
'''


'''#The following gets the histogram for distribution of number of steady states for number of steady states for a fixed number of randomizations
nsteady=[]
for i in range(0,100):
    radj=randomization.random_edge_exchange(adj,5)
    steadys=three_states_sim.steady_states(radj,1000)
    ssf=three_states_sim.steady_state_frequency_li(steadys,radj)
    nsteady.append(len(ssf[0]))
    print(nsteady[i])

print(np.mean(nsteady))
plt.hist(nsteady)
plt.title("Number of steady states for 5 swaps")
plt.show()
'''



#The following gets the team strength vs number of steady states distribution for a fixed number of randomizations

nsteady=[]
team_strength=[]

for i in range(0,100):
    radj=randomization.random_edge_exchange(adj,5)
    steadys=boolean_siml.steady_states(radj,1000)
    ssf=boolean_siml.steady_state_frequency(steadys,radj)
    ts=coherent_parser.team_strength_file(radj)

    nsteady.append(len(ssf[0]))
    team_strength.append(ts)

    print(nsteady[i],ts)

plt.scatter(team_strength,nsteady)
plt.xlabel("Team Strength")
plt.ylabel("Number of steady states")
plt.title("Team Strength vs Number of steady states ")
plt.show()