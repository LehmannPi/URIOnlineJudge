t,c,r,s = 0,0,0,0
n=int(input())
for i in range(n):
  x = input().split()
  if x[1] == 'C':
    c+= int(x[0])
  elif x[1] == 'R':
    r+= int(x[0])
  elif x[1] == 'S':
    s+= int(x[0])
t = s+r+c
cp,rp,sp = 100*c/t,100*r/t,100*s/t
print('Total: {} cobaias\nTotal de coelhos: {}\nTotal de ratos: {}\nTotal de sapos: {}'.format(t,c,r,s))
print('Percentual de coelhos: {:.2f} %\nPercentual de ratos: {:.2f} %\nPercentual de sapos: {:.2f} %'.format(cp,rp,sp))