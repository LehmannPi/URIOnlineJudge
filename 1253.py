ciph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(int(input())):
  w = input()
  s = int(input())
  x = ''
  for j in range(len(w)):
    x += ciph[(ciph.index(w[j]) - s) % 26 ]
  print(x)
