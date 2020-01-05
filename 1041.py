n = [float(i) for i in input().split()]
# n = [X,Y]
if (n[0] == n[1] and n[0] == 0):
  print('Origem')
elif n[0]>0 and n[1]>0:
  print('Q1')
elif n[0]>0 and n[1]<0:
  print('Q4')
elif n[0]<0 and n[1]>0:
  print('Q2')
elif n[0]<0 and n[1]<0:
  print('Q3')
elif n[0]==0 and n[1]!=0:
  print('Eixo Y')
elif n[0]!=0 and n[1]==0:
  print('Eixo X')