import numpy as np

def adj_summary(adj):
    nodes=len(adj)
    n=nodes
    edges=0
    pedges=0
    nedges=0
    for i in range(0,n):
        for j in range(0,n):
            if adj[i][j]==1:
                pedges+=1
                edges+=1
            if adj[i][j]==-1:
                nedges+=1
                edges+=1
    return(nodes,edges,pedges,nedges)

def indegree(adj):
    n=len(adj)
    indeg=[]
    for i in range(0,n):
        count=0
        for j in range(0,n):
            if adj[j][i]==1 or adj[j][i]==-1:
                count+=1
        indeg.append(count)
    return(indeg)

def outdegree(adj):
    n=len(adj)
    outdeg=[]
    for i in range(0,n):
        count=0
        for j in range(0,n):
            if adj[i][j]==1 or adj[i][j]==-1:
                count+=1
        outdeg.append(count)
    return(outdeg)

def indeg_summary(adj):
    n=len(adj)
    indeg=[]
    posd=[]
    negd=[]
    can=[]
    for i in range(0,n):
        count=0
        pos=0
        neg=0
        for j in range(0,n):
            if adj[j][i]==1 or adj[j][i]==-1:
                count+=1
            if adj[j][i]==1:
                pos+=1
            if adj[j][i]==-1:
                neg+=1
        posd.append(pos)
        negd.append(neg)
        can.append(abs(pos-neg))
        
        indeg.append(count)
    return(can,posd,negd,indeg, np.mean(can))


def outdeg_summary(adj):
    n=len(adj)
    outdeg=[]
    posd=[]
    negd=[]
    can=[]
    for i in range(0,n):
        count=0
        pos=0
        neg=0
        for j in range(0,n):
            if adj[i][j]==1 or adj[i][j]==-1:
                count+=1
            if adj[i][j]==1:
                pos+=1
            if adj[i][j]==-1:
                neg+=1
        posd.append(pos)
        negd.append(neg)
        can.append(abs(pos-neg))
        
        outdeg.append(count)
    return(can,posd,negd,outdeg, np.mean(can))