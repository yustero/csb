import glob
path1="/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/programs/three_state/files/topofiles"
filedat=glob.glob(path1+"/*topo")
topofiles=[x.split("/")[-1] for x in filedat]
