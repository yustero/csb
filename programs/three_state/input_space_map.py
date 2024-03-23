import boolean_siml
import coherent_parser
import node_metrics
import three_states_sim
import matplotlib.pyplot as plt 
import random
import numpy as np 
import topopath
import hybrid_states
import artificial
import randomization


n=0
data=coherent_parser.clustered_matrix_file(topopath.topofiles[n])

adj=data[0]
t1=len(data[1])
t2=len(data[2])
nodes=data[-1]


'''what do i want to do? 
#1 Identify states which end up in multiple basins
#2 Establish that hybrid input states end up in hybrid basins - obvious 
#3 Identify the important timesteps to study the states at 
#4 Maybe look at DUNs towards the steady state timesteps 
#5 Note the state of the nodes as well to find out nodes which are off for the most part and verify if incan value is a good proxy for that'''

'''Tracking hybrid nodes can yield some information about trijectory, if your hybrid nodes change completely over the duration of your simulation then that is a long trijectory
and anyways during the simulation, ideally it is just the hybrid nodes which need to be evolved. For optimal states, hybrid nodes should ideally just reduce one by one on average   

It would be interesting to see how inputs leading to hybrid states evolve overtime 
'''


def mean_time(adj,number_sim):
    time_data=[]
    time_distr=[[],[]]
    n=len(adj)

    def time_dist_update(time_dist,ss, time):
        if ss not in time_dist[0]:
            time_dist[0].append(ss)
            time_dist[1].append([])
            
            inde=time_dist[0].index(ss)
            time_dist[1][inde].append(time)

        if ss in time_dist[0]:
            inde=time_dist[0].index(ss)
            time_dist[1][inde].append(time)
        return(time_dist)


    for i in range(0,number_sim):
        t=0
        
        nodes_state=boolean_siml.random_inputs(adj)
        timtaken=0

        while t<1000:
            k=random.randint(0,n-1)
            
            out = boolean_siml.evolve(nodes_state,adj,k)
            if boolean_siml.steady_check(out,adj):
                time_dist_update(time_distr,out,timtaken)                
                time_data.append(timtaken)
                timtaken=0
                break
                
            else :
                nodes_state=out
                timtaken+=1
            
            t+=1
            if t==1000:
                break
    return(time_distr,np.mean(time_data))


def input_basin_track(adj,number_sim):
    n=len(adj)
    steady_states=[]
    in_basin=[[],[]]

    epimes_score=[[],[]]
    abs_epimes_score=[[],[]]

    def input_basin_arrange(basin_data,ss, input):
        if ss not in basin_data[0]:
            basin_data[0].append(ss)
            basin_data[1].append([])
            inde=basin_data[0].index(ss)
            basin_data[1][inde].append(input)
        
        if ss in basin_data[0]:
            inde=basin_data[0].index(ss)
            basin_data[1][inde].append(input)
        return(basin_data)

    for i in range(0,number_sim):
        t=0
        
        nodes_state=boolean_siml.random_inputs(adj)
        input=nodes_state.copy()
        timtaken=0

        while t<1000:
            k=random.randint(0,n-1)
            
            out = boolean_siml.evolve(nodes_state,adj,k)
            if boolean_siml.steady_check(out,adj):
                input_basin_arrange(in_basin,out,input)                

                timtaken=0
                break
                
            else :
                nodes_state=out
                timtaken+=1
            
            t+=1
            if t==1000:
                break
    
    ns=len(in_basin[0])
    
    dat=coherent_parser.clustered_matrix_adj(adj)
    t1=dat[1]
    t2=dat[2]

    def epi_mesi_dist(li,t1,t2):
        epimesdist=[]
        for i in li: 
            epimesdist.append(hybrid_states.epi_mesi_score(i,t1,t2))
        return(epimesdist)

    def abs_epi_mesi_dist(li,t1,t2):
        epimesdist=[]
        for i in li: 
            epimesdist.append(abs(hybrid_states.epi_mesi_score(i,t1,t2)))
        return(epimesdist)



    for i in range(0,ns):
        epimes_score[0].append(hybrid_states.epi_mesi_score(in_basin[0][i],t1,t2))
        epimes_score[1].append(np.mean(epi_mesi_dist(in_basin[1][i],t1,t2)))
        
        abs_epimes_score[0].append(abs(hybrid_states.epi_mesi_score(in_basin[0][i],t1,t2)))
        abs_epimes_score[1].append(np.mean(abs_epi_mesi_dist(in_basin[1][i],t1,t2)))

    
    
    return(in_basin, epimes_score,abs_epimes_score)


