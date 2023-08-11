stacks = ['ZPMHR','PCJB','SNHGLCD','FTDMQSRL','FSPQBTZM','TFSZBG','NRV','PGLTDVCM','WQNJFML']
inp = open("inpd5.txt","r").read()
for line in inp.split('\n'):
    q = int(line.split()[1])
    s = int(line.split()[3])
    e = int(line.split()[5])
    while q:
        ele = stacks[s-1][-1]
        stacks[s-1] = stacks[s-1][:-1]
        stacks[e-1] += ele
        q -= 1
print(''.join([st[-1] for st in stacks]))