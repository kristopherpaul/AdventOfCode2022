lines = open("inpd8.txt","r").read().split('\n')
n = len(lines)
arr = []
for i in range(n):
    arr.append([0]*len(lines[0]))
for i in range(0,n):
    for j in range(len(lines[0])):
        sc_1 = i
        for i_ in range(i-1,-1,-1):
            if lines[i_][j] >= lines[i][j]:
                sc_1 = min(sc_1,i-i_)
                break
        sc_2 = n-i-1
        for i_ in range(i+1,n):
            if lines[i_][j] >= lines[i][j]:
                sc_2 = min(sc_2,i_-i)
                break
        sc_3 = j
        for j_ in range(j-1,-1,-1):
            if lines[i][j_] >= lines[i][j]:
                sc_3 = min(sc_3,j-j_)
                break
        sc_4 = len(lines[0])-j-1
        for j_ in range(j+1,len(lines[0])):
            if lines[i][j_] >= lines[i][j]:
                sc_4 = min(sc_4,j_-j)
                break
        arr[i][j] = sc_1*sc_2*sc_3*sc_4
print(max([max(arr[i]) for i in range(len(arr))]))