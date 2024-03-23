import numpy as np 
from scipy.spatial import distance
b_l= [2794, 1244, 2803, 1173, 1020, 972]
r_l = [86, 45, 50, 5, 14, 7, 8, 17, 19, 4, 6, 2, 2]


bool_list = [[[1, 1, -1, -1], [1, -1, 1, 1], [-1, -1, 1, 1], [-1, 1, -1, -1], [-1, 1, 1, -1], [1, -1, -1, 1]], [2794, 1244, 2803, 1173, 1020, 972]]
racipe_list=[[[1, 1, -1, -1], [-1, -1, 1, 1], [-1, 1, -1, -1], [1, -1, -1, 1], [1, -1, 1, 1], [-1, -1, 1, -1], [1, 1, 1, -1], [1, 1, 1, 1], [-1, 1, 1, -1], [-1, 1, -1, 1], [-1, 1, 1, 1], [1, -1, 1, -1], [1, 1, -1, 1]], [40, 41, 20, 9, 22, 6, 3, 5, 6, 5, 2, 2, 4]]
def arrange_jsd(ssf_racipe,ssf_bool):
    ssf_bool_jsd=[[],[]]
    for i in range(len(ssf_racipe[0])):
        ssf_bool_jsd[0].append(list(np.zeros(len(ssf_racipe[0][1]))))
        ssf_bool_jsd[1].append(0)
    for i in range(len(ssf_racipe[0])):
        ssf_bool_jsd[0][i]= ssf_racipe[0][i]
        if ssf_racipe[0][i] in ssf_bool[0]:
            
            k= ssf_bool[0].index(ssf_racipe[0][i])
            ssf_bool_jsd[1][i] = ssf_bool[1][  k   ]
        else:
            ssf_bool_jsd[1][i]=0
    return(ssf_racipe,ssf_bool_jsd)
final = arrange_jsd(racipe_list,bool_list)
print(final[0][1], final[1][1])
print(distance.jensenshannon(np.array(final[0][1]), np.array(final[1][1])))

print(distance.jensenshannon([1,0],[0,1]))