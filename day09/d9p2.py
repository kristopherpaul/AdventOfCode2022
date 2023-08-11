lines = open("inpd9.txt","r").read().split('\n')
vis,xh,yh,xt,yt = [[0,0]],0,0,[0 for _ in range(9)],[0 for _ in range(9)]

def move(d):
    global vis,xh,yh,xt,yt
    if d == 'L':
        xh -= 1
    elif d == 'R':
        xh += 1
    elif d == 'U':
        yh += 1
    else:
        yh -= 1
    for i in range(9):
        px,py = xh,yh
        if i != 0:
            px = xt[i-1]
            py = yt[i-1]

        if ((px-xt[i])**2+(py-yt[i])**2) <= 2:
            continue
        
        if px == xt[i]:
            if py < yt[i]:
                yt[i] -= 1
            else:
                yt[i] += 1
        elif py == yt[i]:
            if px < xt[i]:
                xt[i] -= 1
            else:
                xt[i] += 1
        else:
            if px < xt[i] and py < yt[i]:
                xt[i],yt[i] = xt[i]-1,yt[i]-1
            elif px < xt[i] and py > yt[i]:
                xt[i],yt[i] = xt[i]-1,yt[i]+1
            elif px > xt[i] and py < yt[i]:
                xt[i],yt[i] = xt[i]+1,yt[i]-1
            else:
                xt[i],yt[i] = xt[i]+1,yt[i]+1
        
    if [xt[-1],yt[-1]] not in vis:
        vis.append([xt[-1],yt[-1]])

for line in lines:
    for _ in range(int(line.split()[1])):
        move(line.split()[0])
print(len(vis))