import boolean_sim
import randomization
import coherenet_parser
import glob
import copy
import numpy as np
import pandas as pd
from sklearn import linear_model
import artificial

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





def node_knockout(adj,nodelist,nindex,file):
    n=len(adj)
    node=nodelist[nindex]
    nodes=nodelist.copy()
    print(node)
    
    dat=coherenet_parser.clustered_matrix_file(file)
    te1= dat[1]
    te2=dat[2]
    
    #wt hybrids
    wtadj=dat[0]
    wsteayds=boolean_sim.steady_states(wtadj,1000)
    wtssf=boolean_sim.steady_state_frequency(wsteayds,wtadj)
    wthybrids=opt_hybrid_states(wtssf,wtadj,nodelist,te1,te2)[1]





    t1=te1.copy()
    t2=te2.copy()


    incan=incan_dist(adj)[0][nindex]
    indeg=indegree(adj)[nindex]
    outcan=outcan_dist(adj)[0][nindex]
    outdeg=outdegree(adj)[nindex]


    if node in t1:
        t1.remove(node)
    if node in t2:
        t2.remove(node)
    
    nodes.remove(nodelist[nindex])
    
    uadj=coherenet_parser.adj_nodes(file,nodes)[0]
    steadys=boolean_sim.steady_states(uadj,1000)
    ssf=boolean_sim.steady_state_frequency(steadys,uadj)

    print(nodelist[nindex], "outdegree:",outdeg, "indegree:", indeg, "outcan:", outcan, "incan:", incan, )
    hybrid=opt_hybrid_states(ssf,uadj,nodes,t1,t2)
    number_of_hybrids=len(hybrid[1])

    hybrid_frequency=hybrid_freq_cumulative(ssf,hybrid[1],hybrid[0])

    hamd=hamming_dist(hybrid[0],hybrid[1])
    new_hybr=new_hybrid(nindex,wthybrids,hybrid[1])
    no_new_hybr=len(new_hybr)
    print("number of hybrids:" , number_of_hybrids)
    print(number_of_hybrids,no_new_hybr)
    


    return(node,outdeg,outcan,indeg,incan,number_of_hybrids,hamd,no_new_hybr,new_hybr,hybrid_frequency)

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
i=-2
print(topofiles[i])
dat=coherenet_parser.clustered_matrix_file(topofiles[i])
adj=dat[0]
dat=coherenet_parser.clustered_matrix_adj(remove_nodes_num(adj,[]))
adj=dat[0]
#print(adj)
t1=dat[1]

t2=dat[2]
nodes=dat[-1]
steadys=boolean_sim.steady_states(adj,1000)
print("done")
ssf=boolean_sim.steady_state_frequency(steadys,adj)
input =[-1.0, 0.0, 2.0, -1.0, 4.0, -4.0, -2.0, -1.0, 1.0, 2.0, -1.0, -2.0, -1.0, -2.0, 0.0]
boolean_sim.bar_graph(ssf,"hello")
#hybrids=opt_hybrid_states(ssf,adj,t1,t2)
#print(steady_node_states(adj,hybrids[1]))

'''

dataa=[]




number=len(adj)
for i in range(0,number):
    dataa.append(node_knockout(adj,nodes,i,topofiles[0]))

df=pd.DataFrame(dataa, columns=["Node", "OutDeg", "OutCan", "InDeg","InCan", "No_hybrids", "hamming_distribution", "Number_of_new_hyrbids","New Hybrids", "Hybrid Frequency(1000 sims)" ])
df.to_csv("node_data_emt_racipe_15_node_hyf.csv",index=False)
'''

#print(node_knockout(adj,nodes,1,topofiles[0]))
df = pd.read_csv("node_data_emt_racipe_15_node_hyf.csv")
