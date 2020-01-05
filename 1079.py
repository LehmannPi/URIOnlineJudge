n = int(input())
for i in range(n):
  x = [float(j) for j in input().split()]
  print('{:.1f}'.format((2*x[0]+3*x[1]+5*x[2])/10))