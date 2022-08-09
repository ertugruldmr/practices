import numpy

N,M,P =map(int,input().split())

N_list=[]
for _ in range(N):
    N_list.append(list(map(int,input().split())))
M_List=[]
for _ in range(M):
    M_List.append(list(map(int,input().split())))
print(numpy.concatenate( (N_list,M_List) ,axis=0))