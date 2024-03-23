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

def steady_check_nodes(nodes,adj):
    #if the state is not steady state it resluts in nodes which evolve and are affected
    n=len(adj)
    changed_nodes=[]
    count=0
    for i in range(0,n):
        if evolve(nodes,adj,i)[i]!= nodes[i]:
            count+=1
            changed_nodes.append(i)
            
        
    if count==0:
        return(True,changed_nodes)
    else:
        return(False,changed_nodes)




def random_inputs(adj):
    n=len(adj)
    nodes_initial= [0 for i in range(0,n)]
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

def state_node_sum(adj,state):
    n=len(adj)
    sumd=[]
    for i in range(0,n):
        sum=0
        for j in range(0,n):
            sum+=state[j]*adj[j][i]
        sumd.append(sum)
    return(sumd)


def steady_states(adj, number_of_simulations):
    steadys=[]
    n=len(adj)    
    
    for i in range(number_of_simulations):
        nodes_state=random_inputs(adj).copy()
        t=0
        timedist=[]
        timtaken=0
        while True:
            k=random.randint(0,n-1)
            
            out = evolve(nodes_state,adj,k)
            if steady_check(out,adj):
                steadys.append(out)
                timedist.append(timtaken)
                timtaken=0
                break
                
            else :
                nodes_state=out
                timtaken+=1
            
            t+=1
            if t==1000:
                break
    return(steadys)

def steady_states_time_regsig(adj, number_of_simulations):
    steadys=[]
    n=len(adj)    
    timedist=[]
    resigd=[]
    for i in range(number_of_simulations):
        nodes_state=random_inputs(adj).copy()
        t=0
        resigd.append([])
        timtaken=0
        while True:
            k=random.randint(0,n-1)
            

            out = evolve(nodes_state,adj,k)
            resigd[i].append(state_node_sum(adj,out))
            if steady_check(out,adj):
                steadys.append(out)
                timedist.append(timtaken)
                timtaken=0
                break
                
            else :
                nodes_state=out
                timtaken+=1
            
            t+=1
            if t==1000:
                break
    return(steadys,timedist,resigd,  np.mean(timedist))


def resig_sort(data,le, adj):
    n=len(adj)
    ns=len(data)
    length_dist=[]
    node_dist=[]
    ideal_length=[]

    for i in data:
        length_dist.append(len(i))

    for i in data:
        if len(i)>=le+1:
            ideal_length.append(i)
    for i in range(0,n):
        node_dist.append([])
    
    for i in ideal_length:
        for j in range(0,n):
            node_dist[j].append(i[le][j])
    return(node_dist)


def steady_states_evol(adj,number_of_simulations):
    #This function returns the evolutionary path of steady states
    steadys=[]
    state_evol=[]

    n=len(adj)    
    
    for i in range(number_of_simulations):
        state_evol.append([])

        nodes_state=random_inputs(adj).copy()
        state_evol[i].append(nodes_state)

        t=0
        timedist=[]
        timtaken=0
        while True:
            k=random.randint(0,n-1)
            
            out = evolve(nodes_state,adj,k)
            state_evol[i].append(out)
            if steady_check(out,adj):
                steadys.append(out)
                timedist.append(timtaken)
                timtaken=0
                break
                
            else :
                nodes_state=out
                timtaken+=1
            
            t+=1
            if t==1000:
                break
    return(steadys,state_evol)



def time_to_steady_states(adj, number_of_simulations):
    steadys=[]
    n=len(adj)    
    timedist=[]
    state_time=[]
    for i in range(number_of_simulations):
        nodes_state=random_inputs(adj).copy()
        t=0
      
        timtaken=0
        while True:
            k=random.randint(0,n-1)
            
            out = evolve(nodes_state,adj,k)
            if steady_check(out,adj):
                timedist.append(timtaken)
                if notli(out,steadys):
                    steadys.append(out)
                    state_time.append([])
                inde=index_np_li(out,steadys)
                state_time[inde].append(timtaken)
                timtaken=0
                break
                
            else :
                nodes_state=out
                timtaken+=1
            
            t+=1
            if t==1000:
                break
        mean_times=[]
        for i in state_time:
            mean_times.append(np.mean(i))
    return(steadys,mean_times,state_time,timedist, np.mean(timedist))

def steady_state_frequency(steadys,adj):
    
    n=len(adj)
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


def steady_check_2(steady,adj):
    n=len(adj)
    sumd=state_node_sum(adj,steady)
    counter=0
    for i in range(0,n):
        if sumd[i]*steady[i]<0:
            counter+=1
    if counter==0:
        return(True)

def steady_states_2(adj,nos):
    pass

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

def nodes_involved(nodes_input,adj):
    steadys=[]
    cnodes=[]

    n=len(adj)    
    
    
    nodes_state=nodes_input.copy()
    t=0
    while True:
        k=random.randint(0,n-1)
        
        out = evolve(nodes_state,adj,k)
        dat=steady_check_nodes(out,adj)
        if dat[0]:
            steadys.append(out)
            break
            
        else :
            nodes_state=out
            cnodes+=dat[1]
            
        t+=1
        if t==1000:
            break
    
    return(steadys,cnodes)    

def node_perturb(state,adj,pos):
    n=len(adj)
    preturb=[]

    nodes_state=state.copy()
    nodes_state[pos]=nodes_state[pos]*-1

    ss=input_steady(nodes_state,adj)
    return(ss)

def node_perturb_dist(state,adj,positions):
    outputs=[]
    for i in positions:
        outputs.append(node_perturb(state,adj,i))
    return(outputs)

    









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

def long_cycles(ssf):
    return(1000-sum(ssf[1]))

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
    for i in range(n):
        for j in range(n):
            if adj[i][j]==-1:
                neg+=1
            if adj[i][j]==1:
                pos+=1
        can.append(abs(pos-neg))
        posi.append(pos)
        nega.append(neg)
    mean=0
    for i in can:
        mean+=i
    mean=mean/n
    var=np.var(can)
    median=np.median(can)
    return(can,var,mean,median,posi,nega)

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
    plt.tight_layout()
    fig.autofmt_xdate()
    #plt.savefig("{}{}".format(image_name,".png"))
    plt.show()
    print("ayeaye!")



def bar_graph_2(ssf):
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
    plt.tight_layout()
    fig.autofmt_xdate()
    
    return(plt)



def interaction_matrix(state, adj):
    n=len(adj)
    int_mat=[]
    for i in range(0,n):
        int=[]
        for j in range(0,n):
            int.append(state[i]*adj[i][j])

        int_mat.append(int)
    return(int_mat)

def interaction_matrices(states,adj):
    int_mats=[]
    for i in states:
        int_mats.append(interaction_matrix(i,adj))
    return(int_mats)

def frustration_matrix(state,adj):
    n=len(adj)
    int_mat=[]
    for i in range(0,n):
        int=[]
        for j in range(0,n):
            int.append(state[i]*adj[i][j]*state[j])

        int_mat.append(int)
    return(int_mat)

def frustrated_matrices(states,adj):
    int_mats=[]
    for i in states:
        int_mats.append(frustration_matrix(i,adj))
    return(int_mats)



topofiles_path= glob.glob("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/landscape_of_epithelial_mesenchymal_paper/teams_data/Teams-main/TopoFiles/*topo")
topofiles=[x.split("/")[-1] for x in topofiles_path]

