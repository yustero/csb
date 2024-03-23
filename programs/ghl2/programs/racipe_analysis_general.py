import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
print(glob.glob("/home/"))
def racipe_parse(path, network):
    k = glob.glob(path)
    for i in k :
        sol_network = i.split("_")
        if len(sol_network)>2:
            if sol_network[0]== "network":
                with open("RACIPE2.0/{}".format(i)):
                    for i in range()

racipe_data=[]

def inli(a,b):
    for i in b:
        if (i==a):
            return(True)
def notli(a,b):
    counter =0
    for i in b:
        if (i==a):
            counter+=1
    if counter ==0:
        return(True)

def suml(a,b):
    sum =[]
    for i in range(0,len(b)):
        sum.append(0)
    for i in range(0,len(b)):
        sum[i]=a[i]+b[i]
    return(sum)