l = [[[73,77],["o","*","5"],11,6,5],[[57,88,80],["o","+","5"],19,6,0],[[61, 81, 84, 69, 77, 88],["o","*","19"],5,3,1],[[78, 89, 71, 60, 81, 84, 87, 75],["o","+","7"],3,1,0],[[60, 76, 90, 63, 86, 87, 89],["o","+","2"],13,2,7],[[88],["o","+","1"],17,4,7],[[84, 98, 78, 85],["o","*","o"],7,5,4],[[98, 89, 78, 73, 71],["o","+","4"],2,3,2]]
#l = [[[79,98],["o","*","19"],23,2,3],[[54,65,75,74],["o","+","6"],19,2,0],[[79,60,97],["o","*","o"],13,1,3],[[74],["o","+","3"],17,0,1]]
cnt = [0 for _ in range(8)]
for _ in range(20):
    for i in range(len(l)):
        for j in range(len(l[i][0])):
            cnt[i] += 1
            o = 0
            if l[i][1][1] == '*':
                o = 1
                if l[i][1][0] == 'o':
                    o *= l[i][0][j]
                else:
                    o *= int(l[i][1][0])
                if l[i][1][2] == 'o':
                    o *= l[i][0][j]
                else:
                    o *= int(l[i][1][2])
            elif l[i][1][1] == '+':
                if l[i][1][0] == 'o':
                    o += l[i][0][j]
                else:
                    o += int(l[i][1][0])
                if l[i][1][2] == 'o':
                    o += l[i][0][j]
                else:
                    o += int(l[i][1][2])
            o //= 3
            if o % l[i][2] == 0:
                l[l[i][3]][0].append(o)
            else:
                l[l[i][4]][0].append(o)
        l[i][0] = []
cnt.sort()
print(cnt[-2]*cnt[-1])