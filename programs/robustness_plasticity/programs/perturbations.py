import numpy as np
import random
import pandas as pd
import glob
import copy



def one_edge_deletion(adj):
    n=len(adj)
    while True:
        a=random.randint(0,n-1)
        b=random.randint(0,n-1)
        if adj[a][b]!=0:
            adj[a][b]=0
            return(adj)
            break

def one_edge_sign_inversion(adj):
    n=len(adj)
    adj2=copy.deepcopy(adj)
    while True:
        a=random.randint(0,n-1)
        b=random.randint(0,n-1)
        if adj2[a][b]!=0:
            adj2[a][b]=adj2[a][b]*(-1)
            return(adj2)
            break

def one_edge_addition(adj):
    n=len(adj)
    while True:
        a=random.randint(0,n-1)
        b=random.randint(0,n-1)
        if adj[a][b]==0:
            adj[a][b]=1
            return(adj)
            break
