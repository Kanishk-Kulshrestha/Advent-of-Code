w = 101
h = 103
quad = [0]*4
while(1):
	
	inp = input()
	if inp=="":
		break

	p,v = inp.split(' ')
	p = list(map(int, p[2:].split(',')))
	v = list(map(int, v[2:].split(',')))

	p = [p[i]+v[i]*100 for i in range(2)]
	p[0] = p[0]%w
	p[1] = p[1]%h
	# print(p[::-1])

	if p[0]<w//2:
		if p[1]<h//2:
			quad[0]+=1
		elif p[1]>h//2:
			quad[1]+=1
	elif p[0]>w//2:
		if p[1]<h//2:
			quad[2]+=1
		elif p[1]>h//2:
			quad[3]+=1

print(quad)
ans = 1
for i in quad:
	ans*=i
print(ans)