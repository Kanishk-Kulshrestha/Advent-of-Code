a = []

while(1):
	inp = input()
	if inp=="":
		break
	a.append(inp)

n = len(a)
m = len(a[0])

v = [[0]*m for _ in range(n)]

def check(i,j):
	r = 0
	if i-1>=0 and a[i-1][j]==a[i][j] and v[i-1][j]==1:
		r += 1
	if i+1<n and a[i+1][j]==a[i][j] and v[i+1][j]==1:
		r += 1
	if j-1>=0 and a[i][j-1]==a[i][j] and v[i][j-1]==1:
		r += 1
	if j+1<m and a[i][j+1]==a[i][j] and v[i][j+1]==1:
		r += 1
	return r-1



def track(i,j,val):
	area = 1
	perimeter = 4
	if i-1>=0 and a[i-1][j]==val and v[i-1][j]==0:
		v[i-1][j]=1
		ar,p = track(i-1,j,val)
		area+=ar
		perimeter+=p-1
	if j-1>=0 and a[i][j-1]==val and v[i][j-1]==0:
		v[i][j-1]=1
		ar,p = track(i,j-1,val)
		area+=ar
		perimeter+=p-1
	if i+1<n and a[i+1][j]==val and v[i+1][j]==0:
		v[i+1][j]=1
		ar,p = track(i+1,j,val)
		area+=ar
		perimeter+=p-1
	if j+1<m and a[i][j+1]==val and v[i][j+1]==0:
		v[i][j+1]=1
		ar,p = track(i,j+1,val)
		area+=ar
		perimeter+=p-1
	
	return area,perimeter-check(i,j)

ans = 0

for i in range(n):
	for j in range(m):
		if v[i][j]==0:
			v[i][j]=1
			area,perimeter = track(i,j,a[i][j])
			perimeter-=1
			ans += area*perimeter
			print(a[i][j], area, perimeter)
			
print(ans)