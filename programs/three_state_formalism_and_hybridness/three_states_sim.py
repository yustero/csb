import numpy as np
import random
import matplotlib.pyplot as plt
import coherent_parser
import glob
import boolean_sim
import randomization
import node_metrics

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
        buffer[pos]=0
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
    plt.ylabel("Frequency")
    plt.title("Number of simulations: 100000")
    fig.autofmt_xdate()
    #plt.savefig("{}{}".format(image_name,".png"))
    plt.show()
    print("ayeaye!")

def one_node_on(n,k):
    input=[0 for i in range(0,n)]
    input[k]=1
    return(input)

path1="/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/three_state/files/topofiles"
filedat=glob.glob(path1+"/*topo")
topofiles=[x.split("/")[-1] for x in filedat]
print(topofiles)