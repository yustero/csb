import boolean_sim
import Parser
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random 
import scipy.stats as sci

def random_adj(n):
    random_adj=[]
    for i in range(n):
        random_adj.append(np.zeros(n))
    for i in range(n):
        for j in range(n):
            random_adj[i][j]= random.randint(-1,1)
    return(random_adj)

adj=random_adj(8)

