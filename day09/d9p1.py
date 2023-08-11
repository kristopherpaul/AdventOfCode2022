lines = open("inpd9.txt","r").read().split('\n')
vis,xh,yh,xt,yt = [[0,0]],0,0,0,0

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
    if ((xh-xt)**2+(yh-yt)**2) <= 2:
        return
    if xh == xt:
        if yh < yt:
            yt -= 1
        else:
            yt += 1
    elif yh == yt:
        if xh < xt:
            xt -= 1
        else:
            xt += 1
    else:
        if xh < xt and yh < yt:
            xt,yt = xt-1,yt-1
        elif xh < xt and yh > yt:
            xt,yt = xt-1,yt+1
        elif xh > xt and yh < yt:
            xt,yt = xt+1,yt-1
        else:
            xt,yt = xt+1,yt+1
    if [xt,yt] not in vis:
        vis.append([xt,yt])

for line in lines:
    for _ in range(int(line.split()[1])):
        move(line.split()[0])
print(len(vis))