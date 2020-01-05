inp,l = int(input()),[]
while inp != 0:
  l.append(int(inp))
  inp = int(input())
for i in range(len(l)):
  print('1', end='')
  for j in range(l[i]-1):
    print(' %d'%(j+2), end='')
  print('')