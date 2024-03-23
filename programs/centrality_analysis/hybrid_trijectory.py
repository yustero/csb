import coherenet_parser
import glob
import random
import triple_state
import randomization
import boolean_sim
import node_knockout_analysis

path1="/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/centrality_analysis/topofiles"
filedat=glob.glob(path1+"/*topo")
topofiles=[x.split("/")[-1] for x in filedat]


def states_evol(states,adj):
    out=[]
    for i in states:
        out.append(triple_state.input_steady(i,adj))
    return(out)

dat=coherenet_parser.clustered_matrix_file(topofiles[2])
adj=dat[0]
t1=len(dat[1])
t2=len(dat[2])

steadys=boolean_sim.steady_states(adj,1000)
ssf=boolean_sim.steady_state_frequency(steadys,adj)
hybrids=node_knockout_analysis.opt_hybrid_states(ssf,adj,t1,t2)[1]

k=states_evol(hybrids,adj)
for i in range(0,len(k)):
    print(hybrids[i], "in three state formalism : ", k[i],node_knockout_analysis.steady_node_state(adj,hybrids[i]))

boolean_sim.bar_graph(ssf,"hello")