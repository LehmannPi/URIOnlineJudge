n = int(input())
for i in range(n):
  sum=0
  a = [int(x) for x in input().split()]
  if a[0]>a[1]:
    inc = -1
    a[0] -= 1
  else:
    inc = 1
    a[0] += 1
  for j in range(a[0],a[1],inc):
    if j%2==1:
      sum+=j
  print(sum)