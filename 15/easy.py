a = []
dic = {
	'^': [-1, 0],
	'<': [0, -1],
	'>': [0, 1],
	'v': [1, 0]
}

while(1):
	inp = input()
	if inp=="":
		break
	a.append(list(inp))

n = len(a)
m = len(a[0])


def next(i,j,char,dir):
	if a[i][j]=='.':
		a[i][j]=char
		return 1
	if a[i][j]=='#':
		return 0
	if a[i][j]=='O':
		if next(i+dic[dir][0],j+dic[dir][1],'O', dir):
			a[i][j]=char
			return 1
		return 0

def end():
	s = 0
	for i in range(n):
		for j in range(m):
			if a[i][j]=='O':
				s+=i*100+j
	print(s) 
	print()
	for _ in a:
		print("".join(_))


def begin(i,j):
	while(1):
		inp = input()
		if inp=='':
			end()
			return

		inp = list(inp)
		# print(inp)
		for x in inp:
			if x=='<':
				if next(i,j-1,'@',x):
					a[i][j]='.'
					j-=1
			elif x=='>':
				if next(i,j+1,'@',x):
					a[i][j]='.'
					j+=1
			elif x=='^':
				if next(i-1,j,'@',x):
					a[i][j]='.'
					i-=1
			elif x=='v':
				if next(i+1,j,'@',x):
					a[i][j]='.'
					i+=1

			# for _ in a:
			# 	print("".join(_))


for i in range(n):
	for j in range(m):
		if a[i][j]=='@':
			begin(i,j)
			break