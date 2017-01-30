#create defaultdict representation of graph
#run dfs on reversed graph
#run dfs on graph, in the order of dinishing times

from time import time as clock
#read file and return a graph
#txt -> defaultdict
from collections import defaultdict
from collections import OrderedDict
def makeGraph(files):
    G = defaultdict(lambda:[[],[]]) #0th for head, 1 for tail vertices
    for i in files:
        with open(i) as graphRep:
            for line in graphRep:
                tail,head = line.split()
                tail,head = int(tail),int(head)
                G[tail][0].append(head)
                G[head][1].append(tail)
    return G
##
##if __name__ == '__main__':
##    makeGraph('s.txt')

#defaultdict(a graph) -> OrderedDict(ordered according to finishing time)\
#create dict by performing dfs on reversed dict
def dfs_main(G):
    Order = []
    toVisit = []
    visited = set()
    for vert in range(1,len(G.keys())+1):
        if vert not in visited:
            dfs_first(G,vert,Order,visited)
    return Order

def dfs_first(G,vert,Order,visited):
    toVisit = [vert]
    while len(toVisit)>0:
        
        nextNode = toVisit[-1]
        #print toVisit,visited,nextNode,G[nextNode][1]
        if G[nextNode][1] == []:
            #print "here"
            visited.add(nextNode)
            v = toVisit.pop()
            Order.insert(0,v)
        else:
            visited.add(nextNode)
            for i in G[nextNode][1]:
                if i not in visited:
                    visited.add(i)
                    toVisit.append(i)
            G[nextNode][1] = []
    #Order.insert(0,vert)
    return

#G=makeGraph('C:\Users\deepak.suresh\Desktop\s.txt')
#n = dfs_main(G)
def dfs_main1(G,order):
    scc = defaultdict(int)
    toVisit = []
    visited = set()
    for vert in order:
        if vert not in visited:
            dfs_sec(G,vert,scc,visited)
    return scc

def dfs_sec(G,lead,scc,visited):
    toVisit = [lead]
    scc[lead] +=1
    while len(toVisit)>0:
        nextNode = toVisit[-1]
        if G[nextNode][0] == []:
            visited.add(nextNode)
            toVisit.pop()
        else:
            visited.add(nextNode)
            for i in G[nextNode][0]:
                if i not in visited:
                    scc[lead] +=1
                    visited.add(i)
                    toVisit.append(i)
            G[nextNode][0] = []
    #Order.insert(0,vert)
    return
def main():
    initial = clock()
    G = makeGraph(['xaa.txt','xab.txt','xac.txt'])
    print "building graph took ",clock()-initial," seconds"
    order_start = clock()
    #G = makeGraph(['my.txt'])
    n = dfs_main(G)
    order_finish = clock()
    print "ordering took ",order_finish-order_start," seconds"
    sccs = dfs_main1(G,n)
    mid= clock()
    print sorted(sccs.values(),reverse=True)[:15]
    final = clock()
    print "SCC took ",mid-order_finish, " seconds"
    
if __name__ == '__main__':
    main()

