import numpy

N,M =  map(int,input().split())
l=[]
for _ in range(N):
    l.append(list(map(int,input().split())))
arr=numpy.array(l)  
print(numpy.max(numpy.min(arr,axis=1)))