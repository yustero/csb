import pandas as pd
import os
import numpy as np
os.chdir("/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/robustness_plasticity/programs/RACIPE2.0")

data=pd.read_csv("abspa_solution_1.dat", sep="\t")
data_arr=np.array(data.values)
print(data_arr[:,2])