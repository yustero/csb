import boolean_siml
import hybrid_states
import input_space_map
import node_metrics
import numpy as np 
import matplotlib.pyplot as plt
import coherent_parser
import topopath
import os
import csv
import boolean_sim
import glob
import copy
import pandas as pd
from sklearn import linear_model
import random

def indegree(adj):
    indist=[]
    n=len(adj)
    for i in range(0,n):
        ind=0
        for j in range(0,n):
            if adj[j][i]!=0:
                ind+=1
        indist.append(ind)
    return(indist)

def outdegree(adj):
    n=len(adj)
    outdist=[]
    for i in range(0,n):
        out=0
        for j in range(0,n):
            if adj[i][j]!=0:
                out+=1
        outdist.append(out)
    return(outdist)

def incan_dist(adj):
    n=len(adj)
    incand=[]
    pos_neg=[]

    for i in range(0,n):
        pos=0
        neg=0
        for j in range(0,n):
            if adj[j][i]==-1:
                neg+=1
            if adj[j][i]==1:
                pos+=1
        incand.append(pos-neg)
        pos_neg.append([pos, neg])
    absincand=[]
    for i in incand:
        absincand.append(abs(i))

    return(incand,pos_neg,absincand)


def outcan_dist(adj):
    n=len(adj)
    outcand=[]
    pos_neg=[]

    for i in range(0,n):
        pos=0
        neg=0
        for j in range(0,n):
            if adj[i][j]==-1:
                neg+=1
            if adj[i][j]==1:
                pos+=1
        outcand.append(pos-neg)
        pos_neg.append([pos, neg])
    absoutcand=[]
    for i in outcand:
        absoutcand.append(abs(i))

    return(outcand,pos_neg,absoutcand)

def opt_hybrid_states(ssf,adj,nt1,nt2):
    n=len(adj)
    nt1
    nt2
    hybrid_states=[]

    def genl(a,n):
        l=[a for i in range(0,n)]
        return(l)


    opt1= genl(1,nt1)+genl(-1,nt2)
    opt2=genl(-1,nt1)+genl(1,nt2)
    opt_states=[opt1,opt2]

    for i in ssf[0]:
        if not (((i[0:nt1]== genl(1,nt1)).all() and (i[nt1:] == genl(-1,nt2)).all()) or ((i[0:nt1]== genl(-1,nt1)).all() and (i[nt1:] == genl(1,nt2)).all())):
            hybrid_states.append(i)
    return(opt_states,hybrid_states)

def opt_hybrid_statesl(ssf,adj,nt1,nt2):
    #the above function but works with lists
    n=len(adj)
    nt1
    nt2
    hybrid_states=[]

    def genl(a,n):
        l=[a for i in range(0,n)]
        return(l)


    opt1= genl(1,nt1)+genl(-1,nt2)
    opt2=genl(-1,nt1)+genl(1,nt2)
    opt_states=[opt1,opt2]

    for i in ssf[0]:
        if not ((i[0:nt1]== genl(1,nt1) and i[nt1:] == genl(-1,nt2)) or (i[0:nt1]== genl(-1,nt1) and i[nt1:] == genl(1,nt2))):
            hybrid_states.append(i)
    return(opt_states,hybrid_states)


def index_np_li(np_array,li):
# Returns the index of numpy array in the given list
    counter =0
    for i in li:
        if (i==np_array).all():
            break
        counter+=1
    return(counter)

def hybrid_freq_cumulative(ssf, hybrids,opt):
    n=len(ssf[1])
    opt_index=[]
    for i in opt:
        opt_index.append(index_np_li(i,ssf[0]))
    freq=0
    for i in range(0,n):
        if i not in opt_index:
            freq+=ssf[1][i]
    return(freq)
    
def hybrid_freq_cumulative_l(ssf,hybrids,opt):
    n=len(ssf[1])
    opt_index=[]
    for i in opt:
        opt_index.append(ssf[0].index(i))
    freq=0
    for i in range(0,n):
        if i not in opt_index:
            freq+=ssf[1][i]
    return(freq)

def hammd(opt,hyb):
    n=len(opt)
    d=0

    for i in range(0,n):
        if hyb[i]!=opt[i]:
            d+=1
    return(d)
def hamming_dist(opt_states,hybrid_states):
    n=len(hybrid_states)
    hamd=[]
    for i in range(0,n):
        hamd.append(min(hammd(opt_states[0],hybrid_states[i]),hammd(opt_states[1],hybrid_states[i])))
    return(hamd)


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
    
def new_hybrid(nindex,wt_hybrids,rhybrids):
    wihybrids=copy.deepcopy(wt_hybrids)
    new_hybrids=[]
    witrhybrids=[]
    for i in wihybrids:
       witrhybrids.append( np.delete(i,nindex))
    
    for i in rhybrids:
        if notli(i,witrhybrids):
            new_hybrids.append(i)
    return(new_hybrids)

def node_on(adj,onn, number_of_simulations):
    steadys=[]
    n=len(adj)    
    
    for i in range(number_of_simulations):
        nodes_state=boolean_sim.random_inputs(adj).copy()
        nodes_state[onn]=1
        t=0
        out=nodes_state.copy()
        timedist=[]
        timtaken=0
        while True:
            k=random.randint(0,n-1)
            if k!=onn:
                out = boolean_sim.evolve(nodes_state,adj,k)
            
            if boolean_sim.steady_check(out,adj):
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





