l = (int(input()))
mode = input()
matriz = []
for i in range(12):
  lista = []
  for j in range(12):
    lista.append(float(input()))
  matriz.append(lista)
s=0
for i in range(len(matriz[l])):
  s += matriz[l][i]
if mode == 'S':
  print('{:.1f}'.format(s))
else:
  print('{:.1f}'.format(s/12))