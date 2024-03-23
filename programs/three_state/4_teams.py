import nteams
import boolean_siml

density=nteams.density_mat_gen(2,1)
adj=nteams.nteam_net(2,[5,5],density)[0]



steadys=boolean_siml.steady_states(adj,1000)
ssf=boolean_siml.steady_state_frequency(steadys,adj)

boolean_siml.bar_graph(ssf,"hello")