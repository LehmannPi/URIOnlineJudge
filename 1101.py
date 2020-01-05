n = [int(i) for i in input().split()]
while not n[0]<=0 and not n[1]<=0:
  n.sort()
  sum = 0
  for i in range(n[0],n[1]+1):
    print(i, end = ' ')
    sum += i
  print('Sum={}'.format(sum))
  n = [int(i) for i in input().split()]