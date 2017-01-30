from collections import defaultdict
from h import *
from copy import deepcopy as c
def make_graph(filename):
    G = defaultdict(lambda:[{},float('inf')])
    count =0
    with open(filename) as f:
        for line in f:
            if count ==0:
                count += 1
                continue
            else:
                start,end,weight = line.split()
                start = int(start)
                end = int(end)
                weight = int(weight)
                G[start][0][end] = weight
                G[end][0][start] = weight
                count += 1
    return G

def prim(G,i):
    ''' Performs Prim's algorithm on a given graph
        Input: Graph G, as defaultdict with attributes [[ends of edges],[weights],score]
        Output: The minimum cost of spanning tree'''
    weighted_sum =0
    parent ={}
    vertHeap = heap(G)
    vertHeap.G[i][1]=0 #start at vertex 1, setting cost to zero
    vertHeap.insert(i) #adding vertices to heap
    visited = set([])
    while len(vertHeap.list)>1:
        root = vertHeap.extract_min() #extracting vertex with min score
        weighted_sum += vertHeap.G[root][1] #update score
        visited.add(root)
        for child,weight in vertHeap.G[root][0].items():
            if child not in visited:
                if child in vertHeap.pos:
                    pos = vertHeap.pos[child]
                    vertHeap.delete(pos)
                vertHeap.G[child][1] = min(vertHeap.G[child][1],weight)
                vertHeap.insert(child)
    print weighted_sum
    
def main():
    G = make_graph('edges.txt')
    prim(G,25)


if __name__ == '__main__':
    main()
