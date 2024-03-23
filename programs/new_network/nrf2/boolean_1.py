import random
import numpy as np
import parser
import matplotlib.pyplot as plt


   


def subtract(a,b):
    output= np.zeros(len(a))
    for i in range(len(a)):
        output[i]= a[i]-b[i]
    return(output)

def inli(a,b):
    for i in b:
        if (i==a):
            return(True)
def notli(a,b):
    counter =0
    for i in b:
        if (i==a):
            counter+=1
    if counter ==0:
        return(True)

def evolve(nodes_initial,adj):
    timestep=0
    nodes_states=nodes_initial
    counter=0

    while True:
        zero=np.zeros(len(nodes_initial))
        k= random.randint(0,len(nodes_states)-1)
        state_calc=0
        check=nodes_states
        for i in range(0,len(nodes_initial)):
            state_calc+= nodes_states[i] * adj[i][k]

        if state_calc>0:

            if nodes_states[k] ==1:
                pass
            if nodes_states[k]== -1:

                nodes_states[k] = 1
        if state_calc<0:
            if nodes_states[k] == -1:
                pass
            if nodes_states[k]== 1:

                nodes_states[k] = -1
        timestep+=1
        if timestep == 1000:
            break
        if (subtract(check,nodes_states)== zero).any():
            counter+=1
        if counter == 100:
            return(nodes_states)
            break
        
        check=nodes_states

def random_inputs(adj):
    nodes_initial=[]
    for i in range(len(adj)):
        k = random.choice([-1,1])
        nodes_initial.append(k)
    return(np.array(nodes_initial))

adj = parser.adj_extract("NRF2")
steady_states=[]
for i in range(0,10000):
    steady_states.append(evolve(random_inputs(adj),adj))


steady_statesli=[]

for i in steady_states:
    steady_statesli.append(list(i)) 


ssf=[[],[]]
for i in steady_statesli:
    if notli(i,ssf[0]):
        ssf[0].append(i)
        ssf[1].append(1)
    if inli(i,ssf[0]):
        k= ssf[0].index(i)
        ssf[1][k]+=1
print(ssf)


#Plotting 


frequencies=ssf[1]
steadystates_plot=[]
for i in ssf[0]:
    steadystates_plot.append("{}".format(i))
#print(steadystates_plot,frequencies)

fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(steadystates_plot, frequencies, color ='blue',
        width = 0.4)
 
plt.xlabel("steady states")
plt.ylabel("Frequencies")
plt.title("Number of simulations: 10000")
fig.autofmt_xdate()
plt.savefig("NRF2_boolean.png")
plt.show()
print("ayeaye!")

#for i in range(len(ssf[0])):
 #   print(ssf[0][i], ssf[1][i])
