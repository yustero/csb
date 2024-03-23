import random 
import numpy as np 
import matplotlib.pyplot as plt
import glob
import coherenet_parser


def evolve(node_state,adj,pos):
    n=len(adj)
    adj_sum=0
    buffer=node_state.copy()
    
    for i in range(0,n):
        adj_sum+=node_state[i]*adj[i][pos]
    
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
        if evolve(nodes,adj,i)[i]!=nodes[i]:
            count+=1
        
    if count==0:
        return(True)
    
    else:
        return(False)


def random_inputs(adj):
    n=len(adj)
    nodes_initial=[0 for i in range(0,n)].copy()
    for i in range(0,n):
        k=random.choice([1,0,-1])
        nodes_initial[i]=k
    return(nodes_initial)

def notli(a,b):
    counter =0
    if len(b)==0:
        return(True)
    if a is not None and len(b)!=0:
        for j in b:
            if (j==a):
                counter+=1
                
        if counter ==0:
            return(True)
def inli(a,b):
    counter =0
    if len(b)==0:
        return(False)
    elif a is not None and len(b)!=0:
        for j in b:
            if (j==a):
                counter+=1
        if counter >0:
            return(True)

def index_np_li(np_array,li):
# Returns the index of numpy array in the given list
    counter =0
    for i in li:
        if (i==np_array):
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
            steadys.append(None)
            break
    return(steadys)    


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
    return(steadys,timedist, np.mean(timedist))

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


