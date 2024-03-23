import parse
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import csv
import random
import glob
import os
import scipy.stats as sci
import perturbations
from scipy.spatial import distance


def evolve(nodes_state,adj,pos):
    
    n=len(adj)
    adj_sum=0
    buffer=nodes_state.copy()
    for i in range(0,n):
        adj_sum+= (nodes_state[i]*adj[i][pos])
    if adj_sum>0:
        buffer[pos]=1
        
    
    elif adj_sum<0:
        buffer[pos]=-1
        
    elif adj_sum==0:
        buffer[pos]=buffer[pos]
    return(buffer)

def steady_check(nodes,adj):
    n=len(adj)
    count=0
    for i in range(0,n):
        if evolve(nodes,adj,i)[i]!= nodes[i]:
           
           count+=1
        
    if count==0:
        return(True)
    else:
        return(False)

def random_inputs(adj):
    n=len(adj)
    nodes_initial= np.zeros(n)
    for i in range(n):
        k = random.choice([-1,1])
        nodes_initial[i]=k
    return(nodes_initial)

def notli(a,b):
    counter =0
    if len(b)==0:
        return(True)
    if a is not None and len(b)!=0:
        for j in b:
            if ((j==a).all()):
                counter+=1
                
        if counter ==0:
            return(True)

def inli(a,b):
    counter =0
    if len(b)==0:
        return(False)
    elif a is not None and len(b)!=0:
        for j in b:
            if ((j==a).all()):
                counter+=1
        if counter >0:
            return(True)

def index_np_li(np_array,li):
# Returns the index of numpy array in the given list
    counter =0
    for i in li:
        if (i==np_array).all():
            break
        counter+=1
    return(counter)

def steady_states(adj, number_of_simulations):
    steadys=[]
    n=len(adj)    
    
    for i in range(number_of_simulations):
        nodes_state=random_inputs(adj).copy()
        t=0
        while True:
            k=random.randint(0,n-1)
            
            out = evolve(nodes_state,adj,k)
            if steady_check(out,adj):
                steadys.append(out)
                break
                
            else :
                nodes_state=out
            
            t+=1
            if t==1000:
                break
    return(steadys)


def steady_state_frequency(steadys,adj):
    
    n=len(adj)
    sf=[[],[]]
    stn=len(steadys)
    for i in range(0,stn):
        if notli(steadys[i],sf[0]):
            sf[0].append(steadys[i])
            sf[1].append(1)
        elif inli(steadys[i],sf[0]):
            m=index_np_li(steadys[i],sf[0])
            sf[1][m]+=1
    return(sf)

def ssf_list(ssf):
    n=len(ssf[0])
    for i in range(0,n):
        ssf[0][i]=list(ssf[0][i])
    return(ssf)
def steady_list(steady):
    n=len(steady)
    for i in range(0,n):
        steady[i]=list(steady[i])
    return(steady)

def jsd_arrange(ssf1,ssf2):
    steady_state=[]
    for i in ssf1[0]:
        steady_state.append(i)
    for j in ssf2[0]:
        if notli(j,steady_state):
            steady_state.append(j)
    freq1=[]
    freq2=[]
    for i in steady_state:
        if inli(i,ssf1[0]):
            
            k=index_np_li(i,ssf1[0])
            freq1.append(ssf1[1][k])
        else:
            freq1.append(0)
        
        if  inli(i,ssf2[0]):
            
            k2=index_np_li(i,ssf2[0])
            
            freq2.append(ssf2[1][k2])
        else:
            freq2.append(0)
    return(freq1,freq2)

def jsd(li1,li2):
    return(distance.jensenshannon(li1,li2))


topofiles_path= glob.glob("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/robustness_plasticity/programs/Gene_Network_Modelling-master/topofiles/*topo")
topofiles=[x.split("/")[-1] for x in topofiles_path]

os.chdir("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/robustness_plasticity/programs/Gene_Network_Modelling-master/topofiles")

topofiles_path_2=glob.glob("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/robustness_plasticity/programs/Gene_Network_Modelling-master/topofiles/Random_nets/*topo")

os.chdir("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/robustness_plasticity/programs/Gene_Network_Modelling-master/topofiles/Random_nets")

topofiles2=[x.split("/")[-1] for x in topofiles_path_2]

file = topofiles2[0]
print(file)
def mean_jsd(file,num):
    jsdli=[]
    adj = parse.adj_extract(file)
    stead=   steady_states(adj,1000)

    k=steady_state_frequency(stead,adj)
    
    for i in range(0,num):
        adj2=perturbations.one_edge_sign_inversion(adj)

        stead2=  steady_states(adj,1000)
        k2=steady_state_frequency(stead2,adj2)
        jsdli.append(jsd(jsd_arrange(k,k2)[0],jsd_arrange(k,k2)[1]))
        print(jsd_arrange(k,k2))
    jsdlen=len(jsdli)
    jsdsum=0
    for i in jsdli:
        jsdsum+=i
    return(jsdsum/jsdlen, jsdli)

i=topofiles2[11]
print(i)
jsdk = mean_jsd(i,100)

plt.hist(jsdk[1])
plt.savefig("pjsd_100_sims_{}_with_mean{}.jpg".format(i,jsdk[0]))
print("pjsd_100_sims_{}.jpg".format(i),jsdk[0])