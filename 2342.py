n = int(input())
l = [x for x in input().split()]
f,r = 0,0
if l[1]=='+':
  f = 1
if f==1:
  if (int(l[0]) + int(l[2])) > n:
    print('OVERFLOW')
  else:
    print('OK')
else:
  if (int(l[0]) * int(l[2])) > n:
    print('OVERFLOW')
  else:
    print('OK')