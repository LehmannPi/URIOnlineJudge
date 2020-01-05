imp,par=[],[]
for i in range(15):
  x = int(input())
  if x%2==0:
    par.append(x)
  else:
    imp.append(x)
  if len(imp) >= 5:
    for i in range(5):
      print('impar[{}] = {}'.format(i,imp[i]))
    imp = []
  if len(par) >= 5:
    for i in range(5):
      print('par[{}] = {}'.format(i,par[i]))
    par = []
if imp:
  for i in range(len(imp)):
      print('impar[{}] = {}'.format(i,imp[i]))
if par:
  for i in range(len(par)):
    print('par[{}] = {}'.format(i,par[i]))