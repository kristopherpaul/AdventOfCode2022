def chk(l1,l2):
    if type(l1) == type(l2):
        if isinstance(l1,int):
            if l1 < l2:
                return 1
            elif l1 == l2:
                return 0
            else:
                return -1
        else:
            for i in range(min(len(l1),len(l2))):
                val = chk(l1[i],l2[i])
                if val == -1:
                    return -1
                elif val == 1:
                    return 1
            if len(l1) > len(l2):
                return -1
            elif len(l1) == len(l2):
                return 0
            else:
                return 1
    elif isinstance(l1,int):
        return chk([l1],l2)
    else:
        return chk(l1,[l2])

idx,ans = 1,0
for line in open("inpd13.txt","r").read().split('\n\n'):
    l1,l2 = eval(line.split('\n')[0]),eval(line.split('\n')[1])
    if chk(l1,l2) == 1:
        ans += idx
    idx += 1
print(ans)