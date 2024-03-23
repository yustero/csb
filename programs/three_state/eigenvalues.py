import topopath 
import numpy as np 
import artificial 
import coherent_parser

z=0.3
k=0
network= coherent_parser.clustered_matrix_file(topopath.topofiles[k])
adj=network[0]
adj=artificial.network(8,8,z,z,z,z)[0]

print(topopath.topofiles)

for i in np.linalg.eigh(adj)[0]:
    if i>1:
        print("great",i)