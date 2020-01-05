i,s=[],0
i.append(int(input()))
i.append(int(input()))
i.sort()
for x in range(i[0]+1,i[1]):
  if x%2==1:
    s+=x
print(s)