'''Hybrid states might not have very hybrid basins, they might have really symmetrical basins'''



def multi_basin(adj,number_sim):
    #returns innputs which end up at multiple basins

    n=len(adj)

    basin_inputs=[]
    basin_outputs=[]

    for i in range(0,number_sim):
        input=boolean_siml.random_inputs(adj)

        for j in range(0,n):
            output=boolean_siml.input_steady(input,adj)
            if input not in basin_inputs:
                basin_inputs.append(input)

                basin_outputs.append(output)
            if input in basin_inputs:
                index=basin_inputs.index(input)
                if len(output)!=0 and output[0] not in basin_outputs[index]:
                    inde=basin_inputs.index(input)
                    basin_outputs[inde].append(output[0])


    return([basin_inputs,basin_outputs])
                
def hybrid_scores_list(li,t1,t2):
    scores=[]
    for i in li:
        scores.append(hybrid_states.epi_mesi_score(i,t1,t2))
    return(scores)


def overtime_incan(adj,number_sim):

    n=len(adj)
    dist=[]

    for i in range(0,number_sim):
        dist.append([])
        t=0
        
        nodes_state=boolean_siml.random_inputs(adj)
        input=nodes_state.copy()
        timtaken=0

        while t<1000:
            k=random.randint(0,n-1)
            
            out = boolean_siml.evolve(nodes_state,adj,k)
            dist[i].append(node_metrics.abs_state_node_sum(adj,out))
            #print("abs value:",node_metrics.abs_state_node_sum(adj,out), "non abs value:", node_metrics.state_node_sum(adj,out))
            if boolean_siml.steady_check(out,adj):
                               

                timtaken=0
                break
                
            else :
                nodes_state=out
                timtaken+=1
            
            t+=1
            if t==1000:
                break
    return(dist)



def overtime_incan_triple(adj,number_sim):

    n=len(adj)
    dist=[]

    for i in range(0,number_sim):
        dist.append([])
        t=0
        
        nodes_state=three_states_sim.random_inputs(adj)
        input=nodes_state.copy()
        timtaken=0

        while t<1000:
            k=random.randint(0,n-1)
            
            out = three_states_sim.evolve(nodes_state,adj,k)
            dist[i].append(node_metrics.abs_state_node_sum(adj,out))
            #print("abs value:",node_metrics.abs_state_node_sum(adj,out), "non abs value:", node_metrics.state_node_sum(adj,out))
            if three_states_sim.steady_check(out,adj):
                               

                timtaken=0
                break
                
            else :
                nodes_state=out
                timtaken+=1
            
            t+=1
            if t==1000:
                break
    return(dist)




def overtime_incan_triple_non_abs(adj,number_sim):

    n=len(adj)
    dist=[]

    for i in range(0,number_sim):
        dist.append([])
        t=0
        
        nodes_state=three_states_sim.random_inputs(adj)
        input=nodes_state.copy()
        timtaken=0

        while t<1000:
            k=random.randint(0,n-1)
            
            out = three_states_sim.evolve(nodes_state,adj,k)
            dist[i].append(node_metrics.state_node_sum(adj,out))
            #print("abs value:",node_metrics.abs_state_node_sum(adj,out), "non abs value:", node_metrics.state_node_sum(adj,out))
            if three_states_sim.steady_check(out,adj):
                               

                timtaken=0
                break
                
            else :
                nodes_state=out
                timtaken+=1
            
            t+=1
            if t==1000:
                break
    return(dist)

















