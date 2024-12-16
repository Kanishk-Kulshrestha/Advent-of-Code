a = []


while(1):
	inp = input()
	if inp=="":
		break

	temp = []
	for i in inp:
		if i=='#':
			temp.append('#')
			temp.append('#')
		elif i=='O':
			temp.append('[')
			temp.append(']')
		elif i=='@':
			temp.append('@')
			temp.append('.')
		elif i=='.':
			temp.append('.')
			temp.append('.')

	a.append(temp)

for _ in a:
	print("".join(_))


n = len(a)
m = len(a[0])