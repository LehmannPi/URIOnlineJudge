n = [float(i) for i in input().split()]
m = (n[0]*2 + n[1]*3 + n[2]*4 + n[3])/10
print('Media: {:.1f}'.format(m))
if m>=7:
  print('Aluno aprovado.')
elif m<5:
  print('Aluno reprovado.')
else:
  print('Aluno em exame.')
  e = float(input())
  print('Nota do exame: {:.1f}'.format(e))
  m = (m+e)/2
  if m>=5:
    print('Aluno aprovado.')
    print('Media final: {:.1f}'.format(m))
  else:
    print('Aluno reprovado.')
