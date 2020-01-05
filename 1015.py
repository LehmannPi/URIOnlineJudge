P1 = [float(i) for i in input().split()]
P2 = [float(i) for i in input().split()]
print("{:.4f}".format(((P1[0]-P2[0])**2 + (P1[1]-P2[1])**2)**(1/2)))