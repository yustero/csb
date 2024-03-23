import matplotlib.pyplot as plt
import pandas as pd
import boolean_sim

def scatter_show(x,y, xname,yname,title, name):
    fig = plt.figure(figsize = (10, 5))
    plt.scatter(x,y, alpha=0.5, color="r")
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.title(title)
    fig.autofmt_xdate()
    plt.show()
    









def scatter_save(x,y, xname,yname,title, name):
    fig = plt.figure(figsize = (10, 5))
    plt.scatter(x,y, alpha=0.5, color="r")
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.title(title)
    fig.autofmt_xdate()
    plt.savefig("{}.png".format(name))
    print("done")




def hist_save(data,xname,title,name):
    fig = plt.figure(figsize = (10, 5))
    plt.hist(data, alpha=0.5, color="g")
    plt.xlabel(xname)
    plt.ylabel("Frequencies")
    plt.title(title)
    fig.autofmt_xdate()
    plt.savefig("{}.png".format(name))
    print("done")


def hist_show(data,xname,title,name):
    fig = plt.figure(figsize = (10, 5))
    plt.hist(data, alpha=0.5, color="g")
    plt.xlabel(xname)
    plt.ylabel("Frequencies")
    plt.title(title)
    fig.autofmt_xdate()
    plt.savefig("{}.png".format(name))
    print("done")


def save_csv(data, column, name):
    df=pd.DataFrame(data,columns=column)
    df.to_csv("{}.csv".format(name), index=False)
    print("done")

