lines = open("inpd10.txt","r").read().split('\n')
x,cyc,ans = 1,0,0
for line in lines:
    if line == "noop":
        cyc += 1
        if cyc in [20,60,100,140,180,220]:
            ans += cyc*x
    elif line.startswith('addx'):
        cyc += 1
        if cyc in [20,60,100,140,180,220]:
            ans += cyc*x
        cyc += 1
        if cyc in [20,60,100,140,180,220]:
            ans += cyc*x
        x += int(line.split()[1])
print(ans)