lines = open("inpd10.txt","r").read().split('\n')
x,cyc = 1,0
screen = [['.' for _ in range(40)] for _ in range(6)]
for line in lines:
    if line == "noop":
        cyc += 1
        if (cyc-1) >= 0 and (cyc-1)%40 in [x-1,x,x+1]:
            screen[cyc//40][(cyc-1)%40] = '#'
    elif line.startswith('addx'):
        cyc += 1
        if (cyc-1) >= 0 and (cyc-1)%40 in [x-1,x,x+1]:
            screen[cyc//40][(cyc-1)%40] = '#'
        cyc += 1
        if (cyc-1) >= 0 and (cyc-1)%40 in [x-1,x,x+1]:
            screen[cyc//40][(cyc-1)%40] = '#'
        x += int(line.split()[1])
print("\n".join(["".join(screen[i]) for i in range(6)]))