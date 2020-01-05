n = int(input())
s = n%60
m = int((n/60)%60)
h = int((n/60)/60)
print('{}:{}:{}'.format(h,m,s))