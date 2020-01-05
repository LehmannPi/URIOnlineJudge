ldNm = [6,2,5,5,4,5,6,3,7,6]

for n in range(int(input())):
  leds = 0
  for i in input():
    leds += ldNm[int(i)]
  print('{} leds'.format(leds))