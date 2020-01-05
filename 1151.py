l,r = [0,1],int(input())
print('0 1', end= '')
if r!=1:
  for i in range(2,r):
    s=0
    s = l[i-1]+l[i-2]
    l.append(s)
    print(' {}'.format(s), end='')
  print('')