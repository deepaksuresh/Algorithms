#small: 2493893
#from time import time as clock
from collections import defaultdict
class item(object):
    def __init__(self,val,weight):
        self.val = val
        self.weight = weight
    def get_weight(self):
        return self.weight
    def get_value(self):
        return self.val
def make_items():
    W=0
    N=0
    items = []
    count =0
    with open('small.txt') as f:
        for line in f:
            if count==0:
                W,_ = line.split()
                W= int(W)
                count+=1
                continue
            else:
                v,w = line.split()
                v,w = int(v),int(w)
                items.append(item(v,w))
    return sorted(items,key = lambda x:x.get_weight()),W

def find_optimal(items,W):
    num=set([])
    A = {(0,i):0 for i in range(W+1)}
    #A=defaultdict(lambda :0)
    for it_num in range(1,len(items)+1):
        it_val,it_weight = items[it_num-1].get_value(),items[it_num-1].get_weight()
        for weight in range(W+1):
            if it_weight > weight:
                A[(it_num,weight)] = A[(it_num-1,weight)]
            else:
                without_item = A[(it_num-1,weight)]
                with_item = A[(it_num-1,weight-it_weight)]+it_val
                if with_item>without_item:
                    A[(it_num,weight)] = with_item
                    num.add(it_num)
                else:
                    A[(it_num,weight)] = without_item
        for weight in range(W+1):
            A.pop((it_num-1,weight),None)
        print len(num)
    print A[(it_num,W)]
    
if __name__=='__main__':
    items,W = make_items()
    print W,len(items)
    
    find_optimal(items,W)

def rec(items,W,N):
    A= defaultdict(lambda :0)
    def rec_kanp(i,w):
        if (i,w) in A:
            return A[(i,w)]
        else:
            return 
