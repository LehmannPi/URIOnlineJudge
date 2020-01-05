l = [int(i) for i in input().split()]
while(0 not in l):
  ev1,ev2,at,d=l[0],l[1],l[2],l[3]
  n1 = round(ev1/d+0.49)
  n2 = round(ev2/d+0.49)
  if at == 3:
    r = n1/(n1+n2)
  else:
    p = at/6
    q = 1 - p
    r = (1- (q/p)**n1)/(1- (q/p)**(n1+n2))
  print('{:.1f}'.format(r*100))
  l = [int(i) for i in input().split()]
  
# Sample unfair case:
''' p = 1/6
q = 1 - p
n1 = 1
n2 = 2
r = (1- (q/p)**n1)/(1- (q/p)**(n1+n2))
print('{:.1f}'.format(r*100)) '''
# Explanation: https://en.wikipedia.org/wiki/Gambler%27s_ruin