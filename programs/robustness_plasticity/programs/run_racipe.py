import glob
import os
import subprocess
import pandas as pd
import numpy as np
import scipy.stats as sci
import matplotlib.pyplot as plt


os.chdir("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/robustness_plasticity/programs/RACIPE2.0")

dir="/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/robustness_plasticity/programs/RACIPE2.0"


topofiles=[]
for i in glob.glob("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/robustness_plasticity/programs/RACIPE2.0/*.topo"):
    topofiles.append(i.split("/")[-1])

def count_solutions(topofile):
    no_sol=0
    solf=[]
    for i in glob.glob(dir+"/*.dat"):
        file=(i.split("/")[-1])
        if file.split("_")[0]==topofile:
          if file not in solf:
            solf.append(file)
    solf.remove("{}_solution.dat".format(topofile))
    solf.remove("{}_parameters.dat".format(topofile))
    solf.remove("{}_T_test.dat".format(topofile))
    n=len(solf)

    print(solf)
    for i in range(0,n):
        
        if solf[i].split("_")[2].split(".")[0].isnumeric():
            no_sol+=1
    return(no_sol)

def list_of_solutions(topofile):

    solf=[]
    for i in glob.glob(dir+"/*.dat"):
        file=(i.split("/")[-1])
        if file.split("_")[0]==topofile:
          if file not in solf:
            solf.append(file)
    solf.remove("{}_solution.dat".format(topofile))
    solf.remove("{}_parameters.dat".format(topofile))
    solf.remove("{}_T_test.dat".format(topofile))
    n=len(solf)

    return(solf)

print(topofiles)

def number_of_nodes(topofile):
   data=pd.read_csv("{}.ids".format(topofile))
   
   return(len(data.values)) 

def unified_table_of_solutions(topofile):
    nsol=count_solutions(topofile)
    n=number_of_nodes(topofile)
    

def tabled_data(topofile):
    n=number_of_nodes(topofile)
    tabled=[]
    solf=list_of_solutions(topofile)
    for i in range(1,n+1):
        if "{}_solution_{}.dat".format(topofile,i) in solf:
            data=pd.read_csv("{}_solution_{}.dat".format(topofile,i), sep="\t", header=None)
            datali=data.values
            no_li=len(datali)
            for j in range(0,no_li):
                for k in range(0,i):
                    tabled.append(datali[j][(n*k+2):(n*(k+1)+2)])
                    #print(datali[j][(n*k+2):(n*(k+1)+2)],"{}_solution_{}.dat".format(topofile,i), "row{}".format(j), "range: {}:{}".format((n*k+3),(n*(k+1)+3)) )
    return(tabled)

def tabled_data_breakdown(topofile):
    n=count_solutions(topofile)
    tabled=[]
    solf=list_of_solutions(topofile)
    for i in range(1,n+1):
        if "{}_solution_{}.dat".format(topofile,i) in solf:
            data=pd.read_csv("{}_solution_{}.dat".format(topofile,i), sep="\t", header=None)
            sol=[]
            datali=data.values
            no_li=len(datali)
            for j in range(0,no_li):
                for k in range(0,i):
                    sol.append(datali[j][(n*k+2):(n*(k+1)+2)])
                    #print(datali[j][(n*k+2):(n*(k+1)+2)],"{}_solution_{}.dat".format(topofile,i), "row{}".format(j), "range: {}:{}".format((n*k+3),(n*(k+1)+3)) )
            tabled.append(sol)
    return(tabled)


def node_list(topofile):
    data=pd.read_csv("{}.prs".format(topofile), sep="\t")
    n=number_of_nodes(topofile) 
    nodes=[]
    print(data)
    for i in range(0,n):
        nodename=data.iloc[i][0].split("_")[2]
        nodes.append(nodename)
    return(nodes)



def adj_extract(topofile):

    topo_data=pd.read_csv("{}.topo".format(topofile), sep =" ")
    topo_ids=node_list(topofile)
    
    def ind(i):
        return(topo_ids.index(i))

    n=len(topo_ids)

    adj=[]
    for i in range(n):
        adj.append(np.zeros(n))

    
    for i in topo_data.values:
        
        if i[2]==1:
            adj[ind(i[0])][ind(i[1])] = 1
        if i[2]==2:
            adj[ind(i[0])][ind(i[1])]= -1
    return(adj)

def bool_convert(state,mean):
    n=len(mean)
    
    bool_state=[]
    for i in range(0,n):

        if state[i]-mean[i]>=0:
            
            bool_state.append(1)
        if state[i]-mean[i]<0:
            
            bool_state.append(-1)
    return(bool_state)

def discretization(data):
    n=len(data[0])
    nd=len(data)
    sum=np.zeros(n)
    for i in data:
        sum=np.add(sum,i)
    mean =[x/nd for x in sum]
    bool_states=[]
    for i in data:
        bools=bool_convert(i,mean)
        bool_states.append(bools)
    return(bool_states)

def ssf_calc(steadys):
    if len(steadys)!=0:    
        n=len(steadys[0])
        sf=[[],[]]
        stn=len(steadys)
        for i in range(0,stn):
            if steadys[i] not in sf[0]:
                sf[0].append(steadys[i])
                sf[1].append(1)
            elif steadys[i] in sf[0]:
                m=sf[0].index(steadys[i])
                sf[1][m]+=1
        return(sf)
    elif len(steadys)==0:
        return([[],[]])

def biomdality(ssf):

    n=len(ssf[1])
    if n!=2 and n!=3:
        k=sci.stats.kurtosis(ssf[1])
        s=sci.stats.kurtosis(ssf[1])
        denom= 3*(((n-1)**2)/((n-2)*(n-3)))+k
        numer=(s**2)+1

        return(denom/numer)
    else:
        raise Exception("The number of steady states can't be 2 or 3")

def plasticity(topofile):
    sing=
#Why do some nodes have a basal production rate? what does discretization mean really and what does the basal production rate tell us about the topological connections of the node?

#print(number_of_nodes("abspa"))
#print(tabled_data("abspa"))

##data=tabled_data("")

#k2=ssf_calc(discretization(data))
#frequencies=k2[1]
#steadystates_plot=[]
#for i in k2[0]:
#    steadystates_plot.append("{}".format(i))
#print(steadystates_plot,frequencies)

#fig = plt.figure(figsize = (10, 5))
 

# creating the bar plot
#plt.bar(steadystates_plot, frequencies, color ='blue',
#        width = 0.4)
#plt.show()





'''dat=tabled_data_breakdown("yeast")

#n=len(dat)
#for i in range(0,n):
    k = ssf_calc(discretization(dat[i]))
    print(biomdality(k))

#print(count_solutions("NRF2"))'''