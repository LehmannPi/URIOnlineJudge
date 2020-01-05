n=float(input())
c100,r = n//100,n%100
c50 = r//50
r = r%50
c20 = r//20
r = r%20
c10 = r//10
r = r%10
c5 = r//5
r = r%5
c2 = r//2
r = r%2
m1 = r//1
r = r%1
m50 = r//0.50
r = r%0.50
m25 = r//0.25
r = r%0.25
m10 = r//0.10
r = r%0.10
m05 = r//0.05
r = r%0.05
m01 = (r+0.001)//0.01

print('NOTAS:\n{:.0f} nota(s) de R$ 100.00\n{:.0f} nota(s) de R$ 50.00\n{:.0f} nota(s) de R$ 20.00\n{:.0f} nota(s) de R$ 10.00\n{:.0f} nota(s) de R$ 5.00\n{:.0f} nota(s) de R$ 2.00\nMOEDAS:\n{:.0f} moeda(s) de R$ 1.00\n{:.0f} moeda(s) de R$ 0.50\n{:.0f} moeda(s) de R$ 0.25\n{:.0f} moeda(s) de R$ 0.10\n{:.0f} moeda(s) de R$ 0.05\n{:.0f} moeda(s) de R$ 0.01'.format(c100,c50,c20,c10,c5,c2,m1,m50,m25,m10,m05,m01))
