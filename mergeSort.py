def sort(array):
    if len(array)==1:
            return array,0
    Left,Ls= sort(array[:len(array)/2])
    Right,Rs = sort(array[len(array)/2:])
    result,s=merge(Left,Right)
    swaps = Ls+Rs+s
    return result,swaps

def merge(L,R):
    i,j,inv=0,0,0
    result=[]
    while i<len(L) and j<len(R):
        if L[i]>R[j]:
            result.append(R[j])
            j+=1
            inv+=(len(L)-i)
            
        else:
            result.append(L[i])
            i+=1
    result.extend(L[i:])
    result.extend(R[j:])
    return result,inv
