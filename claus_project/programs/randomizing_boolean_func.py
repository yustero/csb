'''
In this I have to figure out how to assign random boolean functions to nodes. 

Another direction we could take would be to assign noise (random function at every time step) to nodes of lower priority and see how much noise can ncfs buffer and are ncfs optimal at 
buffering noise compared to ising. My guess it is. 

First I've to figure out how to update via truth table. That would be storing 2^n enteries holy shit.
Okay, so biologial networks tend to have lesser number of inputs indivisually so I can create truth tables. I think for an n input, I can create a n+1 matrix having 1s and 0s with last entry capturing the output for the n enteries before that. 


'''
import random


def reproduce(li):
    #This should make a copy of all the elements of the list and add 0 or 1 at the end of it
    for i in range(0,len(li)):
        buff=li[i].copy()
        buff.append(1)
        li[i].append(0)
        li.append(buff)
        
    return(li)



def input_space(n):
    #This function writes down the input space for n inputs
    inputs=[[]]    
    for i in range(0,n):
        reproduce(inputs)
    return(inputs)



def random_truth(n):
    #this function creates a random truth table with n inputs.
    inputs=input_space(n)

    for i in inputs:
        i.append(random.choice([0,1]))
    return(inputs)



