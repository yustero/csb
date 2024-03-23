import boolean_siml
import hybrid_states
import topopath
import node_metrics
import coherent_parser
import matplotlib.pyplot as plt

def opt_hybrid_statesl(ssf,adj,nt1,nt2):
    #the above function but works with lists and differentiates optimum states from hybrid states and also yields the respective frequencies and abs_drive of the states. 
    n=len(adj)
    hybrid_states=[]
    hybrid_freq=[]
    hybrid_drive=[]


    opt_freq=[]
    opt_drive=[]

    def genl(a,n):
        l=[a for i in range(0,n)]
        return(l)


    opt1= genl(1,nt1)+genl(-1,nt2)
    opt2=genl(-1,nt1)+genl(1,nt2)
    opt_states=[opt1,opt2]


    counter=0
    for i in ssf[0]:
        if not ((i[0:nt1]== genl(1,nt1) and i[nt1:] == genl(-1,nt2)) or (i[0:nt1]== genl(-1,nt1) and i[nt1:] == genl(1,nt2))):
            hybrid_states.append(i)
            hybrid_freq.append(ssf[1][counter])
            hybrid_drive.append(sum(node_metrics.abs_state_node_sum(adj,i)))
            
        
        else:
            opt_drive.append(sum(node_metrics.abs_state_node_sum(adj,i)))
            opt_freq.append(ssf[1][counter])

        counter+=1
    return(opt_states,hybrid_states,hybrid_freq,hybrid_drive,opt_freq, opt_drive)


'''for i in topopath.topofiles:
    file = i
    data=coherent_parser.clustered_matrix_file(file)
    adj=data[0]
    t1=len(data[1])
    t2=len(data[2])
    steadys=boolean_siml.steady_states(adj,1000)
    ssf=boolean_siml.steady_state_frequency(steadys,adj)

    data=opt_hybrid_statesl(ssf,adj,t1,t2)


    plt.scatter(data[2],data[3])
    plt.xlabel("Frequencies")
    plt.ylabel("Drive sum")
    plt.title("Hybrid Types{}".format(file))
    plt.show()
'''