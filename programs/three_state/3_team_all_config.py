import boolean_siml

#Normal toggle triad
adj1=[[1,-1,-1],[-1,1,-1],[-1,-1,1]]

#Self inhibition instead of activation
adj2=[[1,-1,-1],[-1,1,-1],[-1,-1,-1]]

#Third team activates other two
adj3=[[1,-1,-1],[-1,1,-1],[1,1,1]]

#One team activates the third
adj4=[[1,-1,1],[-1,1,-1],[-1,-1,1]]

#Both teams activate the third
adj5=[[1,-1,1],[-1,1,1],[-1,-1,1]]

#Both teams actiave the third and the third team also activates the two
adj6=[[1,-1,1],[-1,1,1],[1,1,1]]


adj=adj6
steadys=boolean_siml.steady_states(adj,1000)
ssf=boolean_siml.steady_state_frequency(steadys,adj)
boolean_siml.bar_graph(ssf,adj)