'''
The networks would be stored in a file called networks.json in a big list L

L[i] would be a list having data related to i'th network 

the first element would be the name of the network, 
the second element would be the adjacency matrix,
the third element would be nested matrix having a list having elements of first team and then the elements of second team,
the fourth element would be a nested list having lists of priorities of i'th node

This was for networks having completely nested canalizing functions. 


How do I store and implement random boolean functions? 
'''
import json 


def store_function(network):
    with open("nNetworks.json","r") as file:
        data=json.load(file)
    file.close()
    data.append(network)
    with open("nNetworks.json","w") as file:
        json.dump(data,file)
    file.close()
    return("Job done")

def list_networks(file):
    with open("{}".format(file),"r") as file:
        data=json.load(file)
    file.close()
    n=len(data)
    networks=[]
    for i in range(0,n):
        networks.append(data[i][0])
        print(data[i][0])
    return(networks)

def delete_network(filename,index):
    with open("{}".format(filename),"r") as file:
        data=json.load(file)
        del data[index]

    with open("{}".format(filename),"w") as file:
        json.dump(data,file)
        
        

    return("Job done")

def get_networks(filename):
    with open("{}".format(filename),"r") as file:
        data=json.load(file)
    return(data)



