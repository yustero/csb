import cumulative_drive
import coherent_parser
import topopath
import boolean_siml
import cumulative_drive as cumd
import randomization
import numpy as np
import matplotlib.pyplot as plt


n=0
file=topopath.topofiles[n]
print(topopath.topofiles)
data=coherent_parser.clustered_matrix_file(file)
adj=data[0]

def teamstrentgh_vs_drive_plot(adj):
    steadys0=boolean_siml.steady_states(adj,100)
 

    drivedist=cumd.drive_dist(steadys0,adj)


    avd0= np.average(cumd.average_drive(drivedist,adj))
    ts0=coherent_parser.team_strength_file(adj)
    
    plt.scatter(ts0,avd0, color="r")
    
    rand_average_drive=[]
    rand_teamstrength=[]
    
    for i in range(0,100):
        radj=randomization.random_edge_exchange(adj,5)
        steadys=boolean_siml.steady_states(adj,100)

        drivedist=cumd.drive_dist(steadys,adj)

        rand_average_drive.append(np.average(cumd.average_drive(drivedist,adj)))
        rand_teamstrength.append(coherent_parser.team_strength_file(radj))

        print(rand_average_drive[i],rand_teamstrength[i])    
        
    plt.scatter(rand_teamstrength,rand_average_drive)

    plt.title("Average drive vs Team Strength for multi level boolean formalism")
    plt.xlabel("Team Strength")
    plt.ylabel("Average drive")

    return(plt)

plt=teamstrentgh_vs_drive_plot(adj)
plt.show()
