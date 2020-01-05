R = input().split(" ")

L = []
for item in R:
  L.append(float(item))

A = (L[0]*L[2]/2)
B = (3.14159*L[2]**2)
C = ((L[0]+L[1])*L[2]/2)
D = (L[1]**2)
E = (L[0]*L[1])
print("TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}".format(A,B,C,D,E))