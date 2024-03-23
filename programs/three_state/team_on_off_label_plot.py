import matplotlib.pyplot as plt 

def act_inh_off_label_3_team(ssf,t1,t2,t3):
    labels=[]
    for i in ssf[0]:
        nact=0
        noff=0
        ninh=0

        nact2=0
        noff2=0
        ninh2=0


        nact3=0
        noff3=0
        ninh3=0

        for j in range(0,t1):
            if i[j]==1:
                nact+=1
            
            if i[j]==0:
                noff+=1    
            
            if i[j]==-1:
                ninh+=1
        str1="t1_{}_{}_{}".format(nact,noff,ninh)

        for j in range(t1,t1+t2):
            if i[j]==1:
                nact2+=1
            
            if i[j]==0:
                noff2+=1    
            
            if i[j]==-1:
                ninh2+=1
        str2="_t2_{}_{}_{}".format(nact2,noff2,ninh2)

        for j in range(t1+t2,t1+t2+t3):
            if i[j]==1:
                nact3+=1
            
            if i[j]==0:
                noff3+=1    
            
            if i[j]==-1:
                ninh3+=1
        str3="_t3_{}_{}_{}".format(nact3,noff3,ninh3)
        labels.append(str1+str2+str3)
    return(labels)

def bar_graph(ssf,t1,t2,t3):
    frequencies=ssf[1]
    steadystates_plot= act_inh_off_label_3_team(ssf,t1,t2,t3)

    print(steadystates_plot,frequencies)

    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(steadystates_plot, frequencies, color ='blue',
            width = 0.4)
    
    plt.xlabel("steady states")
    plt.ylabel("Frequencies")
    plt.title("Number of simulations: 1000")
    fig.autofmt_xdate()

    plt.show()
    print("ayeaye!")

import three_states_sim
import nteams
import boolean_siml
  
density=nteams.density_mat_gen(3,0.3)
adj=nteams.nteam_net(3,[5,5,4],density)[0]
steadys=three_states_sim.steady_states(adj,1000)
ssf=boolean_siml.steady_state_frequency(steadys,adj)
bar_graph(ssf,5,5,4)