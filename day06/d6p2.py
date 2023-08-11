s = open("inpd6.txt","r").read()
for i in range(13,len(s)):
    if len(list(set(s[i-13:i+1]))) == 14:
        print(i+1)
        break