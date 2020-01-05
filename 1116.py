for i in range(int(input())):
  d=[int(i) for i in input().split()]
  if d[1]==0:
    print('divisao impossivel')
  else:
    print(d[0]/d[1])