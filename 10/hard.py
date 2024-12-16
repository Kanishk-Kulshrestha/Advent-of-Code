a = []
ans = 0

def track(i,j,v):
	r = 0
	if v==9:
		return 1
	if i+1<n and int(a[i+1][j])==v+1:
		r += track(i+1,j,v+1)
	if j+1<m and int(a[i][j+1])==v+1:
		r += track(i,j+1,v+1)
	if i-1>=0 and int(a[i-1][j])==v+1:
		r += track(i-1,j,v+1)
	if j-1>=0 and int(a[i][j-1])==v+1:
		r += track(i,j-1,v+1)
	return r


while(1):
	inp = input()
	if inp=="":
		break
	a.append(inp)

n = len(a)
m = len(a[0])

for i in range(n):
	for j in range(m):
		if a[i][j]=='0':
			ans += track(i,j,0)
			

print(ans)

