ans = 0

for x in open("inpd3.txt","r").read().split('\n'):
    try:
        com = ""
        for y in x[:len(x)//2]:
            if y in x[len(x)//2:]:
                com = y
                break
        if ord('a') <= ord(com) <= ord('z'):
            ans += ord(com)-ord('a')+1
        elif ord('A') <= ord(com) <= ord('Z'):
            ans += ord(com)-ord('A')+27
    except:
        pass

print(ans)