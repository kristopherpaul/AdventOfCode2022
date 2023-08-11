l = [int(x)*811589153 for x in open("inpd20.txt","r").read().split("\n")]
order = [i for i in range(0,len(l))]
for _ in range(10):
    for i in range(len(l)):
        si = 0
        for j in range(len(l)):
            if order[j] == i:
                si = j
                break
        v = l[si]
        u = order[si]
        del l[si]
        del order[si]
        if si+v <= 0:
            order.insert(len(l)-(abs(si+v)%len(l)),u)
            l.insert(len(l)-(abs(si+v)%len(l)),v)
        else:
            order.insert((si+v)%len(l),u)
            l.insert((si+v)%len(l),v)
ind = l.index(0)
print(l[(ind+1000)%len(l)]+l[(ind+2000)%len(l)]+l[(ind+3000)%len(l)])