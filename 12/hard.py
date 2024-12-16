a = []

while(1):
	inp = input()
	if inp=="":
		break
	a.append(inp)

n = len(a)
m = len(a[0])

v = [[0]*m for _ in range(n)]
si = [[-1]*m for _ in range(n)]

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

def checker(i,j):
	r = 0
	if i-1>=0 and a[i-1][j]==a[i][j]:
		r += 1
	if i+1<n and a[i+1][j]==a[i][j]:
		r += 1
	if j-1>=0 and a[i][j-1]==a[i][j]:
		r += 1
	if j+1<m and a[i][j+1]==a[i][j]:
		r += 1
	return r-1


def track(i,j,val):
	area = 1
	sides = side(i,j)
	si[i][j]=side(i,j)
	if i-1>=0 and a[i-1][j]==val and v[i-1][j]==0:
		v[i-1][j]=1
		ar,s = track(i-1,j,val)
		area+=ar
		sides+=s
	if j-1>=0 and a[i][j-1]==val and v[i][j-1]==0:
		v[i][j-1]=1
		ar,s = track(i,j-1,val)
		area+=ar
		sides += s
	if i+1<n and a[i+1][j]==val and v[i+1][j]==0:
		v[i+1][j]=1
		ar,s = track(i+1,j,val)
		area+=ar
		sides += s
	if j+1<m and a[i][j+1]==val and v[i][j+1]==0:
		v[i][j+1]=1
		ar,s = track(i,j+1,val)
		area+=ar
		sides += s
	
	return area,sides


def cordia(i,j,dir):
	x,y = i,j
	x += dir[0]
	y += dir[1]
	if x>=0 and x<n and y>=0 and y<m and a[x][y]==a[i][j] and a[i][y]==a[i][j] and a[x][j]==a[i][j]:
		return 1
	return 0


def side(i,j):
	k = checker(i,j)+1
	if k==0:
		return 4
	if k==1:
		return 2
	if k==2:
		if i-1>=0 and i+1<n and a[i-1][j]==a[i][j] and a[i+1][j]==a[i][j]:
			return 0
		elif j-1>=0 and j+1<n and a[i][j-1]==a[i][j] and a[i][j+1]==a[i][j]:
			return 0
		else:
			x1 = cordia(i,j,[1,1])
			x2 = cordia(i,j, [1,-1])
			x3 = cordia(i,j, [-1,1])
			x4 = cordia(i,j, [-1,-1])
			return 2-x1-x2-x3-x4
	if k==3:
		x1 = cordia(i,j,[1,1])
		x2 = cordia(i,j, [1,-1])
		x3 = cordia(i,j, [-1,1])
		x4 = cordia(i,j, [-1,-1])
		return 2-x1-x2-x3-x4
	else:
		x1 = cordia(i,j,[1,1])
		x2 = cordia(i,j, [1,-1])
		x3 = cordia(i,j, [-1,1])
		x4 = cordia(i,j, [-1,-1])
		return 4-x1-x2-x3-x4





ans = 0




for i in range(n):
	for j in range(m):
		if v[i][j]==0:
			v[i][j]=1
			area,sides = track(i,j,a[i][j])
			ans += area*sides
			# print(a[i][j], area, sides)
			
print(ans)