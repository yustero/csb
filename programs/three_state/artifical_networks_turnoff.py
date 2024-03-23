import three_states_sim as tss
import artificial
import boolean_siml as bs
import matplotlib.pyplot as plt
import numpy as np


def numpy_to_li(adj):
    network=[]
    for i in adj:
        network.append(list(i))
    return(network)


#The following list has the number of steady states obtained via ising and then obtained via turn_off 

tssli=[]
bsli=[]
for i in range(0,500):

    adj=numpy_to_li(artificial.network(8,8,0.3,0.3,0.3,0.3)[0])
    steadys=bs.steady_states(adj,1000)
    ssf=bs.steady_state_frequency(steadys,adj)

    steadytss=tss.steady_states(adj,1000)
    ssftss=tss.steady_state_frequency_li(steadytss,adj)
    
    print(len(ssf[0]), len(ssftss[0]))
    tssli.append( len(ssftss[0]))
    bsli.append(len(ssf[0]))

plt.scatter(tssli,bsli)
plt.ylabel("Number of solutions with ising")
plt.xlabel("Number of solutions with three state")
plt.title("Density 0.3 , t1=t2=8")
plt.show()

'''while True:
    network= numpy_to_li(artificial.network(8,8,0.3,0.3,0.3,0.3)[0])
    steadys=three_states_sim.steady_states(network,1000)
    ssf=three_states_sim.steady_state_frequency(steadys,network)
    
    if len(ssf[0])>3:
        print(network)
'''