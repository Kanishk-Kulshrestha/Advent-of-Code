n = 140
m = 140
a  = []
count = 0
for i in range(n):
	a.append(list(input()))

for i in range(1,n-1):
	for j in range(1,m-1):
		if a[i][j]=='A':
			if ((a[i-1][j-1]=='M' and a[i+1][j+1]=='S') or (a[i-1][j-1]=='S' and a[i+1][j+1]=='M')) and ((a[i-1][j+1]=='M' and a[i+1][j-1]=='S') or (a[i-1][j+1]=='S' and a[i+1][j-1]=='M')):
				count+=1

print(count)