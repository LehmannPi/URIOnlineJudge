m,p=0,0
for x in range(100):
  i=int(input())
  if i>m:
    m=i
    p=x+1
print('%d\n%d'%(m,p))