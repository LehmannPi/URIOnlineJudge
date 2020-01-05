n = input().split()
while n[0]!='0' and n[1]!='0':
  try:
    x = (n[1].translate({ord(n[0]): None}))
    if len(x)< 10:
      x = float(x)
  except:
    x = 0
  try:
    print('{:.0f}'.format(x))
  except:
    print('{}'.format(x))
  n = input().split()