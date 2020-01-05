n = [int(i) for i in input().split()]
if n[0]<n[1]:
  print('O JOGO DUROU {} HORA(S)'.format(n[1]-n[0]))
else:
  print('O JOGO DUROU {} HORA(S)'.format(abs(n[0]-24)+n[1]))