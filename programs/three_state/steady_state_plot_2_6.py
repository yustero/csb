import boolean_siml
import nteams
import matplotlib.pyplot as plt
import json
import os
import csv

d=0.8
os.chdir("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/2_3_teams/panel1/steady_2_6")
for i in range(2,7):
    density=nteams.density_mat_gen(i,d)
    adj=nteams.nteam_net(i,[5 for z in range(0,i)],density)[0]
    
    steadys=boolean_siml.steady_states(adj,1000)
    ssf=boolean_siml.steady_state_frequency(steadys,adj)
    plt =boolean_siml.bar_graph_2(ssf)
    plt.title("{}_teams_density".format(i,d))
    plt.savefig("{}teams_d{}_steadystates.png".format(i,d))
    with open("{}teams_d{}_steadystates.csv".format(i,d),"w",newline="") as file:

        writer=csv.writer(file)
        writer.writerow(["steadystate","frequency"])
        for i in range(len(ssf[0])):
            writer.writerow([ssf[0][i],ssf[1][i]])
    print(i)