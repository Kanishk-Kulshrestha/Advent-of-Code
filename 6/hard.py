n = 10
a = []
cord = []
d = 1


for i in range(n):
	a.append(list(input()))


for i in range(n):
	for j in range(n):
		if a[i][j] == '^':
			while(i<n and j<n and i>=0 and j>=0):
				if d==1:
					i-=1
					if (i<n and j<n and i>=0 and j>=0) and a[i][j]=='#':
						i+=1
						cord.append([i,j])
						d=2
				elif d==2:
					j+=1
					if (i<n and j<n and i>=0 and j>=0) and a[i][j]=='#':
						j-=1
						cord.append([i,j])
						d=3

				elif d==3:
					i+=1
					if (i<n and j<n and i>=0 and j>=0) and a[i][j]=='#':
						i-=1
						cord.append([i,j])
						d=4

				elif d==4:
					j-=1
					if (i<n and j<n and i>=0 and j>=0) and a[i][j]=='#':
						j+=1
						cord.append([i,j])
						d=1
			
			break

print(cord)