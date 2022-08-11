import numpy
N,M = map(int, input().split() )

matrix=[]
for _ in range(N):
    matrix.append(list(map(int,input().split())))
N_matrix=numpy.array(matrix)
Sum=numpy.sum(N_matrix,axis=0)
print(numpy.prod(Sum))