def incan_dist_graph(dist, max_time, time_steps, adj):
    
    n=len(adj)
    node_data=[[] for x in range(0,n)]
    time=[x for x in range(0,max_time,time_steps)]
    
    useful_paths=[]
    for i in dist:
        if len(i)>= max_time:
            useful_paths.append(i)
    
    for i in range(0,max_time,time_steps):
        for j in range(0,n):
            node_dat=[]
            for k in useful_paths:
                node_dat.append(k[i][j])
            node_data[j].append(np.mean(node_dat))
    return(node_data,time)



def incan_all_path_dist_graph(dist,max_time, time_steps, adj):
    n=len(adj)
    node_data=[[] for x in range(0,n)]
    time=[x for x in range(0,max_time,time_steps)]
    useful_paths=[]
    for i in dist:
        if len(i)>= max_time:
            useful_paths.append(i)
    
    for i in range(0,max_time,time_steps):
        for j in range(0,n):
            node_dat=[]
            for k in dist:
                if len(k)>i:
                    node_dat.append(k[i][j])

            node_data[j].append(np.mean(node_dat))
    return(node_data,time)
    
def average_norm_incan(node_dist):
    #data revers to outcome of incan_all_path.. function
    
    avg=[]
    for i in node_dist:
        avg.append(np.mean(i))

    return(avg)


def incan_all_path_dist_graph_indeg_normal(dist,max_time, time_steps, adj):
    #This normalizes the incan value for each node with respect to its indegree
    indeg_dist=node_metrics.indegree(adj)


    n=len(adj)
    node_data=[[] for x in range(0,n)]
    norm_node_data=[[] for x in range(0,n)]
    
    time=[x for x in range(0,max_time,time_steps)]
    useful_paths=[]
    for i in dist:
        if len(i)>= max_time:
            useful_paths.append(i)
    
    for i in range(0,max_time,time_steps):
        for j in range(0,n):
            node_dat=[]
            for k in dist:
                if len(k)>i:
                    node_dat.append(k[i][j])

            node_data[j].append(np.mean(node_dat))
    
    for i in range(0,n):
        for j in node_data[i]:
            if indeg_dist[i]!=0:
                norm_node_data[i].append(j/indeg_dist[i])
            else:
                norm_node_data[i].append(0)
    avg=average_norm_incan(norm_node_data)

    stat_norm_incan=node_metrics.indeg_summary(adj)[-1]
    infdr=node_metrics.influence_static_can(adj)[0]
    k=max(infdr)
    norm_infdr=[x/k for x in infdr]
    return(norm_node_data,time,avg,stat_norm_incan,indeg_dist,norm_infdr)





def incan_dist_plot_all_nodes(incan_dat,nodes):
    node_data=incan_dat[0]
    time = incan_dat[1]
    avg=incan_dat[2]

    n=len(node_data)
    for i in range(0,n):
        plt.plot(time,node_data[i],label="{}_{}".format(nodes[i],avg[i]))
        print(avg[i],nodes[i])
    plt.legend(loc="upper left")
    plt.xlabel("Time steps")    
    plt.ylabel("Drive")
    return(plt)


def incan_dist_plot_all_nodes_team_coloured(incan_dat,nodes,adj,t1,t2):
    node_data=incan_dat[0]
    time = incan_dat[1]
    avg=incan_dat[2]

    n=len(node_data)
    for i in range(0,n):
        if i< t1:
            plt.plot(time,node_data[i],label="{}_{}".format(nodes[i],avg[i]), color="r")
        if i>= t1:
            plt.plot(time,node_data[i],label="{}_{}".format(nodes[i],avg[i]), color="g")

        print(avg[i],nodes[i])
    plt.legend(loc="upper left")
    plt.xlabel("Time steps")    
    plt.ylabel("Absolute Mean InCan Value")
    return(plt)


