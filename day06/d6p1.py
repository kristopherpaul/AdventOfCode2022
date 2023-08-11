s = open("inpd6.txt","r").read()
for i in range(3,len(s)):
    if len(list(set(s[i-3:i+1]))) == 4:
        print(i+1)
        break