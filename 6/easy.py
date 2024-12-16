n = 10
a = []
c = 0
d = 1
for i in range(n):
	a.append(list(input()))


for i in range(n):
	for j in range(n):
		if a[i][j] == '^':
			while(i<n and j<n and i>=0 and j>=0):
				if d==1:
					a[i][j] = 'X'
					i-=1
					if (i<n and j<n and i>=0 and j>=0) and a[i][j]=='#':
						c+=1
						i+=1
						d=2
				elif d==2:
					a[i][j] = 'X'
					j+=1
					if (i<n and j<n and i>=0 and j>=0) and a[i][j]=='#':
						c+=1
						j-=1
						d=3

				elif d==3:
					a[i][j] = 'X'
					i+=1
					if (i<n and j<n and i>=0 and j>=0) and a[i][j]=='#':
						c+=1
						i-=1
						d=4

				elif d==4:
					a[i][j] = 'X'
					j-=1
					if (i<n and j<n and i>=0 and j>=0) and a[i][j]=='#':
						c+=1
						j+=1
						d=1
			
			break

print(c)

count = 0

for i in a:
	for j in i:
		if j=='X':
			count+=1

print(count)