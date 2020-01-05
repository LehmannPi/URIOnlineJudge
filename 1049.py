#estrutura: l[0]; classe: l[1]; habitos_alimentares: l[2]
l = []
for i in range(3):
  l.append(input())
if l[0] == 'vertebrado':
  if l[1] == 'ave':
    if l[2] == 'carnivoro':
      print('aguia')
    else:
      print('pomba')
  else:
    if l[2] == 'onivoro':
      print('homem')
    else:
      print('vaca')
else:
  if l[1] == 'inseto':
    if l[2] == 'hematofago':
      print('pulga')
    else:
      print('lagarta')
  else:
    if l[2] == 'hematofago':
      print('sanguessuga')
    else:
      print('minhoca')
