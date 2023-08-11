sz,files = {},{}
def find_sz(d):
    global sz,files
    if d not in sz.keys():
        csz = 0
        for f in files[d]:
            if f.split()[0] == 'dir':
                csz += find_sz(d+"|"+f.split()[1])
            else:
                csz += int(f.split()[0])
        sz[d] = csz
        return sz[d]
    else:
        return sz[d]

cmds = open("inpd7.txt","r").read().split('$ ')
cur_dir = ""
for i in range(1,len(cmds)):
    cmd = cmds[i].split('\n')[0]
    res = cmds[i].split('\n')[1:]
    if cmds[i].split('\n')[-1] == "":
        res = res[:-1]
    if cmd.startswith('cd'):
        if cmd.split()[1] == "..":
            cur_dir = "|".join(cur_dir.split('|')[:-1])
        else:
            if cur_dir == "":
                cur_dir = cmd.split(' ')[1]
            else:
                cur_dir = cur_dir+"|"+cmd.split(' ')[1]
        if cur_dir not in files.keys():
            files[cur_dir] = 0
    else:
        files[cur_dir] = res

print(min([find_sz(key) for key in files.keys() if find_sz(key) >= find_sz('/')-40000000]))