I = [float(i) for i in input().split()]
try:
  R1 = (-I[1] + (I[1]**2 -4*I[0]*I[2])**(1/2))/(2*I[0])
  R2 = (-I[1] - (I[1]**2 -4*I[0]*I[2])**(1/2))/(2*I[0])
  if(type(R1) is complex):
    print("Impossivel calcular")
  else:
    print('R1 = {:.5f}\nR2 = {:.5f}'.format(R1,R2))
except:
  print("Impossivel calcular")
