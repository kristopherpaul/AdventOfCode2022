l = [int(x) for x in open("inpd20.txt","r").read().split("\n")]
vis = [False for _ in range(len(l))]
for i in range(len(l)):
    si = 0
    for j in range(len(l)):
        if vis[j] == False:
            si = j
            break
    v = l[si]
    del l[si]
    del vis[si]
    if si+v <= 0:
        vis.insert(len(l)-(abs(si+v)%len(l)),True)
        l.insert(len(l)-(abs(si+v)%len(l)),v)
    else:
        vis.insert((si+v)%len(l),True)
        l.insert((si+v)%len(l),v)
ind = l.index(0)
print(l[(ind+1000)%len(l)]+l[(ind+2000)%len(l)]+l[(ind+3000)%len(l)])