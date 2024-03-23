import numpy as np
import random as rn
def network(teamsize1,teamsize2,spar11,spar22,spar12,spar21):
    netsize=teamsize1+teamsize2
    net=np.zeros((netsize,netsize))
    t1=[]
    t2=[]
    
    for i in range(netsize):
        if len(t1)<teamsize1:
            t1.append(i)
        else:
            t2.append(i)
            
    a,b,c,d=0,0,0,0
    while a < int((teamsize1**2)*spar11):
        source=rn.choice(t1)
        target=rn.choice(t1)
        if net[source][target]==0:
            net[source][target]=1
            a+=1
    
    while b < int((teamsize2**2)*spar22):
        source=rn.choice(t2)
        target=rn.choice(t2)
        if net[source][target]==0:
            net[source][target]=1
            b+=1
    
    while c < int((teamsize1*teamsize2)*spar12):
        source=rn.choice(t1)
        target=rn.choice(t2)
        if net[source][target]==0:
            net[source][target]=-1
            c+=1
    
    while d < int((teamsize1*teamsize2)*spar21):
        source=rn.choice(t2)
        target=rn.choice(t1)
        if net[source][target]==0:
            net[source][target]=-1
            d+=1
    
    return net, t1, t2

def peripheral(mat):
    per=0
    for i in range(len(mat)):
        checkin=0
        checkout=0
        for j in range(len(mat)):
            if mat[i][j]!=0:
                checkout+=1
                
            elif mat[j][i]!=0:
                checkin+=1
                
        if checkin==0 or checkout==0:
            per+=1
    return per

def actedges(t1,t2,mat):
    edges=0
    for i in t1:
        for j in t2:
            if mat[i][j]==1:
                edges+=1
    return edges

def inhibedges(t1,t2,mat):
    edges=0
    for i in t1:
        for j in t2:
            if mat[i][j]==-1:
                edges+=1
    return edges

def sameteam(i,j,t):
    if i in t and j in t:
        return True
    else:
        return False

def rectify(t1,t2,mat):
    rectmat=mat.copy()
    for i in range(len(mat)):
        for j in range(len(mat)):
            if sameteam(i,j,t1) or sameteam(i,j,t2):
                if mat[i][j]==-1:
                    rectmat[i][j]=1 
            else:
                if mat[i][j]==1 :
                    rectmat[i][j]=-1
    return rectmat

def complete(t1,t2,mat):
    compmat=mat.copy()
    for i in range(len(mat)):
        for j in range(len(mat)):
            if sameteam(i,j,t1) or sameteam(i,j,t2):
                if mat[i][j]!=1:
                    compmat[i][j]=1 
            else:
                if mat[i][j]!=-1 :
                    compmat[i][j]=-1
    return compmat

def edges(mat):
    edg=0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]!=0:
                edg+=1
    return edg

def sym():
    mat=np.zeros((14,14))
    t1=[]
    t2=[]
    for i in range(len(mat)):
        if i%2==0:
            t2.append(i)
        else:
            t1.append(i)
    for i in t1:
        mat[i][(i+2)%14]=1
        mat[(i+2)%14][i]=1
        mat[i][(i+1)%14]=-1
        mat[(i+1)%14][i]=-1

    for i in t2:
        mat[i][(i+2)%14]=1
        mat[(i+2)%14][i]=1
        mat[i][(i+1)%14]=-1
        mat[(i+1)%14][i]=-1
        
    return mat
#net=network(8,8,1,1,1,1)
#print(net[0].tolist(), net[1], net[2])

