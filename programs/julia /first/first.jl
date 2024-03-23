using Random
using Plots

function random_intputs(n)
    output=Array{Int64}(undef, n)
    val=[1,-1]

    for i in 1:n
        output[i]=rand(val)
    end
return(output)

end

function evol( input, pos, adj)
    n=size(input)[1]
    
    adjsum=0
    
    output=copy(input)
    
    for i in 1:n
    adjsum+=adj[i,pos]* input[i]

    end

    if adjsum>0
        output[pos]=1
    elseif adjsum<0
        output[pos]=-1
    elseif adjsum==0
        output[pos]=output[pos]
    end

    return(output)

end


function steady_check(input,adj)

    n=size(input)[1]
    counter=0

    for i in 1:n
        if evol(input,i,adj)[i]!=input[i]
        counter+=1
        end
    end

    if counter>0
        return(false)
    elseif counter==0
        return(true)
    end
end
adj=[1 1 -1 -1; 1 1 -1 -1 ; -1 -1 1 1 ; -1 -1 1 1 ]

input = [1 1 -1 -1]


function steady_states(adj,no_sim)
n=size(adj)[1]

steadys=[]

    for i in 1:no_sim
        input=random_intputs(n)
        t=0

        while true
        rn=rand(1:n)
        out=evol(input,rn,adj)
        
        if steady_check(out,adj)
            push!(steadys,out)
            t+=1
            break
        else
            input=out
            t+=1
        end
        
        if t>1000
        break
        end
        
    
        end


    end

    return(steadys)
end


function steady_state_frequency(steady_states,adj)


    n=size(adj)[1]
    ssf=[[],[]]

    for i in steady_states
        if !(i in ssf[1])
        push!(ssf[1],i)
        push!(ssf[2],1)
        end
        
        if i in ssf[1]
        inde=findfirst(item-> item == i, ssf[1])
        ssf[2][inde]+=1
        end 
    
    end


    return(ssf)
end

println(  steady_state_frequency(    steady_states(adj,1000)     ,adj)  )