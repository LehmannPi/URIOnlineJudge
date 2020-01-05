N = [float(i) for i in input().split()]
C = N.copy()
C.sort()
if C[0]+C[1]<=C[2]:
  print('Area = {:.1f}'.format((N[0]+N[1])*N[2]/2))
else:
  print('Perimetro = {}'.format(sum(N)))