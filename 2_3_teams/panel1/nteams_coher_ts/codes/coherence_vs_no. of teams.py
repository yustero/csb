import artificial as art
import matplotlib.pyplot as plt
import boolean_formalism as bf
import numpy as np

strengths=[]
teaminstates=[] #list of initial states for each no. of teams
for n in range(0,5):
    teaminstates.append([])
    if (n+2)==2: #2 teams
        state=[]
        for i in range(10):
            state.append(1) if i<5 else state.append(-1) #1 team ON
        teaminstates[n].append(state)
    if (n+2)==3: #3teams
        state1=[]
        state2=[]
        for i in range(15):
            state1.append(1) if i<5 else state1.append(-1) #1 team ON
            state2.append(1) if i<10 else state2.append(-1) #2 teams ON
        teaminstates[n].append(state1)
        teaminstates[n].append(state2)
    if (n+2)==4: #4teams
      
        state=[]
        for i in range(20):
            state.append(1) if i<10 else state.append(-1) #2teams ON
            
        teaminstates[n].append(state)
       
    if (n+2)==5: #5teams
        state1=[]
        state2=[]
        for i in range(25):
            state1.append(1) if i<10 else state1.append(-1) #2 teams ON
            state2.append(1) if i<15 else state2.append(-1) #3 teams ON
        teaminstates[n].append(state1)
        teaminstates[n].append(state2)
        
    if (n+2)==6: #6teams
        state=[]
        for i in range(30):
            state.append(1) if i<15 else state.append(-1) #3 teams ON
          
        teaminstates[n].append(state)
        
perturbs=[]         
cohers =[]
density=0.8
networks=[]
for n in range(2,7):
    cohers.append([])
    net,teams=art.uniformnetwork(n, 5, density) #n team(5 nodes each) network with uniform density
    networkname=str(n)+"_teams_density_"+str(density)
    networks.append(net)
    np.savetxt("C:\\Users\\halda\\codes\\nteams_coher_ts\\coherence\\networks\\{}.csv".format(networkname), net, delimiter=",") #save to csv file
    for state in teaminstates[n-2]:
        cohers[n-2].append([])
        
perturbs=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9] # bin for proportion of nodes perturbed
for perturb in perturbs:
    print(perturb)
    for n in range(2,7): #no. of teams from 2 to 6
        print(n)
        for state in teaminstates[n-2]:
            cohers[n-2][teaminstates[n-2].index(state)].append(bf.coherence(state, networks[n-2], int(perturb*n*5))) # get coherence of corresponding steady states

coherences=[]
for coher in cohers:
    for i in coher:
        coherences.append(i)
           
phens=["2 teams: 1 ON","3 teams: 1 ON","3 teams: 2 ON","4 teams: 2 ON","5 teams: 2 ON","5 teams: 3 ON","6 teams: 3 ON"]
for i in range(len(phens)):
    plt.plot(perturbs, coherences[i] , label=phens[i])


plt.title("Density= "+str(density))
plt.ylabel("Coherence")
plt.xlabel("Proportion of perturbed nodes")
plt.legend()
plt.show()
        
        