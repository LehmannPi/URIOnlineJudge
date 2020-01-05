i=1
for j in range(7,16,2):
  for k in range(j,j-3,-1):
    print('I=%d J=%d'%(i,k))
  i+=2