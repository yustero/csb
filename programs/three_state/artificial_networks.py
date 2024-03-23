#This program is supposed to collect artificial networks which give steady states with turn off formalism 

import artificial
import three_states_sim
import numpy as np
import node_metrics
import numpy as np
import matplotlib.pyplot as plt



'''while True:
    net=artificial.network(7,7,0.3,0.3,0.3,0.3)
    adj=net[0]
    steadys=three_states_sim.steady_states(adj,1000)
    ssf=three_states_sim.steady_state_frequency(steadys,adj)
    if len(ssf[0])>3:
        print(ssf[0])
        print(node_metrics.indegree(adj))
        print("--------------------------")

'''

#Estimating rarity of more than 3 solutions in artificial networks 
'''d=0.2
count=0
ideal_count=0
while True:
    count+=1
    net=artificial.network(7,7,d,d,d,d)
    adj=net[0]
    steadys=three_states_sim.steady_states(adj,1000)
    ssf=three_states_sim.steady_state_frequency(steadys,adj)
    print(len(ssf[0]))
    if len(ssf[0])>3:
        ideal_count+=1
        print(count,ideal_count)
'''

def hyb_solution_check(adj):
    steadys=three_states_sim.steady_states(adj,1000)
    ssf=three_states_sim.steady_state_frequency(steadys,adj)
    num_sol=len(ssf[0])
#    print(len(ssf[0]))
    if num_sol>3:
#        print("greater value")
        return(True)

    if num_sol<=3:
        return(False)

def hyb_sol_freq_count(density,teamsize,num):
    count=0
    for i in range(0,num):
        net=artificial.network(teamsize,teamsize,density,density,density,density)
        adj=net[0]
        if hyb_solution_check(adj):
            count+=1
#            print("Count increased to:", count)
            
    freq=count/num
    return(freq)



densities=[]
frequencies=[]
for i in np.linspace(0.0,0.5,10):
    
    freq = hyb_sol_freq_count(i,7,100)
    
    densities.append(i)
    frequencies.append(freq)
    print(i,freq)
print(densities,frequencies)

plt.scatter(densities,frequencies)
plt.xlabel("Density")
plt.ylabel("Frequency")
plt.show()



