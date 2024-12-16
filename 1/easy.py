n = 1000
a = []
b = []
ans = 0

for i in range(n):
	x,y  = map(int, input().split())
	a.append(x)
	b.append(y)

a.sort()
b.sort()

for i in range(n):
	if a[i]-b[i] < 0:
		ans+= b[i]-a[i]
	else:
		ans += a[i]-b[i]

print(ans)