ans = 0
l = open("inpd3.txt","r").read().split('\n')
for i in range(0,len(l),3):
    try:
        com = ""
        for y in l[i]:
            if y in l[i+1] and y in l[i+2]:
                com = y
                break
        if ord('a') <= ord(com) <= ord('z'):
            ans += ord(com)-ord('a')+1
        elif ord('A') <= ord(com) <= ord('Z'):
            ans += ord(com)-ord('A')+27  
    except:
        pass    

print(ans)