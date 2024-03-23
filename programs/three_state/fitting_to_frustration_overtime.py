from scipy.optimize import curve_fit
import numpy as np 
import three_states_sim
import interaction_matrices
import topopath
import matplotlib.pyplot as plt 
import coherent_parser
from pylab import * 
import randomization





def exponential(t,a,b):
    return(a* np.exp(-b*t))

def get_rsq(f, y, popt,x):

    ss_res = np.dot((y - exponential(x, *popt)),(y - exponential(x, *popt)))
    ymean = np.mean(y)
    ss_tot = np.dot((y-ymean),(y-ymean))
    return 1-ss_res/ss_tot

'''print(topopath.topofiles)
k=2
network = coherent_parser.clustered_matrix_file(topopath.topofiles[k])
adj=network[0]
t1=len(network[1])


states=three_states_sim.steady_states_evol(adj,1000)[1]


mean_frustrated_edges=interaction_matrices.norm_frustrated_cumul(states,adj,120)


time=[x for x in range(len(mean_frustrated_edges))]

popt,pcov=curve_fit(exponential,time,mean_frustrated_edges)
print(popt)
x=np.array(time)
rsq=get_rsq(exponential,mean_frustrated_edges,popt,x)
print(rsq)

plt.scatter(popt[0],popt[1], color="r" )

randoma=[]
randomb=[]
for i in range(0,20):
    [[0.4, 0.4, 0.4], [0.4, 0.4, 0.4], [0.4, 0.4, 0.4]]
    #above adj is three teams with 0.4 density
    adj=randomization.random_edge_exchange(adj,5)
    states=three_states_sim.steady_states_evol(adj,1000)[1]


    mean_frustrated_edges=interaction_matrices.norm_frustrated_cumul(states,adj,120)


    time=[x for x in range(len(mean_frustrated_edges))]

    popt,pcov=curve_fit(exponential,time,mean_frustrated_edges)
    print(popt)
    x=np.array(time)
    rsq=get_rsq(exponential,mean_frustrated_edges,popt,x)
    print(rsq)

    randoma.append(popt[0])
    randomb.append(popt[1]) 
    
plt.scatter(randoma,randomb)
plt.title("a,b biological network vs random (5 edge swap)")
plt.show()
#plt.scatter(time,mean_frustrated_edges)
#time2=np.linspace(0,120,300)
#plt.plot(time2, exponential(time2,popt[0], popt[1]))
#plt.scatter(time,mean_frustrated_edges)
#plt.title("{}_rsq:{}_a:_{}_b:{}".format(rsq,topopath.topofiles[k], popt[0],popt[1]))
#plt.show()
'''

'''

'''