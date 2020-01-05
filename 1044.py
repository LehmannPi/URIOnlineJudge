N = [int(i) for i in input().split()]
N.sort()
if N[1]%N[0] == 0:
  print("Sao Multiplos")
else:
  print("Nao sao Multiplos")