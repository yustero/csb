import boolean_siml
import coherent_parser
import matplotlib.pyplot as plt
import topopath
import numpy as np
import randomization
import cumulative_drive as cumd


def mean_frustration(steadys,adj):
    frusts=[]
    for i in steadys:
        frusts.append(boolean_siml.frustration(i,adj))
    return(np.mean(frusts))

def frustration_plot(adj):
    steadys0=boolean_siml.steady_states(adj,1000)
#Team strength and mean frustration of biological network    
    mf0=mean_frustration(steadys0,adj)
    ts0=coherent_parser.team_strength_file(adj)
    
    plt.scatter(ts0,mf0, color="r")
    
    rand_frustration=[]
    rand_teamstrength=[]
    
    for i in range(0,100):
        radj=randomization.random_edge_exchange(adj,5)
        steadys=boolean_siml.steady_states(adj,100)

        rand_frustration.append(mean_frustration(steadys,adj))
        rand_teamstrength.append(coherent_parser.team_strength_file(radj))

        print(rand_frustration[i],rand_teamstrength[i])    
        
    plt.scatter(rand_teamstrength,rand_frustration)

    plt.title("Frustration vs Team Strength for multi level boolean formalism")
    plt.xlabel("Team Strength")
    plt.ylabel("Frustration")

    return(plt)

def frustration_vs_drive_plot(adj):
    steadys0=boolean_siml.steady_states(adj,1000)
 

    drivedist=cumd.drive_dist(steadys0,adj)


    avd0= np.average(cumd.average_drive(drivedist,adj))
    mf0=mean_frustration(steadys0,adj)
    
    plt.scatter(mf0,avd0, color="r")
    
    rand_average_drive=[]
    rand_frustration=[]
    
    for i in range(0,100):
        radj=randomization.random_edge_exchange(adj,5)
        steadys=boolean_siml.steady_states(adj,1000)

        drivedist=cumd.drive_dist(steadys,adj)

        rand_average_drive.append(np.average(cumd.average_drive(drivedist,adj)))
        rand_frustration.append(mean_frustration(steadys,adj))

        print(rand_average_drive[i],rand_frustration[i])    
        
    plt.scatter(rand_frustration,rand_average_drive)

    plt.title("Average drive vs Frustration")
    plt.xlabel("Frustration")
    plt.ylabel("Average drive")

    return(plt)


n=0
file=topopath.topofiles[n]
print(topopath.topofiles)
data=coherent_parser.clustered_matrix_file(file)
adj=data[0]

plt=frustration_vs_drive_plot(adj)
plt.show()