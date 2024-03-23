import nteams
import boolonezero
import boolean_siml
import three_states_sim
import hybrid_states
import artificial

'''
take a nice two teams network, add two impurities randomly and compare it with a third team having one node 

we can make the frustration plots for three teams


'''
k=0.4
twoteam=artificial.network(8,8,k,k,k,k)
adjtwo=twoteam[0]
t1=twoteam[1]
t2=twoteam[2]

'''steadys=boolean_siml.steady_states(adjtwo,1000)
ssf=boolean_siml.steady_state_frequency(steadys,adjtwo)
boolean_siml.bar_graph(ssf,"hello")

adjimp=artificial.random_impurities(adjtwo,t1,t2,64)
steadys=boolean_siml.steady_states(adjimp,1000)
ssf=boolean_siml.steady_state_frequency(steadys,adjimp)
boolean_siml.bar_graph(ssf,"hello")
'''

three_adj=nteams.nteam_net(3,[8,8,8],[[0.4, 0.4, 0.4], [0.4, 0.4, 0.4], [0.4,0.4,0.4]])[0]
print(three_adj)
steadys=boolean_siml.steady_states(three_adj,1000)
ssf=boolean_siml.steady_state_frequency(steadys,three_adj)
boolean_siml.bar_graph(ssf,"hello")



