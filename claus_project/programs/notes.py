'''
Now for starters I intend to create completely nested canalizing functions for each node in the following manner:
For lets say node n, we create a random priority list for all the nodes leading into it. Now we allow only two states 1/0 to exist. 
now the nodes could be classified into two, the one in the same team and the one in the other team.

To decide the updated state of the node, we go through the priority order, 
if the first node is having state 1 and it's in the same team, we set the state of the node to be 1. 
if first node has state 0 , we move on to second node, if it has state 1 and if its in other team we set state to be 0, if its in the same team we set the state to be 1. 
... so on till the last node. If the last node has state 0, we don't change anything. 

How could this be implemented? 
For each node we could create few lists, one having the names of all the nodes having edges into it, 
one having a priority sequence, one having the information of which team they're in. We could store the functions externally. 





The scoring scheme?

If the node is in t1 and has state 1, score +=1
If the node is in t1 and has state 0, score+= -1

If the network is in t2 and has state 1, score += -1
If the network is in t2 and has state 0, score += 1

The final score is the absolute value of this score. 



For completely nested canalizing functions i.e all the nodes connected to the given node are canalizing. 

Instead of setting the state to 1 upon a 1 input incase of activating connection, we can set the state to 0 upon a 0 input incase of positive connection and 1 incase of negative connection as well.


#Talking with kishore, I need to change the scoring scheme such that I do not penalize the score if member from the same team is out of sync with the team. 
And I need to allow more than one node in the same layer. What does it mean? Are the two nodes in the same layer connected by an AND function? If they're connected by an OR function then isn't it the same as nested canalizing when they're immediate neighbors? 


Some wild ideas about assigning priority order: By out degree. This preserves some universality. But what about fully connected network? 

I was also thinking of having layers with one input from the same team and one input from the other team, if we could somehow figure out what having the same "layer" means. 



#Ways of assigning priorities changes dynamics. 

For a given node, if we assign higher priority to nodes from the same team having inputs to that node and if we do it for all nodes, I think it might result in unideal outcomes (1,1) states. 
It feels like if ncfs, if "arranged" properly can meet different goals.  



-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#In different dynamics, I try to address the question of how giving priority differently to nodes results in different kinds of steady states. 

    1. More priority to nodes in the same team/other team (based on outdegree/random)
    2. Priorities alternating between nodes of two different teams ( Two cases: Highest priority from same team/other team)
    3. Have to check priority based on indegree
    4. In biological networks however, with impure edges. It is not straightforward to order the networks by outdegree. 


---------------------------
Some question: If you have a network with no connections then the steady states are all the input states but does having a few connections reduce the steady states? Yes, looks that way. But to what extent? 
---------------------------
https://www.ias.ac.in/article/fulltext/jbsc/047//0017
Think about unateness/motonicity. Can we maintain just that and still get bimodal solutions?
    1. Essentiality of input
    2. We could try using link operator functions and see what we get
    3. Collectively canalizing: Few variables' input determines state instead of one?
    4. How are NCFs in this paper not collectively canalizing? Aren't NCFs subset of collectively canalizing functions?
    5. "A k-input BF is said to be ‘collectively canalyzing’ if by fixing a certain subset of i inputs (such that 1\ i \ k), the output of the function is determined (Reichhardt and Bassler 2007), while it is not when fixing fewer than i inputs."
    6. Collectively canalizing functions can be interesting because they might be somewhat related to some "threshold" of nodes being active. 
    7. NCFs offering some kind of small world network like robustness wrt nodes of low priority having random boolean functions. 
    8. "The dominance of AND-NOT LOFs in the dataset implies that regulatory logic is primarily governed by a special type of veto mechanism wherein the presence of a single inhibitor determines the output of the gene" What mate.     
        1. "the activators can function only in the absence of the inhibitors, and the vetoing power of all the inhibitors is the same"
    9. 
'''

