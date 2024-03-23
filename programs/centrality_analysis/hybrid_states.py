import coherenet_parser
import boolean_sim
import three_states_sim
import numpy as np 
import copy

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

def opt_freq_cumulative(ssf,opt):
    n=len(ssf[1])
    opt_index=[]
    for i in opt:
        opt_index.append(index_np_li(i,ssf[0]))
    freq=0
    for i in range(0,n):
        if i not in opt_index:
            freq+=ssf[1][i]
    return(freq)
    

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
    n=len(adj)
    scores=[]
    ns=len(states)
    for i in states:
        scores.append(epi_mesi_score(i,t1,t2))
    return(scores)


