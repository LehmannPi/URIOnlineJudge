p = float(input())
if p <= 2000:
  print('Isento')
elif p > 2000 and p <= 3000:
  print('R$ {:.2f}'.format((p-2000)*0.08))
elif p > 3000 and p <= 4500:
  print('R$ {:.2f}'.format((1000)*0.08+(p-3000)*0.18))
elif p > 4500:
  print('R$ {:.2f}'.format((1000)*0.08+(1500)*0.18+(p-4500)*0.28)) 
