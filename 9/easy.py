# a = "2333133121414131402"
# print(len(a))
# s = ""

# for i in range(len(a)):
# 	if i%2:
# 		s+='.'*int(a[i])
# 	else:
# 		s+=str(i//2)*int(a[i])

# # print(s)

# s = list(s)

# i = 0
# j = len(s)-1

# while(i<j):
# 	if s[i]=='.':
# 		if s[j]!='.':
# 			s[i] = s[j]
# 			s[j] = '.'
# 		else:
# 			j-=1
# 	else:
# 		i+=1

# # print("".join(s))

# ans = 0

# for i in range(len(s)):
# 	if s[i]=='.':
# 		break
# 	ans+=i*int(s[i])

# print(ans)


import sys
import re
from collections import defaultdict, Counter, deque
import pyperclip as pc
def pr(s):
    print(s)
    pc.copy(s)

D = input().strip()

def solve(part2):
    A = deque([])
    SPACE = deque([])
    file_id = 0
    FINAL = []
    pos = 0
    for i,c in enumerate(D):
        if i%2==0:
            if part2:
                A.append((pos, int(c), file_id))
            for i in range(int(c)):
                FINAL.append(file_id)
                if not part2:
                    A.append((pos, 1, file_id))
                pos += 1
            file_id += 1
        else:
            SPACE.append((pos, int(c)))
            for i in range(int(c)):
                FINAL.append(None)
                pos += 1

    for (pos, sz, file_id) in reversed(A):
        for space_i,(space_pos, space_sz) in enumerate(SPACE):
            if space_pos < pos and sz <= space_sz:
                for i in range(sz):
                    assert FINAL[pos+i] == file_id, f'{FINAL[pos+i]=}'
                    FINAL[pos+i] = None
                    FINAL[space_pos+i] = file_id
                SPACE[space_i] = (space_pos + sz, space_sz-sz)
                break

    ans = 0
    for i,c in enumerate(FINAL):
        if c is not None:
            ans += i*c
    return ans

p1 = solve(False)
p2 = solve(True)
pr(p1)
pr(p2)