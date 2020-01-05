m,c=0,0
for i in range(6):
  n = float(input())
  if(n>=0):
    m+=n
    c+=1
print('%d valores positivos\n%.1f'%(c,m/c))