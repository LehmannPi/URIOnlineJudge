n,l,s=int(input()),[],0
while(n>=0):
  l.append(n)
  s+=n
  n=int(input())
print('{:.2f}'.format(s/len(l)))