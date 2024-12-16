n = 50
a = []
d ={}
count = 0
def dis(x1,y1,x2,y2):
	return ((x1-x2)**2+(y1-y2)**2)

def equation(e1, e2, x, y):
	x1,y1 = e1
	x2,y2 = e2
	if x*(y1-y2) + x1*(y2-y) + x2*(y-y1) == 0:
		if dis(x,y,x1,y1)*2==dis(x,y,x2,y2) or dis(x,y,x1,y1)==dis(x,y,x2,y2)*2:
			return 1
	return 0

def check(x,y,d):
	for a in d:
		for i in range(len(d[a])):
			for j in range(i+1, len(d[a])):
				if equation(d[a][i], d[a][j], x, y):
					return 1
	return 0



for i in range(n):
	a.append(list(input()))

for i in range(n):
	for j in range(n):
		if a[i][j]!='.':
			if a[i][j] in d:
				d[a[i][j]].append([i,j])
			else:
				d[a[i][j]] = [[i,j]]

for i in d:
	print(i, d[i])

for i in range(n):
	for j in range(n):
		count+=check(i,j,d)
print(count)