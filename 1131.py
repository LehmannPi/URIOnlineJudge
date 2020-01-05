cg,cit,emp,cnt,flag = 0,0,0,0,1 #1 sim,2 nao
ganhador = ''
while flag==1:
  n = [int(i) for i in input().split()]
  if n[0] > n[1]:
    cit += 1
  elif n[0] < n[1]:
    cg += 1
  else:
    emp += 1
  cnt += 1
  print( 'Novo grenal (1-sim 2-nao)')
  flag = int(input())
if cg<cit:
  ganhador = 'Inter venceu mais'
elif cg>cit:
  ganhador = 'Gremio venceu mais'
else:
  ganhador = 'Nao houve vencedor'
print('{} grenais\nInter:{}\nGremio:{}\nEmpates:{}\n{}'.format(cnt,cit,cg,emp,ganhador))
