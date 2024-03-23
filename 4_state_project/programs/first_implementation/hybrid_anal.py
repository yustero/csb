import multi_rules
import coherent_parser
import topopath
import node_metrics

def drive_dist(states,adj):
    def adj_sum(state,pos):
        #Function to get sum for i'th position 
        sum=0
        n=len(adj)
        for i in range(0,n):
            sum+=adj[i][pos]*state[i]
        return(sum)
    #distribution of drive values of each node for the given states
    

    indegree=node_metrics.indegree(adj)
    n=len(adj)
    values=[]
    
    #Following code iterates over all the states and all its nodes and gets a list of distribution of drive values
    for i in states:
        drive_dist=[]
        for j in range(0,n):
            drive_dist.append(abs(adj_sum(i,j)/indegree[j]))
        
        values.append(drive_dist)
    
    return(values)

#The above function generates distribution of drive values. A metric of interest is the sum drive values of all nodes divided by number of nodes. The following function calculates that 

def average_drive(drivedist,adj):
    n=len(adj)
    values=[]

    for i in drivedist:
        sum=0
        for j in range(0,n):
            sum+=i[j]
        values.append(sum/n)
    return(values)


n=2
file=topopath.topofiles[n]
print(topopath.topofiles)
data=coherent_parser.clustered_matrix_file(file)
adj=data[0]

steadys=multi_rules.steady_states(adj,1000)
ssf=multi_rules.steady_state_frequency(steadys,adj)
print(len(ssf[0]))
drivedist=drive_dist(ssf[0],adj)
print(average_drive(drivedist,adj))