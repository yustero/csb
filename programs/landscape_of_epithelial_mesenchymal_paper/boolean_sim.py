import Parser
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import csv
import random
import glob
import scipy.stats as sci
import networkx as nx


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


def summary(ssf,file,no_of_steady_states,n):
    
    output_data=open("data/{}{}".format(file.split(".")[0] , ".csv"),"w", newline="")
    
    wri=csv.writer(output_data)
    b=len(ssf[1])
    print(file)
    print("number of steadystates = {}".format(b), "number of nodes = {}".format(n))
    wri.writerow(["steady_state", "frequency"])
    for i in range(0,no_of_steady_states):
        
        wri.writerow([ssf[0][i], ssf[1]])
    output_data.close()



def write_ssf(topofiles):
    for i in topofiles:
        
        file=i
        adj=Parser.adj_extract(file)
        stead= steady_states(adj,1000)

        ssf=steady_state_frequency(stead,adj)
        n=len(adj)
        print(n)
        no_of_steady_states=len(ssf[1])
        summary(ssf,file,no_of_steady_states,n)

def steps_to_steady_state(adj, number_of_simulations):
    stead_speed=[]
    n=len(adj)    
    
    for i in range(number_of_simulations):
        speed=0
        nodes_state=random_inputs(adj).copy()
        t=0
        while True:
            speed+=1
            k=random.randint(0,n-1)
            
            out = evolve(nodes_state,adj,k)
            if steady_check(out,adj):
                stead_speed.append([out, speed])
                break
                
            else :
                nodes_state=out
            
            t+=1 
            if t==1000:
                break
    return(stead_speed)



def input_steady(nodes_input,adj):
    steadys=[]
    n=len(adj)    
    
    
    nodes_state=nodes_input.copy()
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
def coherence(ssf,adj):
    n=len(adj)
    ssfc=ssf.copy()
    coherence_list=[]
    for i in ssf[0]:
        coher=0
        for j in range(0,n):

            perturb= i.copy()
            if i[j]==1:
                perturb[j]=-1
            if i[j]==-1:
                perturb[j]==1
            outs=input_steady(perturb,adj)
            if outs is not None:
                if (outs==i).all():
                    coher+=1
        coherence_list.append(coher)
    coherence_sf=[x/n for x in coherence_list]
    return(coherence_sf)
def coherence_iterations(ssf,adj,num):
    l=list(np.zeros(len(ssf[1])))
    for i in range(0,num):
        l=[l[j]+ coherence(ssf,adj)[j] for j in range(0,len(ssf[1]))]
    final_coherence=[x/num for x in l]
    return(final_coherence)

def frustration(steady,adj):
    n=len(adj)
    frustration=0
    for i in range(0,n):
        for j in range(0,n):
            if adj[i][j]* steady[i]*steady[j]<0:
                frustration+=1
    return(frustration)

def biomdality(ssf,adj):

    n=len(ssf[1])
    if n!=2 and n!=3:
        k=sci.stats.kurtosis(ssf[1])
        s=sci.stats.kurtosis(ssf[1])
        denom= 3*(((n-1)**2)/((n-2)*(n-3)))+k
        numer=(s**2)+1

        return(denom/numer)
    else:
        return(0)


def canal_node(adj):
    n=len(adj)
    can=[]
    neg=0
    pos=0
    for i in range(n):
        for j in range(n):
            if adj[i][j]==-1:
                neg+=1
            if adj[i][j]==1:
                pos+=1

        can.append(abs(pos-neg))
        pos=0
        neg=0
    mean=0
    for i in can:
        mean+=i
    mean=mean/n
    return(mean)
def canal_node_summary(adj):
    n=len(adj)
    can=[]
    posi=[]
    nega=[]
    neg=0
    pos=0
    posneg=[]
    for i in range(n):
        for j in range(n):
            if adj[i][j]==-1:
                neg+=1
            if adj[i][j]==1:
                pos+=1
        can.append(abs(pos-neg))
        posi.append(pos)
        nega.append(neg)
        posneg.append([pos,neg])
        pos=0
        neg=0
    mean=0
    for i in can:
        mean+=i
    mean=mean/n
    var=np.var(can)
    median=np.median(can)
    return(can,var,mean,median,posneg)

def outgoing_node(adj):
    n=len(adj)
    can=[]
    posi=[]
    nega=[]
    posneg=[]    
    neg=0
    pos=0
    for i in range(n):
        for j in range(n):
            if adj[i][j]==-1:
                neg+=1
            if adj[j][i]==1:
                pos+=1
        can.append(abs(pos-neg))
        posi.append(pos)
        nega.append(neg)
        posneg.append([pos,neg])
        pos=0
        neg=0
    mean=0
    for i in can:
        mean+=i
    mean=mean/n
    var=np.var(can)
    median=np.median(can)
    return(can,var,mean,median,posneg)

def pfl_nfl_calc(adj):
    adj=np.matrix(adj)
    graph=nx.from_numpy_array(adj)
    cycles=nx.simple_cycles(graph)
    pos=0
    neg=0
    cyc =[x for x in cycles]
    print(len(cyc))
    for i in cycles:
        sum=1
        cycle_length=len(i)
        print(cycle_length)    
        for j in range(0,cycle_length):
            if j<cycle_length-1:
                sum*= graph.edges[i[j],i[j+1]]["weight"]
                print(sum)
            elif j==cycle_length-1:
                sum*= graph.edges[i[j], i[0]]["weight"]
                print(sum)
        if sum>0:
            pos+=1/cycle_length
        elif sum<0:
            neg+=1/cycle_length
    #print(pos,neg)
    return(pos,neg)


def bar_graph(ssf, image_name):
    frequencies=ssf[1]
    steadystates_plot=[]
    for i in ssf[0]:
        steadystates_plot.append("{}".format(i))
    print(steadystates_plot,frequencies)

    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(steadystates_plot, frequencies, color ='blue',
            width = 0.4)
    
    plt.xlabel("steady states")
    plt.ylabel("Frequencies")
    plt.title("Number of simulations: 1000")
    fig.autofmt_xdate()
    #plt.savefig("{}{}".format(image_name,".png"))
    plt.show()
    print("ayeaye!")

topofiles_path= glob.glob("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/landscape_of_epithelial_mesenchymal_paper/teams_data/Teams-main/TopoFiles/*topo")
topofiles=[x.split("/")[-1] for x in topofiles_path]


adj=Parser.adj_extract(topofiles[2])

#print(steps_to_steady_state(adj,1000))

#print(input_steady(np.array([ 1., -1.,  -1., -1., -1., -1.,  1.,  1.]),adj))

#steady_st=steady_states(adj,1000)
#ssf=steady_state_frequency(steady_st,adj)
#print(coherence(ssf,adj))




'''
topofiles_path= glob.glob("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/landscape_of_epithelial_mesenchymal_paper/teams_data/Teams-main/TopoFiles/*topo")
topofiles=[x.split("/")[-1] for x in topofiles_path]
adj=Parser.adj_extract(topofiles[2])
print(topofiles[2])
stead=steady_states(adj,10000)
print(len(stead))
print(steady_state_frequency( stead ,adj))
'''