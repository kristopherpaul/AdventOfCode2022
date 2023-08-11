lines = open("inpd8.txt","r").read().split('\n')
n = len(lines)
arr = []
for i in range(n):
    arr.append([1]+[0]*(len(lines[0])-2)+[1])
arr[0] = [1]*len(lines[0])
arr[-1] = [1]*len(lines[0])
for i in range(0,len(lines)):
    cur = int(lines[i][0])
    for j in range(1,len(lines[0])):
        if int(lines[i][j]) > cur:
            arr[i][j] = 1
        cur = max(cur,int(lines[i][j]))

    cur = int(lines[i][-1])
    for j in range(len(lines[0])-2,-1,-1):
        if int(lines[i][j]) > cur:
            arr[i][j] = 1
        cur = max(cur,int(lines[i][j]))
for j in range(0,len(lines[0])):
    cur = int(lines[0][j])
    for i in range(1,len(lines)):
        if int(lines[i][j]) > cur:
            arr[i][j] = 1
        cur = max(cur,int(lines[i][j]))
    cur = int(lines[-1][j])
    for i in range(len(lines)-2,-1,-1):
        if int(lines[i][j]) > cur:
            arr[i][j] = 1
        cur = max(cur,int(lines[i][j]))
print(sum([sum(arr[i]) for i in range(len(arr))]))