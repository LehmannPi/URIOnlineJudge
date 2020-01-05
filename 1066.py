p,imp,pos,neg = 0,0,0,0
for i in range(5):
  n = int(input())
  if n<0:
    neg+=1
  elif n>0:
    pos+=1
  if n%2==0:
    p+=1
  elif n%2==1:
    imp+=1
print('{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)'.format(p,imp,pos,neg))