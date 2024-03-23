import cumulative_drive
import boolean_siml
import topopath
import coherent_parser


n=2
file=topopath.topofiles[n]
print(topopath.topofiles)
data=coherent_parser.clustered_matrix_file(file)
adj=data[0]

steadys=boolean_siml.steady_states(adj,1000)
ssf=boolean_siml.steady_state_frequency(steadys,adj)
print(len(ssf[0]))

drivedist=cumulative_drive.drive_dist(ssf[0],adj)
print(cumulative_drive.average_drive(drivedist,adj))