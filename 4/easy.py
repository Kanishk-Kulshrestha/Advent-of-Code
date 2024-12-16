n = 140
m = 140
a  = []
count = 0
for i in range(n):
	a.append(list(input()))

for i in range(n):
	for j in range(m):
		if a[i][j]=='X':	
			# left-up
			if i>=3 and j>=3 and a[i-1][j-1]+a[i-2][j-2]+a[i-3][j-3]=="MAS":
				count+=1
			# right-down
			if i<=n-4 and j<=m-4 and a[i+1][j+1]+a[i+2][j+2]+a[i+3][j+3]=="MAS":
				count+=1
			# right-up
			if i>=3 and j<=m-4 and a[i-1][j+1]+a[i-2][j+2]+a[i-3][j+3]=="MAS":
				count+=1
			# left-down
			if i<=n-4 and j>=3 and a[i+1][j-1]+a[i+2][j-2]+a[i+3][j-3]=="MAS":
				count+=1
			# down
			if i<=n-4 and a[i+1][j]+a[i+2][j]+a[i+3][j]=="MAS":
				count+=1
			# up
			if i>=3 and a[i-1][j]+a[i-2][j]+a[i-3][j]=="MAS":
				count+=1
			# left
			if j<=m-4 and a[i][j+1]+a[i][j+2]+a[i][j+3]=="MAS":
				count+=1
			# right
			if j>=3 and a[i][j-1]+a[i][j-2]+a[i][j-3]=="MAS":
				count+=1

				
print(count)
