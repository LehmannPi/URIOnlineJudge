for i in range(int(input())):
	n = [int(j) for j in input().split()]
	while n[1]:
		n[0], n[1] = n[1],n[0]%n[1]
	print(n[0])