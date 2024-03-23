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

def overtime_drive_2_state(adj,number_sim):

    n=len(adj)
    dist=[]

    for i in range(0,number_sim):
        dist.append([])
        t=0
        
        nodes_state=boolean_siml.random_inputs(adj) #uses (1,-1)
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

def overtime_drive_3_state(adj,number_sim):

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

#In the above two functions, I haven't divided by the indegree. 

def drive_dist_graph(dist, max_time, time_steps, adj):
    
    '''what this function does is takes the distribution of drive values of different states and then selects the ones 
    which have lengths greater then max time and then computes the average'''

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

def drive_all_path_dist_graph(dist,max_time, time_steps, adj):
    '''This function instead of choosing paths with lengths greater than the threshold, while evaluating the node average for a time step i, it looks for all the trijectories which 
    have lengths greater than equal to i and then evaluates the average over those trijectories, this means that for initial time steps, the average has more data points'''


    n=len(adj)
    node_data=[[] for x in range(0,n)]
    time=[x for x in range(0,max_time,time_steps)]
    
    for i in range(0,max_time,time_steps):
        for j in range(0,n):
            node_dat=[]
            for k in dist:
                if len(k)>i:
                    node_dat.append(k[i][j])

            node_data[j].append(np.mean(node_dat))
    return(node_data,time)
    
def average_norm_drive(node_dist):
    #data revers to outcome of incan_all_path.. function
    #this is used in the function right below this to calculate average values of a list
    avg=[]
    for i in node_dist:
        avg.append(np.mean(i))

    return(avg)

def drive_all_path_dist_graph_indeg_normal(dist,max_time, time_steps, adj):
    #This normalizes the incan value for each node with respect to its indegree
    #dist refers to output of overtime_ functions
    #This is the primary function referenced later
    indeg_dist=node_metrics.indegree(adj)


    n=len(adj)
    node_data=[[] for x in range(0,n)]
    norm_node_data=[[] for x in range(0,n)]
    
    time=[x for x in range(0,max_time,time_steps)]
    
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
    avg=average_norm_drive(norm_node_data)

    stat_norm_incan=node_metrics.indeg_summary(adj)[-1]
    infdr=node_metrics.influence_static_can(adj)[0]
    k=max(infdr)
    norm_infdr=[x/k for x in infdr]

    #norm_node_data represents the indegree normalized values of average drive over the entire ensemble.
    #avg is the list of average of norm_node_data which is the global average of the data for each node. 
    return(norm_node_data,time,avg,stat_norm_incan,indeg_dist,norm_infdr)


#Plotting

def drive_dist_plot_all_nodes(cumulative_dat,nodes):
    #here cumulative_dat refers to collective output of drive_all_path_dist_indeg_normal
    
    node_data=cumulative_dat[0]
    time = cumulative_dat[1]
    avg=cumulative_dat[2]

    n=len(node_data)
    for i in range(0,n):
        plt.plot(time,node_data[i],label="{}_{}".format(nodes[i],avg[i]))
        print(avg[i],nodes[i])
    plt.legend(loc="upper left")
    plt.xlabel("Time steps")    
    plt.ylabel("Drive")
    return(plt)

 
#To rank nodes in terms of slope
def drive_rank(drive_data,nodes):
    #This function ranks nodes on the basis of their drive slopes
    #drive_data refers to output of drive_dist_all_path_indeg_normal_function

    node_drive_data=drive_data[0]
    time=drive_data[1]

    slope_list=[]
    for i in node_drive_data:
        slope_list.append((i[-1]-i[1]/time[-1]))
        
    return(slope_list)

def drive_order(drive_rank):
    #This takes the list having drive ranks and then yields a list having list indices such that their corresponding values in the list are arranged in an ascending order
    return(list(np.argsort(drive_rank)))

def epi_mes_score(state,t1,t2,adj):
    #t1 and t2 are lists having indices of nodes in those teams 
    n=len(adj)
    score=0
    #here more postive the score, the more epithelial it is and the more negative the score the more mesenchymal it is. 

    for i in range(0,n):
        if i in t1:
            if state[i]==1:
                score+=1
        if i in t2:
            if state[i]==1:
                score+=-1
    return(score)

def epi_mes_score_dist(states,t1,t2,adj):
    n=len(adj)
    scores=[]
    for i in states:
        scores.append(epi_mes_score(i,t1,t2,adj))
    return(scores)    





'''i=0
net=coherent_parser.clustered_matrix_file(topopath.topofiles[i])
adj=net[0]
nodes=net[-1]

data=overtime_drive_3_state(adj,1000)
drive_data=drive_all_path_dist_graph_indeg_normal(data,100,2,adj)
print(drive_order(drive_rank(drive_data,nodes)))
print(nodes)'''