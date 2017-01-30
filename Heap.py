class heap():
    ''' Min-Heap'''
    def __init__(self,G):
        self.list=[0] #to ease dealing with indices, an arbitrary value at index 0
        self.pos={} #holds position of elements with respect to list
        self.G = G #Graph, contains the score for each element in G[element][2]
        
    def percUp(self): #percolate up, called by insert method
        start = len(self.list)-1
        while start//2>0:
            if self.G[self.list[start/2]][1] > self.G[self.list[start]][1]:
                self.list[start/2],self.list[start] = self.list[start],self.list[start/2]
            start = start//2
    
    def insert(self,element):
        self.list.append(element)
        self.percUp()
        self.update_pos()

    def percDown(self,start=1): #percolate down, called by extract_min method
        while 2*start < len(self.list):
            min_ind = self.getMinInd(start)
            if self.G[self.list[start]][1] > self.G[self.list[min_ind]][1]:
                self.list[start],self.list[min_ind] = self.list[min_ind],self.list[start]
            start = min_ind

    def extract_min(self):
        small = self.list.pop(1)
        self.percDown()
        self.update_pos()
        return small
 
    def delete(self,pos):
        del self.list[pos]
        self.percDown(pos)

    def getMinInd(self,start):
        if 2*start+1 > len(self.list)-1:
            return 2*start
        else:
            if self.G[self.list[2*start]][1]<self.G[self.list[2*start+1]][1]:
                return 2*start
            else:
                return 2*start+1
            
    def update_pos(self):
        self.pos = {}
        for i in xrange(1,len(self.list)):
            self.pos[self.list[i]]=i
