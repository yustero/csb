import Parser
import numpy as np
import random
import matplotlib.pyplot as plt
import glob
import csv

def subtract(a,b):
    output= np.zeros(len(a))
    for i in range(len(a)):
        output[i]= a[i]-b[i]
    return(output)

def inli(a,b):
    for j in b:
        if ((j==a).all()):
            return(True)
def notli(a,b):
    counter =0
    if a is not None and len(b)!=0:
        for j in b:
            if ((j==a).all()):
                counter+=1
        if counter ==0:
            return(True)
def index_np_li(li,np_array):
# Returns the index of numpy array in the given list
    counter =0
    for i in li:
        if (i==np_array).all():
            break
        counter+=1
    return(counter)


def evolve(nodes_initial,adj):
    timestep=0
    nodes_states=nodes_initial.copy()
    counter=0
    node_buffer=[]
    n=len(adj)
    zero=np.zeros(n)
    while True:
  
        k= random.randint(0,len(nodes_states)-1)
        state_calc=0
        check=nodes_states.copy()
        for i in range(0,len(nodes_initial)):
            state_calc+= nodes_states[i] * adj[i][k]

        if state_calc>0:

            if nodes_states[k] ==1:
                pass
            if nodes_states[k]== -1:

                nodes_states[k] = 1
        if state_calc<0:
            if nodes_states[k] == -1:
                pass
            if nodes_states[k]== 1:

                nodes_states[k] = -1

        if state_calc==0:
            pass
        print(nodes_states)
        timestep+=1
        if timestep == 1000:
            return("none")
            break
        if (subtract(check,nodes_states)== zero).all():
            if k not in node_buffer:
                node_buffer.append(k)
                counter+=1
            else:
                counter=0
                node_buffer=[]
        if len(node_buffer)==n:
            return(nodes_states)
            break
        
        check=nodes_states.copy()




def evolve_2(initial_nodes, adj):
    
    n=len(adj)
    zero=np.zeros(n)
    timer=0
    k_collect=[]
    while True:
        k = random.randint(0,n-1)
        effect_counter=0
        node_buffer=initial_nodes.copy()
        for i in range(0,n-1):
            effect_counter+= initial_nodes[i]*adj[i][k]
        if effect_counter>0:
            if initial_nodes[k] == 1:
                pass
            if initial_nodes[k]==-1:
                initial_nodes[k]=1
        if effect_counter == 0:
            pass
        if effect_counter < 0:
            if initial_nodes[k] == 1:
                initial_nodes[k]=-1
            if initial_nodes[k]== -1:
                pass
        if (node_buffer-initial_nodes==np.zeros(n)).all():
            if k not in k_collect:
                k_collect.append(k)
        else:
            k_collect=[]

        node_buffer=initial_nodes.copy()
        if len(k_collect)==n:
            
            return(initial_nodes)

        if timer==1000:
            return("none")
            break
        
        timer+=1




def random_inputs(adj):
    nodes_initial=[]
    for i in range(len(adj)):
        k = random.choice([-1,1])
        nodes_initial.append(k)
    return(np.array(nodes_initial))


def steady_statesf(adj, number_of_simulations):
    steady_states=[]

    for i in range(0,number_of_simulations):
        ss = evolve_2(random_inputs(adj),adj)
        if ss == "none":
            pass
        else:
            steady_states.append(ss)


    steady_statesli=[]

#    for i in steady_states:
#    steady_statesli.append(list(i)) 

    return(steady_states)

def steady_state_frequency_calculator(steady_states):
    ssf=[[],[]]
    for i in steady_states:
        if notli(i,ssf[0]):
            ssf[0].append(i)
            ssf[1].append(1)
        #print(i,ssf[0])
        if inli(i,ssf[0]):
            k= index_np_li(ssf[0],i)
            ssf[1][k]+=1    
    return(ssf)

def summary(ssf,file,n):
    
    output_data=open("data/{}{}".format(file.split(".")[0] , ".csv"),"w", newline="")
    
    wri=csv.writer(output_data)
    b=len(ssf[1])
    print(file)
    print("number of steadystates = {}".format(b), "number of nodes = {}".format(n))
    wri.writerow(["steady_state", "frequency"])
    for i in range(0,n):
        
        wri.writerow([ssf[0][i], ssf[1]])
    output_data.close()

topofiles_path= glob.glob("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/landscape_of_epithelial_mesenchymal_paper/teams_data/Teams-main/TopoFiles/*topo")
topofiles=[x.split("/")[-1] for x in topofiles_path]


def write_ssf(topofiles):
    for i in topofiles:
        
        file=i
        adj=Parser.adj_extract(file)
        steady_states= steady_statesf(adj,1000)

        ssf=steady_state_frequency_calculator(steady_states)
        n=len(adj)
        print(n)

        summary(ssf,file,n)
#def coherence(ssf):

#write_ssf(topofiles)


#Plotting

def bar_graph(ssf, image_name):
    frequencies=ssf[1]
    steadystates_plot=[]
    for i in ssf[0]:
        steadystates_plot.append("{}".format(i))
    print(steadystates_plot,frequencies)

    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(steadystates_plot, frequencies, color ='blue',
            width = 0.4)
    
    plt.xlabel("steady states")
    plt.ylabel("Frequencies")
    plt.title("Number of simulations: 1000")
    fig.autofmt_xdate()
    plt.savefig("{}{}".format(image_name,".png"))
    plt.show()
    print("ayeaye!")

#bar_graph(ssf,"melanoma_boolean_0")

#
#adj=Parser.adj_extract(topofiles[1])
#print(topofiles[1])
#ss=steady_statesf(adj,10000)
#print(len(adj))

#print(len(steady_state_frequency_calculator(ss)[1]))

'''       
adj= Parser.adj_extract(topofiles[0])
print(adj)

while True:
    input = random_inputs(adj)
    
    print(evolve(input,adj))'''