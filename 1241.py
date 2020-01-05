for i in range(int(input())):
  x = input().split()
  if x[1] == x[0][-(len(x[1]))::1]:
    print('encaixa')
  else:
    print('nao encaixa')