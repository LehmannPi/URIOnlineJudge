n = int(input())
a = n//365
r = n%365
m = r//30
r = r%30
d = r
print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(a,m,d))