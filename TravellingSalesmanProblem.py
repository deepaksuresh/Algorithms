import numpy as np
from itertools import combinations as comb
from collections import defaultdict
def points(filename):
    cities={}
    count=1
    a=0
    with open(filename) as f:
        for line in f:
            if a==0:
                a+=1
                continue###DELETE THIS####
            x,y=map(lambda x:round(float(x),2),line.split())
            city=np.array([x,y])
            cities[count]=city
            count+=1
    return cities
def make_set():
    cities = range(2,26)
    for i in range(1,25):
        subs = comb(cities,i)
        for j in subs:
            j=set(j)
            j.add(1)
            yield j
def distances(cities):
    dist={}
    for i in cities:
        for j in cities:
            if i!=j:
                dist[frozenset((i,j))]=round(np.linalg.norm(cities[i]-cities[j]),2)
    return dist
def tsp(cities):
    final=defaultdict(lambda : float('inf'))
    final[(frozenset([1]),1)]=0
    subsets = make_set()
    for S in subsets:
        for j in S:
            if j!=1:
                for k in S:
                    if k!=j:
                        sp=set(S)
                        sp.remove(j)
                        final[(frozenset(S),j)]=min(final[(frozenset(S),j)],
                                                    final[(frozenset(sp),j)]+\
                                                    round(np.linalg.norm(cities[j]-cities[k]),2))
    
