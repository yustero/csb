import numpy as np
import random
import matplotlib.pyplot as plt
import coherent_parser
import glob
import boolean_sim
import randomization
import node_metrics
import topopath


'''
The goal is to turn off nodes selectively and increase the number of nodes turned off in each step
'''


def evolve(nodes_state,adj,pos, hybn):
    
    n=len(adj)
    adj_sum=0
    buffer=nodes_state.copy()
    if pos not in hybn:
        for i in range(0,n):
            adj_sum+= (nodes_state[i]*adj[i][pos])
        if adj_sum>0:
            buffer[pos]=1
            
        
        elif adj_sum<0:
            buffer[pos]=-1
            
        elif adj_sum==0:
            buffer[pos]= buffer[pos]
        return(buffer)
    
    if pos in hybn:
        for i in range(0,n):
            adj_sum+= (nodes_state[i]*adj[i][pos])
        if adj_sum>0:
            buffer[pos]=1
            
        
        elif adj_sum<0:
            buffer[pos]=-1
            
        elif adj_sum==0:
            buffer[pos]=0
        return(buffer)

def steady_check(nodes,adj,hybn):
    n=len(adj)
    count=0
    for i in range(0,n):
        if evolve(nodes,adj,i,hybn)[i]!= nodes[i]:
           
           count+=1
        
    if count==0:
        return(True)
    else:
        return(False)

def random_inputs(adj):
    n=len(adj)
    nodes_initial= np.zeros(n)
    for i in range(n):
        k = random.choice([-1,0,1])
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

def steady_states(adj, number_of_simulations,hybn):
    steadys=[]
    
    n=len(adj)    
    
    for i in range(number_of_simulations):
        nodes_state=random_inputs(adj).copy()
        t=0
        timedist=[]
        timtaken=0
        while True:
            k=random.randint(0,n-1)
            
            out = evolve(nodes_state,adj,k,hybn)
            if steady_check(out,adj,hybn):
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


def hamming(a,b):
    n=len(a)
    ham=0
    for i in range(0,n):
        if a[i]!=b[i]:
            ham+=1
    return(ham)      

def steady_states_non_random(adj, initial_conditions):
    steadys=[]
    ni=len(initial_conditions)
    n=len(adj)    
    ham_dist=[ [] for i in range(0,ni)]

    for i in range(len(initial_conditions)):
        nodes_state=initial_conditions[i].copy()
        buff=nodes_state.copy()
        t=0
        timedist=[]
        timtaken=0
        while True:
            k=random.randint(0,n-1)
            
            out = evolve(nodes_state,adj,k)
            ham_dist[i].append(hamming( buff,out))
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
    return(steadys,ham_dist)

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




def steady_states_time(adj, number_of_simulations):
    steadys=[]
    n=len(adj)    
    timedist=[]
    for i in range(number_of_simulations):
        nodes_state=random_inputs(adj).copy()
        t=0
      
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
    return(steadys,timedist)

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

def bar_graph2(ssf, image_name, node):
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
    plt.ylabel("Frequency")
    plt.title("{} rmnode simulated via three state".format(node))
    fig.autofmt_xdate()
    plt.savefig("{}{}".format(image_name,".png"))
    #plt.show()
    print("ayeaye!")

def one_node_on(n,k):
    input=[0 for i in range(0,n)]
    input[k]=1
    return(input)

'''print(topopath.topofiles)

topo= topopath.topofiles[9]

data=coherent_parser.clustered_matrix_file(topo)

adj=data[0]
t1=len(data[1])
t2=len(data[2])
nodes=data[-1]
print(nodes)


n=len(adj)
numofsteady=[]
numnodeoff=[]

for i in range(0,n):
    nli=[x for x in range(0,n)]
    nodes_index=random.sample(nli,i)
    print(nodes_index)
    
    steadys=steady_states(adj,100,nodes_index)
    ssf=steady_state_frequency(steadys,adj)
    numofsteady.append(len(ssf[0]))
    numnodeoff.append(i)

plt.scatter(numnodeoff,numofsteady)
plt.title("{}_dyturnoff_vs_number_of_nodes".format(topo))


import os 

os.chdir("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/three_state/files/plots/selective_turnoff_dy")
plt.savefig("{}.png".format(topo))'''