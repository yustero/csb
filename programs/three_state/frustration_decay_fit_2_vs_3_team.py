import three_states_sim
import interaction_matrices
import boolean_siml
import boolonezero
import matplotlib.pyplot as plt 
import fitting_to_frustration_overtime as fft
import nteams
import numpy as np 


for i in range(0,50):

    den1=nteams.density_mat_gen(2,0.3)
    adj1=nteams.nteam_net(2,[6,6],den1)[0]

    states1=boolean_siml.steady_states_evol(adj1,1000)[1]


    mean_frustrated_edges1=interaction_matrices.norm_frustrated_cumul(states1,adj1,80)


    time1=[x for x in range(len(mean_frustrated_edges1))]

    popt,pcov=fft.curve_fit(fft.exponential,time1,mean_frustrated_edges1)
    print(popt)
    x=np.array(time1)
    rsq=fft.get_rsq(fft.exponential,mean_frustrated_edges1,popt,x)
    print(rsq)

    plt.scatter(popt[0],popt[1], color="r" )
#------------------------ Three teams below
    den1=nteams.density_mat_gen(3,0.3)
    adj1=nteams.nteam_net(3,[4,4,4],den1)[0]

    states1=boolean_siml.steady_states_evol(adj1,1000)[1]


    mean_frustrated_edges1=interaction_matrices.norm_frustrated_cumul(states1,adj1,50)


    time1=[x for x in range(len(mean_frustrated_edges1))]

    popt,pcov=fft.curve_fit(fft.exponential,time1,mean_frustrated_edges1)
    print(popt)
    x=np.array(time1)
    rsq=fft.get_rsq(fft.exponential,mean_frustrated_edges1,popt,x)
    print(rsq)

    plt.scatter(popt[0],popt[1], color="green" )

plt.xlabel("Value of a")
plt.ylabel("Value of -b")
plt.title("Frustration decay comparision of two teams(red) and three teams(green)")
plt.show()



