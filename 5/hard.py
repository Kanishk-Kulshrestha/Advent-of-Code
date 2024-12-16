ans = 0
d = {}

def srt(a):
	ret = [-1]*len(a)
	for i in a:
		count = 0
		if i in d:
			for j in d[i]:
				if j in a:
					count+=1
		if ret[count]!=-1:
			while(ret[count]!=-1):
				count+=1
		ret[count] = i
	return ret


while(1):
	a = input()
	if a=='':
		break
	
	a,b = map(int, a.split('|'))
	if b not in d:
		d[b] = set()

	d[b].add(a)

while(1):
	p = [0]*100
	flag = 1
	inp = input()
	if inp=="":
		break
	a = list(map(int, inp.split(',')))
	pages = set(a)
	for i in a:
		if i in d:
			for j in d[i]:
				if j in pages and p[j]==0:
					ans += srt(a)[len(a)//2]

					flag = 0
					break
		p[i] = 1
		if not flag:
			break
	if not flag:
		continue

print(ans)