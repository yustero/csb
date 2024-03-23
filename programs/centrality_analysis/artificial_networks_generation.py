import random
import coherenet_parser
import artificial
import node_metrics
import randomization
import matplotlib.pyplot as plt
import glob
import boolean_sim
import numpy as np
import hybrid_states
path1="/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/centrality_analysis/topofiles"
filedat=glob.glob(path1+"/*topo")
topofiles=[x.split("/")[-1] for x in filedat]

def team_gen(t1n,t2n,t1e,t2e, t1t2e, t2t1e):
    if t1e>t1n**2 or t2e> t2n**2 or t1t2e> t1n*t2n or t2t1e> t1n*t2n:
        raise ValueError("Lots of edges")
    n=t1n+t2n
    adj=[]
    edge=[0 for i in range(0,n)]
    for i in range(0,n):
        adj.append(edge.copy())
    
    for i in range(0,t1n):
        k=random.randint(0,t1n-1)
        adj[k][i]=1
    for i in range(t1n,n):
        k=random.randint(t1n,n-1)
        adj[k][i]=1
    for i in range(t1n,n):
        k=random.randint(0,t2n-1)
        adj[k][i]=-1
    for i in range(t2n,n):
        k=random.randint(0,t1n-1)
        adj[k][i]=-1

    t1re=t1e-t1n
    t2re=t2e-t2n
    t1t2re=t1t2e-t1n
    t2t1re=t2t1e-t2n 

    while t1re>0:
        a=random.randint(0,t1n-1)
        b=random.randint(0,t1n-1)
        if adj[a][b]==0:
            adj[a][b]=1
            t1re=t1re-1
            
    
    while t2re>0:
        a=random.randint(t1n,n-1)
        b=random.randint(t1n,n-1)
        if adj[a][b]==0:
            adj[a][b]=1
            t2re=t2re-1
            
    while t1t2re>0:
        a=random.randint(0,t1n-1)
        b=random.randint(t1n,n-1)
        if adj[a][b]==0:
            adj[a][b]=-1
            t1t2re=t1t2re-1
            
    while t2t1re>0:
        a=random.randint(t1n,n-1)
        b=random.randint(0,t1n-1)
        if adj[a][b]==0:
            adj[a][b]=-1
            t2t1re=t2t1re-1
            
    return(adj,t1n,t2n)

def node_density_inh(adj,k):
    inh=0
    n=len(adj)
    for i in range(0,n):
        if adj[i][k]==-1:
            inh+=1
    return(inh)


def team_structure():
    pass






def team_gen_node(t1n,t2n,t1e,t2e, t1t2e, t2t1e, n1,n2):
    if t1e>t1n**2 or t2e> t2n**2 or t1t2e> t1n*t2n or t2t1e> t1n*t2n:
        raise ValueError("Lots of edges")
    n=t1n+t2n
    adj=[]
    edge=[0 for i in range(0,n)]
    for i in range(0,n):
        adj.append(edge.copy())
    
    for i in range(0,t1n):
        k=random.randint(0,t1n-1)
        adj[k][i]=1
    for i in range(t1n,n):
        k=random.randint(t1n,n-1)
        adj[k][i]=1

    t1re=t1e-t1n
    t2re=t2e-t2n 

    while t1re>0:
        a=random.randint(0,t1n-1)
        b=random.randint(0,t1n-1)
        if adj[a][b]==0:
            adj[a][b]=1
            t1re=t1re-1
            
    
    while t2re>0:
        a=random.randint(t1n,n-1)
        b=random.randint(t1n,n-1)
        if adj[a][b]==0:
            adj[a][b]=1
            t2re=t2re-1
    
    non1=int(t2t1e/n1)
    r1=t2t1e-non1*n1

    non2=int(t1t2e/n2)
    r2=t1t2e-non2*n2

    in1t1=r1+non1
    in2t2=r2+non2


    k=random.randint(0,t1n-1)

    while in1t1>0:
        a=random.randint(t1n,n-1)
        if adj[a][k]==0:
            adj[a][k]=-1
            in1t1=in1t1-1
            
    for i in range(0,n1-1):
        count=non1
        while True:
            a=random.randint(0,t1n-1)
            if node_density_inh(adj,a)==0:
                break
        while count>0:
            b=random.randint(t1n,n-1)
            if adj[b][a]==0:
                adj[b][a]=-1
                count=count-1

    k=random.randint(t1n,n-1)

    while in2t2>0:
        a=random.randint(0,t1n-1)
        if adj[a][k]==0:
            adj[a][k]=-1
            in2t2=in2t2-1
    
    for i in range(0,n2-1):
        count=non2
        while True:
            a=random.randint(t1n,n-1)
            if node_density_inh(adj,a)==0:
                break
        while count>0:
            b=random.randint(0,t1n-1)
            if adj[b][a]==0:
                adj[b][a]=-1
                count=count-1

    return(adj,t1n,t2n, non1,non2)
'''dist=[]
ts=[]
hybfq=[]
z=1
for i in range(z,3):
    dist.append([])
    ts.append([])
    hybfq.append([])
    for j in range(0,10):
        dat=team_gen_node(2,2,4,4,2,2,i,i)
        adj=dat[0]
        t1=dat[1]
        t2=dat[2]
        
        print(adj,i)
        ts1=coherenet_parser.team_strength_file(adj)
        print(ts1)
        steadys=boolean_sim.steady_states(adj,1000)
        ssf=boolean_sim.steady_state_frequency(steadys,adj)
        hybrid=hybrid_states.opt_hybrid_states(ssf,adj,t1,t2)
        freq=hybrid_states.opt_freq_cumulative(ssf,hybrid[0])

        
        
        dist[i-z].append(len(ssf[1]))
        ts[i-z].append(ts1)
        hybfq[i-z].append(freq)
n=len(dist)
for i in range(0,n):
    print(np.mean(dist[i]), np.mean(ts[i]),np.mean(hybfq[i]))'''