def incan_dist_plot_all_nodes_static_colored(incan_dat,nodes):
    #plots the dyamic incan values colored with static incan_norm
    node_data=incan_dat[0]
    time = incan_dat[1]
    avg=incan_dat[2]
    stat_incan=incan_dat[3]
    indeg_dist=incan_dat[4]
    infdr=incan_dat[5]

    n=len(node_data)

    blues=plt.get_cmap("YlOrRd")

    for i in range(0,n):
        plt.plot(time,node_data[i],color= blues(infdr[i]),label="{}_{}_{}".format(nodes[i],avg[i],infdr[i]), alpha=1)
        print(avg[i],nodes[i],indeg_dist[i])
    plt.legend(loc="upper right")
    plt.xlabel("Time steps")    
    plt.ylabel("Absolute Mean InCan Value")
    return(plt)


def incan_dist_plot_all_nodes_indeg_coloured(incan_dat,nodes):
    #plots the dyamic incan values colored with static incan_norm
    node_data=incan_dat[0]
    time = incan_dat[1]
    avg=incan_dat[2]
    stat_incan=incan_dat[3]
    indeg_dist=incan_dat[4]
    infdr=incan_dat[5]

    n=len(node_data)

    blues=plt.get_cmap("YlOrRd")

    for i in range(0,n):
        plt.plot(time,node_data[i],label="{}_{}_{}".format(nodes[i],avg[i],indeg_dist[i]), alpha=1)
        print(avg[i],nodes[i],indeg_dist[i])
    plt.legend(loc="upper right")
    plt.xlabel("Time steps")    
    plt.ylabel("Absolute Mean InCan Value")
    return(plt)

def avg_incan_vs_indeg(incan_dat,nodes):
    #Plots average incan vs indegree
    node_data=incan_dat[0]
    time = incan_dat[1]
    avg=incan_dat[2]
    stat_incan=incan_dat[3]
    indeg_dist=incan_dat[4]
    infdr=incan_dat[5]

    n=len(node_data)

    plt.scatter(avg,indeg_dist)
    return(plt)


def incan_dist_plot_nodelist(incan_dat,nodes,nodelist):
    #node list has list of node indexes which need to be plotted instead of all nodes

    node_data=incan_dat[0]
    time = incan_dat[1]

    n=len(node_data)
    for i in nodelist:
        plt.plot(time,node_data[i],label=nodes[i])
    plt.legend(loc="upper right")
    plt.xlabel("Time steps")    
    plt.ylabel("Absolute Mean InCan Value")
    return(plt)

def hybrid_node_evolution(inputs,adj,t1,t2):
    #to track "hybrid nodes over time"

    n=len(adj)
    ns = len(inputs)
    dist=[]

    for i in range(0,ns):
        dist.append([])
        t=0
        
        nodes_state=inputs[i]
        input=nodes_state.copy()
        timtaken=0

        while t<1000:
            
            
            dist[i].append(hybrid_states.hybrid_node(adj,nodes_state,t1,t2))
            
            k=random.randint(0,n-1)
            out = boolean_siml.evolve(nodes_state,adj,k)
            if boolean_siml.steady_check(out,adj):
                               

                timtaken=0
                break
                
            else :
                nodes_state=out
                timtaken+=1
            
            t+=1
            if t==1000:
                break
    return(dist)
     
def state_transition_path(state,adj ):
    trij=[state]
    nodeup=[]
    n=len(adj)
    t=0
    
    #trij and nodeup have different lengths 
    
    nodes_state=state
    input=nodes_state.copy()
    timtaken=0

    while t<1000:
        k=random.randint(0,n-1)
        
        out = boolean_siml.evolve(nodes_state,adj,k)
        trij.append(out)
        nodeup.append(k)

        if boolean_siml.steady_check(out,adj):
                            

            timtaken=0
            break
            
        else :
            nodes_state=out
            timtaken+=1
        
        t+=1
        if t==1000:
            break
    
    return(trij,nodeup)

