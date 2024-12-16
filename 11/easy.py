a = list(map(int, input().split()))

for _ in range(25):
	res = []
	for i in a:
		if i==0:
			res.append(1)
		elif len(str(i))%2==0:
			res.append(int(str(i)[:len(str(i))//2]))
			res.append(int(str(i)[len(str(i))//2:]))
		else:
			res.append(i*2024)

	a = res

print(len(res))