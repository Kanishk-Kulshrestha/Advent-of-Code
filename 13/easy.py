def take(op):
	inp = input()
	if inp=="q":
		quit()
	a = inp.split(':')[1]
	a = a.split(',')
	a = [x.split(op) for x in a]
	a = list(map(int, [x[1] for x in a]))
	return a

ans = 0

for _ in range(320):
	a = take('+')
	# print(a)
	b = take('+')
	# print(b)
	p = take('=')
	# print(p)
	input()

	n = min(p[0]//b[0], p[1]//b[1])
	# print(n)
	for i in range(n):
		if (p[0]-b[0]*(n-i))%a[0]==0 and (p[1]-b[1]*(n-i))%a[1]*i==0 and (p[0]-b[0]*(n-i))//a[0]==(p[1]-b[1]*(n-i))//a[1]:
			ans += (n-i) +  ((p[0]-b[0]*(n-i))//a[0])*3
			
print(ans)