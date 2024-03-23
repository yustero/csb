import artificial as art
import phenotype as pn
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc 
import statistics as stat
strengths=[]
nteams=[]
density=0.8 #change as per requirement
for n in range(2,7): #no. of teams ranging from 2 to 6
    nteams.append(n)
    ts=[]
    for i in range(1000): #1000 networks for each n
        print(n,i)
        net,teams=art.uniformnetwork(n, 5, density) #n team(5 nodes each) network with uniform density
        ts.append(np.round(pn.strength(pn.influence(net), teams),2)) #find team strength
    strengths.append(ts)

tsmeans=[]
for t in strengths:
    tsmeans.append(stat.mean(t)) #find mean team strength for each n
def monoExp(x, m, t, b): #decreasing exponential
    return m * np.exp(-t * x) + b
nteams=np.array(nteams)
params1=sc.optimize.curve_fit(monoExp,nteams,tsmeans)[0] #fit means to monoexp
yfit1=params1[0]*np.exp(-params1[1]*nteams)+params1[2]
label1=str(np.round(params1[0],2))+"e^(-"+str(np.round(params1[1],2))+"x)"+" +"+str(np.round(params1[2],2)) 
plt.plot(nteams,yfit1, label=label1)    
plt.violinplot(strengths,nteams)
plt.title("Density= "+str(density))
plt.ylabel("Team strength")
plt.xlabel("No. of teams")
plt.legend()
plt.show()
