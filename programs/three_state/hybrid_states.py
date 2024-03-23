import coherent_parser
import boolean_sim
import three_states_sim
import numpy as np 
import copy
import topopath
import matplotlib.pyplot as plt

def opt_gen(adj,t1,t2):
    n=len(adj)
    hybrid_states=[]

    def genl(a,n):
        l=[a for i in range(0,n)]
        return(l)


    opt1= genl(1,t1)+genl(-1,t2)
    opt2=genl(-1,t1)+genl(1,t2)
    opt_states=[opt1,opt2]

    return(opt_states)



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
    #the above function but works with lists and differentiates optimum states from hybrid states
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


def state_node_perturb(state,i):
    state[i]=state[i]*-1
    return(state)

def index_np_li(np_array,li):
# Returns the index of numpy array in the given list
    counter =0
    for i in li:
        if (i==np_array).all():
            break
        counter+=1
    return(counter)

def opt_freq_cumulative(ssf,opt):
    n=len(ssf[1])
    opt_index=[]
    for i in opt:
        opt_index.append(index_np_li(i,ssf[0]))
    freq=0
    for i in range(0,n):
        if i in opt_index:
            freq+=ssf[1][i]
    return(freq)
    
def hybrid_freq_cumulative(ssf,opt):
    n=len(ssf[1])
    opt_index=[]
    for i in opt:
        opt_index.append(index_np_li(i,ssf[0]))
    freq=0
    for i in range(0,n):
        if i not in opt_index:
            freq+=ssf[1][i]
    return(freq)




def hybrid_freq_cum_l(ssf,adj, t1,t2):
# Gives the frequency of hybrid states, given the steady state distrubution and team sizes, (works for numpy arrays as states in ssf)
    opt=opt_hybrid_statesl(ssf,adj,t1,t2)[0]
    
    n=len(ssf[1])
    opt_index=[]
    for i in opt:
        opt_index.append(ssf[0].index(i))
    freq=0
    for i in range(0,n):
        if i not in opt_index:
            freq+=ssf[1][i]
    return(freq)   

def hybrid_freq_cum(ssf,adj, t1,t2):
    opt=opt_hybrid_states(ssf,adj,t1,t2)[0]
    
    n=len(ssf[1])
    opt_index=[]
    for i in opt:
        opt_index.append(index_np_li(i,ssf[0]))
    freq=0
    for i in range(0,n):
        if i not in opt_index:
            freq+=ssf[1][i]
    return(freq)

def hybrid_freq_cum2(ssf,adj, t1,t2):
#This considers the top two steady states as optimal instead of the one manufactured by teams since that is giving an issue with three state formalism 

    def two_largest(inlist):
        
        largest=inlist[0]
        second_largest=inlist[0]
        for item in inlist:
            if item > largest:
                largest = item
            elif largest > item > second_largest:
                second_largest = item
        # Return the results as a tuple
        return(inlist.index(largest), inlist.index(second_largest))

    def two_largest2(inlist):
        lib=inlist.copy()
        lib.sort(reverse=True)
        return ( inlist.index(lib[0]), inlist.index(lib[1]))

    opt_index= two_largest2(ssf[1])

    
    n=len(ssf[1])
    
    freq=0
    for i in range(0,n):
        if i not in opt_index:
            freq+=ssf[1][i]
    return(freq)







def number_hybrid_states(ssf):
    count=len(ssf[0])-2
    return(count)


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



def state_node_sum(adj,state):
    n=len(adj)
    sumd=[]
    for i in range(0,n):
        sum=0
        for j in range(0,n):
            sum+=state[j]*adj[j][i]
        sumd.append(sum)
    return(sumd)



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
def epi_mesi_score(state,t1,t2):
    n=len(state)
    epi=0
    mesi=0
    for i in range(0,t1):
        if state[i]==1:
            epi+=1
    for i in range(t1,n):
        if state[i]==1:
            mesi+=1
    epi=epi/t1
    mesi=mesi/t2
    epmes=epi-mesi
    return(epmes)

def hybrid_score(adj,states, t1,t2):
    #Hybrid scores for a list of states
    n=len(adj)
    scores=[]
    ns=len(states)
    for i in states:
        scores.append(epi_mesi_score(i,t1,t2))
    return(scores)

def different_nodes(li1,li2):
    n=len(li1)
    difn=[]
    
    for i in range(0,n):
        if li1[i]!=li2[i]:
            difn.append(i)
    return(difn)


def hybrid_nodes(adj,states,t1,t2):
    n=len(adj)
    ns=len(states)

    opt=[[1 for i in range(0,t1)]+ [-1 for i in range(0,t2)],[-1 for i in range(0,t1)]+ [1 for i in range(0,t2)] ]
    
    hybn=[]
    for i in range(0,ns):
        hybn.append([])

    scores=hybrid_score(adj,states,t1,t2)
    
    for i in range(0,ns):
        if scores[i]> 0:
            hybn[i]=different_nodes(opt[0],states[i])
        if scores[i]<0:
            hybn[i]=different_nodes(opt[1],states[i])       

    return(hybn)

def hybrid_node(adj,state,t1,t2):
    #This returns hybrid nodes of a single state instead of multiple states
    n=len(adj)
    

    opt=[[1 for i in range(0,t1)]+ [-1 for i in range(0,t2)],[-1 for i in range(0,t1)]+ [1 for i in range(0,t2)] ]
    
    hybn=[]

    score=epi_mesi_score(state,t1,t2)
    
    
    if score> 0:
        hybn=different_nodes(opt[0],state)
    if score<0:
        hybn=different_nodes(opt[1],state)       

    return(hybn)


def non_hybrid_nodes(adj,states,t1,t2):
    n=len(adj)
    ns=len(states)
    nonhyb=[]
    hybn=hybrid_nodes(adj,states,t1,t2)

    for i in hybn:
        nh=[]
        for j in range(0,n):
            if j not in i:
                nh.append(j)
        nonhyb.append(nh)
    return(nonhyb) 

def agree_disagree_cans(state1,state2,adj):
    n=len(adj)
    agree=[]
    disagree=[]
    suma=0
    sumd=0
    s1=state_node_sum(adj,state1)
    s2=state_node_sum(adj,state2)
    
    for i in range(0,n):
        if state1[i]==state2[i]:
            agree.append(i)
        elif state1[i]!=state2[i]:
            disagree.append(i)
    
    for i in agree:
        suma+=abs(s2[i])

    for i in disagree:
        sumd+=abs(s2[i])
    
    if suma>=sumd:
        hybrid_nodes=disagree
    if suma<sumd:
        hybrid_nodes=agree
    return(hybrid_nodes)


def weak_nodes(adj,states,t1,t2):
    weakn=[]   

    opt=[[1 for i in range(0,t1)]+ [-1 for i in range(0,t2)],[-1 for i in range(0,t1)]+ [1 for i in range(0,t2)] ]
    
    for i in states:
        weakn.append(agree_disagree_cans(opt[0], i, adj))

    return(weakn)

def abs_dist(li):
    d=[]
    for i in li:
        d.append(abs(i))
    return(d)


