sum = 0
n = [int(int(input())) for i in range(2)]
n.sort()
for i in range(n[0],n[1]+1):
  if i%13!=0:
    sum += i
print(sum)