def rec(r,a, i, v):
	if i==len(a):	
		return r==v

	return rec(r,a, i+1, v+a[i]) or rec(r, a, i+1, v*a[i])

ans = 0
while(1):
	inp = input()
	if inp=="":
		break
	r, a = inp.split(':')
	r = int(r)
	a = list(map(int, a.split()))
	op = ["+"]*(len(a)-1)
	if rec(r,a,1,a[0]):
		ans+=r
print(ans)