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
	p[0] += 10000000000000
	p[1] += 10000000000000
	# print(p)
	input()

	n = min(p[0]//b[0], p[1]//b[1])
	# print(n)
	x = round(((a[0]/a[1])*p[1]-p[0])/((a[0]/a[1])*b[1]-b[0]))
	y = round((p[1]-b[1]*x)/a[1])
	print(x,y)
	if p[0]==a[0]*y+b[0]*x and p[1]==a[1]*y+b[1]*x:
		ans+=y*3+x
print(ans)