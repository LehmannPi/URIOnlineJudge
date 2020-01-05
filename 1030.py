y=[]
for i in range(int(input())):
  n = [int(j) for j in input().split()]
  l = [k+1 for k in range(n[0])]
  c = 0
  while len(l) != 1:
    c = (c+(n[1]-1))%len(l)
    l.pop(c)
  y.append(l[0])
for i in range(len(y)):
  print('Case {}: {}'.format(i+1,y[i]))