a,p = [],0
for i in range(10):
  a.append(int(input()))
l = [1 if i <= 0 else i for i in a]
for i in l:
  print('X[{}] = {}'.format(p,i))
  p+=1