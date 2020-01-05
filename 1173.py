a,p = [],0
a.append(int(input()))
for i in range(0,9):
  a.append(a[i]*2)
for i in a:
  print('N[{}] = {}'.format(p,i))
  p+=1