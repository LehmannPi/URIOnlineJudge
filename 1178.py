l =[float(input())]
for i in range(99):
  l.append(l[i]/2)
for i in range(len(l)):
  print('N[{}] = {:.4f}'.format(i,l[i]))