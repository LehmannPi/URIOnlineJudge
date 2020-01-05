A = [int(i) for i in input().split()]
if(A[1]>A[2] and A[3]>A[0] and A[3]+A[2]>A[0]+A[1]):
  print('Valores aceitos')
else:
  print('Valores nao aceitos')