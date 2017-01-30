class Queue(object):
    def __init__(self,elements):
        self.elements = elements
    def add(self,e):
        self.elements.append(e)
    def eject(self):
        return self.elements.pop(0)
    def __len__(self):
        return len(self.elements)

class Stack(object):
    def __init__(self,elements):
        self.elements = elements
    def add(self,e):
        self.elements.append(e)
    def eject(self):
        return self.elements.pop()
    def __len__(self):
        return len(self.elements)


class Puzzle(object):
    def __init__(self,state, lastMove):
        self.state = state
        self.lastMove=lastMove
        self.end = len(self.state)
        self.n = int(self.end**.5)
        self.zeroPos = self.state.index(0)
        
    def isSolved(self):
        if self.zeroPos==0:
            if self.state[1:]==range(1,self.end):
                return True
        if self.zeroPos==self.end-1:
            if self.state[0:-1]==range(1,self.end):
                return True
        return False
    
    def getMoves(self):
        moves=['U','D','L','R']
        if self.zeroPos<self.n:
            moves.remove('U')
        if self.zeroPos>=self.end-self.n:
            moves.remove('D')
        if self.zeroPos%self.n==0:
            moves.remove('L')
        if (self.zeroPos+1)%self.n==0:
            moves.remove('R')
        for move in moves:yield move

    def newNodes(self):
        moves = self.getMoves()
        newPuzzles=[]
        for move in moves:
            newPuzzles.append(self.performMove(move))
        return newPuzzles
    
    def performMove(self, move):
        if move=='U':
            newState=self.state[:]
            newState[self.zeroPos],newState[self.zeroPos-self.n]=newState[self.zeroPos-self.n],newState[self.zeroPos]
            return Puzzle(newState,'U')
            
        if move=='D':
            newState=self.state[:]
            newState[self.zeroPos],newState[self.zeroPos+self.n]=newState[self.zeroPos+self.n],newState[self.zeroPos]
            return Puzzle(newState,'D')
            
        if move=='L':
            newState=self.state[:]
            newState[self.zeroPos],newState[self.zeroPos-1]=newState[self.zeroPos-1],newState[self.zeroPos]
            return Puzzle(newState,'L')
            
        if move =='R':
            newState=self.state[:]
            newState[self.zeroPos],newState[self.zeroPos+1]=newState[self.zeroPos+1],newState[self.zeroPos]
            return Puzzle(newState,'R')

    def toString(self):
        return ''.join(map(str,self.state))


def buildPath(final,explored):
    path=[]
    last_move=final.lastMove
    while(last_move!=''):
        if last_move=='U':
            path.insert(0,'Up')
            previous_state = final.performMove('D')
            last_move = explored[previous_state.toString()]
            final = previous_state
            continue
        if last_move=='D':
            path.insert(0,'Down')
            previous_state = final.performMove('U')
            last_move = explored[previous_state.toString()]
            final = previous_state
            continue
        if last_move=='L':
            path.insert(0,'Left')
            previous_state = final.performMove('R')
            last_move = explored[previous_state.toString()]
            final = previous_state
            continue
        if last_move=='R':
            path.insert(0,'Right')
            previous_state = final.performMove('L')
            last_move = explored[previous_state.toString()]
            final = previous_state
            continue
    return path

def bfs(tree):
    explored={}
    while (len(tree)>0):
        node = tree.eject()
        explored[node.toString()]=node.lastMove
        if node.isSolved():
            print buildPath(node,explored)
            print node.state
            return True
        else:
            new_Nodes= node.newNodes()
            for i in new_Nodes:
                if i.toString() not in explored:
                    tree.add(i)

def dfs(tree):
    explored={}
    frontier=set([])
    frontier.add(tree.elements[0].toString())
    while (len(tree)>0):
        node = tree.eject()
        nodeStr=node.toString()
#        print nodeStr
##        frontier.remove(nodeStr)
##        for i in tree.elements:
##            print i.toString(),
##        print '\n'
        explored[node.toString()]=node.lastMove
        new_Nodes= node.newNodes()
        new=[]
        for i in new_Nodes:
            strNode = i.toString()
            if strNode not in (frontier and explored):
                new.append(i)
                frontier.add(strNode)
        for i in new[::-1]:
            tree.add(i)
        if node.isSolved():
            print buildPath(node,explored)
            return

def main():
    puzzle=Puzzle([1,2,5,3,4,0,6,7,8],'')
    tree = Stack([puzzle])
    dfs(tree)

if __name__=='__main__':
    main()
