def swap(lis,pos1,pos2):
    temp=lis[pos1]
    lis[pos1]=lis[pos2]
    lis[pos2]=temp
    return lis


List = [12, 35, 9, 56, 24]
print(swap(List,1,3))