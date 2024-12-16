n = 1000
a = []
b = []
ans = 0

for i in range(n):
	x,y  = map(int, input().split())
	a.append(x)
	b.append(y)

c = {}

for i in b:
	if i in c:
		c[i]+=1
	else:
		c[i]=1

ans = 0

for i in a:
	if i in c:
		ans+=i*c[i]

print(ans)