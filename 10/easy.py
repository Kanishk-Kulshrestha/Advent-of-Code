a = []
ans = 0

def track(i,j,v):
	s = set()
	if v==9:
		return set([(i,j)])
	if i+1<n and int(a[i+1][j])==v+1:
		s = s.union(track(i+1,j,v+1))
	if j+1<m and int(a[i][j+1])==v+1:
		s = s.union(track(i,j+1,v+1))
	if i-1>=0 and int(a[i-1][j])==v+1:
		s = s.union(track(i-1,j,v+1))
	if j-1>=0 and int(a[i][j-1])==v+1:
		s = s.union(track(i,j-1,v+1))
	return s


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
			val = track(i,j,0)
			ans += len(val)

print(ans)

