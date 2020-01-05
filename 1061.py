d0 = int((input().split())[1])
t0 = list(map(int,input().split(':')))
t0 = t0[0]*3600+t0[1]*60+t0[2]
d1 = int((input().split())[1])
t1 = list(map(int,input().split(':')))
t1 = t1[0]*3600+t1[1]*60+t1[2]
ex,c=0,0
if t1-t0 < 0:
  c=-1
  t = 24*3600-t0+t1
else:
  t = t1-t0
#transformação seg to h/m/s
d = d1-d0+c
h = (t//3600)
m = (t%3600)//60
s = (t%3600)%60
print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(d,h,m,s))