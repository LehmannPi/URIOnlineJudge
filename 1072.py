i=0
o=0
y=int(input())
for x in range(y):
  if 10<=int(input())<=20:
    i+=1
  else:
    o+=1
print('{} in\n{} out'.format(i,o))