def bifurcation_graph(input,adj,t1,t2,no_sim):
    trijs=[]

    def hamming_li(li):
        hamli=[]
        ns=len(li)
        #returns a list of having hamming values with respect to first element 
        for i in range(0,ns):
            hamli.append(hybrid_states.hammd(li[0], li[i]))
        return(hamli)

    for i in range(0,no_sim):
        trijs.append(hamming_li(state_transition_path(input,adj)[0]))
    
    for i in trijs:
        time = [x for x in range(0,len(i))]
        plt.plot( time , i, "-", alpha=0.25)
        plt.scatter(time[-1],i[-1] )
    plt.xlabel("Time")
    plt.ylabel("Hamming distance from initial state")
    plt.title("Hamming distance trijectories of an input leading to multiple basins")    
    plt.show()

def avg_incan_driver(adj,no_sim,max_time,time_steps):
    dist=overtime_incan(adj,no_sim)
    data=incan_all_path_dist_graph_indeg_normal(dist,max_time,time_steps,adj)
    return(average_norm_incan(data[0]))




#infdr=node_metrics.influence_static_can(adj)[0]
#for i in range(0,len(infdr)):
 #   print(infdr[i],nodes[i])

#Driver
k=0.3
data2=artificial.network(15,15,k,k,k,k)
nodes=data2[1]+data2[2]
adj=data2[0]


#adj=randomization.random_edge_exchange(adj,10)

n=0 
dat=coherent_parser.clustered_matrix_file(topopath.topofiles[n])
#adj=dat[0]
t1=dat[1]
t2=dat[2]
#nodes=t1+t2

dist=overtime_incan_triple(adj,1000)
data=incan_all_path_dist_graph_indeg_normal(dist,200,2,adj)



plot=incan_dist_plot_all_nodes(data,nodes)
#plot=incan_dist_plot_all_nodes_indeg_coloured(data,nodes)
#plot=avg_incan_vs_indeg(data,nodes)
#plot=incan_dist_plot_all_nodes_static_colored(data,nodes)
#plot.title("{}_normalized incan".format(topopath.topofiles[n]))
#plt.title("{}_drive_with_indegree".format(topopath.topofiles[n]))
#plt.title("{}_avgincan_vs_nodes".format(topopath.topofiles[n]))
#plt.title("{}_avgincan_vs_nodes".format("Artificial network spar=0.3"))
#plt.xlabel("avg_incan")
#plt.ylabel("indegree")
plt.title("drive_values_{}".format(topopath.topofiles[n]))
plot.show()


'''could the hybrid nodes be crucial for switching?'''


'''
more_ts=node_metrics.high_team_strength(adj,100,2)
print(more_ts)

for i in more_ts:
    dist=overtime_incan_triple(i,1000)
    data=incan_all_path_dist_graph_indeg_normal(dist,100,2,i)
    
    plot=incan_dist_plot_all_nodes_static_colored(data,nodes)
    #plot.title("{}_normalized incan".format(topopath.topofiles[n]))
    plt.title("{}randomswap_norm incan ".format("high ts"))
    plot.show()
'''

'''#Driver for claus networks 

import meta_analysis_paper_networks as mnp
import os
for i in mnp.topoli:
    data=mnp.clustered_matrix_file(i)
    adj=data[0]
    t1=len(data[1])
    t2=len(data[2])
    nodes=data[-1]
    time = int(np.floor(mean_time(adj,1000)[1]+10))
    


    dist=overtime_incan_triple_non_abs(adj,1000)
    data=incan_all_path_dist_graph_indeg_normal(dist,time,2,adj)
    
    plot=incan_dist_plot_all_nodes_team_coloured(data,nodes,adj,t1,t2)
    #plot.title("{}_normalized incan".format(topopath.topofiles[n]))

    plt.title("{} non absolute drive  ".format(i))
    plt.show()

'''


'''#Artificial Analysis
import data

adj=data.artificial_net_impure2
t1=len(data.t1)
t2=len(data.t2)
nodes=data.t1+data.t2
time = int(np.floor(mean_time(adj,1000)[1]+10))



dist=overtime_incan_triple(adj,1000)
data=incan_all_path_dist_graph_indeg_normal(dist,time,2,adj)

plot=incan_dist_plot_all_nodes(data,nodes)
#plot.title("{}_normalized incan".format(topopath.topofiles[n]))

plt.title("{}   ".format("Artificial Impure random"))
plt.show()
'''