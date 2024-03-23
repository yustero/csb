import pandas as pd
import numpy as np

racipe_data=[]

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

def suml(a,b):
    sum =[]
    for i in range(0,len(b)):
        sum.append(0)
    for i in range(0,len(b)):
        sum[i]=a[i]+b[i]
    return(sum)

with open("RACIPE2.0/GRHL2_solution.dat") as f:
    for i in f:
        racipe_data.append(i.split()[3:7])

with open("RACIPE2.0/GRHL2_solution_1.dat") as f:
    for i in f:
        

        racipe_data.append(i.split()[2:7])

with open("RACIPE2.0/GRHL2_solution_2.dat") as f:
    for i in f:
        racipe_data.append(i.split()[3:7])

with open("RACIPE2.0/GRHL2_solution_3.dat") as f:
    for i in f:
        
        racipe_data.append(i.split()[3:7])

#Not very general

sum=[0,0,0,0]



for i in range(0,len(racipe_data)):
    for j in range(0,4):
        racipe_data[i][j]= float(racipe_data[i][j])
for i in racipe_data:
    sum =suml(sum,i)
    
n=len(racipe_data)
n2=len(racipe_data[1])


mean= [x/ n for x in sum]

steady_states_racipe_bool=[]


for i in range(len(racipe_data)):
    steady_states_racipe_bool.append(np.zeros(n2))
    for j in range(n2):
        if racipe_data[i][j]-mean[j]>0:
            steady_states_racipe_bool[i][j]=1
        if racipe_data[i][j]-mean[j]<0:
            steady_states_racipe_bool[i][j]=-1


def steady_state_counter(steady_states):
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
    return(ssf)

print(steady_state_counter(steady_states_racipe_bool))