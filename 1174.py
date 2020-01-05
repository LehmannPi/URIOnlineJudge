a,p = [],0
for i in range(100):
  a.append(float(input()))
for i in a:
  if i <= 10:
    print('A[{}] = {:.1f}'.format(p,i))
  p+=1