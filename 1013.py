L = input().split(' ')
A = [int(i) for i in L]
B = int((A[0]+A[1]+abs(A[0]-A[1]))/2)
C = int((A[2]+B+abs(A[2]-B))/2)
print('{} eh o maior'.format(C))