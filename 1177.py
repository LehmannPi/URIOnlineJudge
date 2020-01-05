j,l,n=0,[],int(input())
for i in range(1000):
  l.append(j)
  j = (1+j)%n
  print('N[{}] = {}'.format(i,l[i]))