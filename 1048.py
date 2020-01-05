n = float(input())
if n<=400:
  r=0.15
elif n<=800:
  r=0.12
elif n<=1200:
  r=0.10
elif n<=2000:
  r=0.07
else:
  r=0.04
print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:.0f} %'.format(n+(n*r),n*r,r*100))