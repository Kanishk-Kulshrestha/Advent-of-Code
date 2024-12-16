w = 101
h = 103
quad = [0]*4
p = []
v = []

def spread(i,j):
    k=1
    while(grid[i][j-k]):
        k+=1
        if j-k<0:
            break
    return k

def check(i,j):
    val = 0
    wid = 1
    while(grid[i][j]):
        temp = spread(i,j)
        if temp>wid:
            wid=temp
        else:
            break
        i+=1
        if i>=h:
            break
        val+=1

    return val>4

while(1):
    
    inp = input()
    if inp=="":
        break

    pos,vel = inp.split(' ')
    p.append(list(map(int, pos[2:].split(','))))
    v.append(list(map(int, vel[2:].split(','))))

# print("LEN", len(p))

seconds = 1

while(1):
    grid = [[0]*101 for _ in range(103)]

    for i in range(len(p)):
        p[i][0]+=v[i][0]
        p[i][1]+=v[i][1]
        p[i][0] = p[i][0]%w
        p[i][1] = p[i][1]%h

        grid[p[i][1]][p[i][0]] += 1


    # print(sum([sum(_) for _ in grid]))
    for i in range(103):
        for j in range(101):
            if grid[i][j]==1:
                if check(i,j):
                    for _ in grid:
                        print(_)
                    print(seconds)
                    quit()

    seconds+=1