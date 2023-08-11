blocked,max_y = {},0
for line in open("inpd14.txt","r").read().split('\n'):
    l = line.split(' -> ')
    for i in range(1,len(l)):
        x1,y1 = map(int,l[i-1].split(','))
        x2,y2 = map(int,l[i].split(','))
        max_y = max([max_y,y1,y2])
        x1,x2,y1,y2 = min(x1,x2),max(x1,x2),min(y1,y2),max(y1,y2)
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                blocked[(x,y)] = True

def move(x,y):
    global blocked,max_y
    if y == max_y+1:
        return x,y
    if (x,y+1) not in blocked.keys():
        return move(x,y+1)
    if (x-1,y+1) not in blocked.keys():
        return move(x-1,y+1)
    if (x+1,y+1) not in blocked.keys():
        return move(x+1,y+1)
    return x,y

ans = 0
for _ in range(1000000):
    lx,ly = move(500,0)
    blocked[(lx,ly)] = True
    ans += 1
    if lx == 500 and ly == 0:
        break
print(ans)