def node_knockout(adj,nodelist,nindex,file,avg_incan):
    n=len(adj)
    node=nodelist[nindex]
    nodes=nodelist.copy()
    print(node)
    

    dat=coherent_parser.clustered_matrix_file(file)
    te1= dat[1]
    te2=dat[2]
    
    #wt hybrids
    wtadj=dat[0]
    wsteayds=boolean_siml.steady_states(wtadj,1000)
    wtssf=boolean_siml.steady_state_frequency(wsteayds,wtadj)
    wthybrids=opt_hybrid_statesl(wtssf,wtadj,len(te1),len(te2))[1]





    t1=te1.copy()
    t2=te2.copy()


    indeg=indegree(adj)[nindex]
    outdeg=outdegree(adj)[nindex]


    if node in t1:
        t1.remove(node)
    if node in t2:
        t2.remove(node)
    
    nodes.remove(nodelist[nindex])
    
    uadj=coherent_parser.adj_nodes(file,nodes)[0]
    steadys=boolean_siml.steady_states(uadj,1000)
    ssf=boolean_siml.steady_state_frequency(steadys,uadj)
    graph=boolean_siml.bar_graph_2(ssf)
    graph.title("{}_{}_{}_{}".format(file,nodelist[nindex],indeg,avg_incan[nindex]))
    os.chdir("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/three_state/files/plots/{}/".format(topofiles[j]))

    graph.savefig("{}_{}_{}_{}.png".format(file,nodelist[nindex],indeg,avg_incan[nindex]))
    os.chdir("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/three_state/files/topofiles")
    print(nodelist[nindex], "indegree:", indeg, "average_incan:", avg_incan[nindex]  )
    #hybrid=opt_hybrid_statesl(ssf,uadj,len(t1),len(t2))
    
    #number_of_hybrids=len(hybrid[1])

    #hybrid_frequency=hybrid_freq_cumulative_l(ssf,hybrid[1],hybrid[0])
    #print("number of hybrids:" , number_of_hybrids, "hybridf: ", hybrid_frequency)
    
    


    #return(node,avg_incan[nindex],outdeg,indeg,number_of_hybrids,hybrid_frequency)
    return(node)


def temp_shit(adj,file):
    n=len(adj)
    

    
    #wt hybrids





    
    
    steadys=boolean_siml.steady_states(adj,1000)
    ssf=boolean_siml.steady_state_frequency(steadys,adj)
    graph=boolean_siml.bar_graph_2(ssf)
    graph.title("{}_all_nodes".format(file))
    os.chdir("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/three_state/files/plots/{}/".format(topofiles[j]))

    graph.savefig("{}_all_nodes.png".format(file))
    os.chdir("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/three_state/files/topofiles")
    print(topofiles[j]  )
    #hybrid=opt_hybrid_statesl(ssf,uadj,len(t1),len(t2))
    
    #number_of_hybrids=len(hybrid[1])

    #hybrid_frequency=hybrid_freq_cumulative_l(ssf,hybrid[1],hybrid[0])
    #print("number of hybrids:" , number_of_hybrids, "hybridf: ", hybrid_frequency)
    
    


    #return(node,avg_incan[nindex],outdeg,indeg,number_of_hybrids,hybrid_frequency)
    return("done")
def remove_nodes_num(adj,z):
    n=len(adj)
    mat=[]
    for i in range(0,n):
        edge=[]
        

        if i not in z:
            for j in range(0,n):
                if j not in z:
                    edge.append(adj[i][j])
            mat.append(edge)
    return(mat)

def steady_node_state(adj,steady_state):
    n=len(adj)
    dist=[]
    som=0
    for i in range(0,n):
        sum=0
        for j in range(0,n):
            sum+=steady_state[j]*adj[j][i]
        dist.append(sum)
    for i in dist:
        som+=abs(i)
    return(dist,som)
def steady_node_states(adj,steady_states):
    n=len(adj)
    ddist=[]
    sdist=[]
    for i in steady_states:
        dist=[]
        for j in range(0,n):
            sum=0
            for k in range(0,n):
                sum+= i[k]*adj[k][j]
            dist.append(sum)
        count=0
        for m in dist:
            count+=abs(m)
        sdist.append(count)
        ddist.append(dist)
    return(ddist,sdist,steady_states)
path1="/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/centrality_analysis/topofiles"
filedat=glob.glob(path1+"/*topo")
topofiles=[x.split("/")[-1] for x in filedat]


j=0
print(topofiles[j])
dat=coherent_parser.clustered_matrix_file(topofiles[j])

adj=dat[0]
t1=dat[1]
t2=dat[2]
nodes=dat[-1]


dataa=[]




number=len(adj)
avg_incan=input_space_map.avg_incan_driver(adj,1000,100,2)
'''
for i in range(0,number):
    dataa.append(node_knockout(adj,nodes,i,topofiles[j],avg_incan))

df=pd.DataFrame(dataa, columns=["Node","Avg Incan", "OutDeg", "InDeg", "No_hybrids",  "Hybrid Frequency(1000 sims)" ])

df.to_csv("node_data_emt_racipe_15_dyn_incan.csv",index=False)

print(os.getcwd())
#print(node_knockout(adj,nodes,1,topofiles[0]))
'''
'''for i in range(0,number):
    print(node_knockout(adj,nodes,i,topofiles[j],avg_incan))
'''

