#This has the plots of selectiev turn off of k nodes of low drives relative to random k nodes on number of steady states obtained 

import matplotlib.pyplot as plt 

emtracipe15 = [4, 8, 10, 7, 9, 10, 8, 4, 6, 6, 13, 7, 8, 8, 8, 9, 13, 7, 8, 5, 9, 8, 8, 9, 11, 11, 11, 5, 7, 12, 8, 10, 7, 10, 8, 7, 11, 8, 9, 21, 10, 5, 11, 4, 8, 6, 11, 7, 7, 8, 6, 7, 14, 11, 6, 12, 6, 5, 7, 6, 9, 7, 10, 9, 9, 6, 5, 9, 9, 12, 9, 4, 4, 11, 7, 11, 11, 8, 9, 6, 7, 11, 8, 6, 12, 8, 10, 7, 10, 6, 11, 9, 11, 10, 8, 12, 4, 4, 6, 4, 10]
emtracipe22=[14, 27, 35, 45, 38, 36, 37, 38, 32, 30, 36, 27, 46, 33, 34, 44, 34, 40, 46, 31, 37, 28, 38, 38, 45, 36, 49, 27, 37, 35, 34, 30, 38, 33, 46, 36, 34, 46, 35, 44, 45, 42, 49, 40, 29, 35, 41, 39, 40, 32, 29, 37, 29, 41, 33, 35, 41, 39, 34, 31, 29, 34, 31, 36, 47, 41, 46, 35, 44, 29, 28, 35, 25, 42, 42, 42, 37, 29, 33, 42, 31, 30, 35, 43, 29, 30, 33, 44, 31, 31, 34, 28, 36, 40, 20, 49, 38, 33, 36, 47, 44]
plt.hist(emtracipe22, bins=20)
plt.axvline(x=4, color="red")
plt.title("Selective turn off of 3 nodes having lowest drive compared to selective turn off of 3 random nodes for the 22 node emtracipe network")
plt.xlabel("Number of steady states")
plt.ylabel("Frequency")
plt.show()