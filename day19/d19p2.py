from math import ceil
import time
dp = {}

def trav(bag,cost,cnt,t):
    if (bag,cnt,t) in dp.keys():
        return dp[(bag,cnt,t)]
    if t == 1:
        dp[(bag,cnt,t)] = 0
        return 0
    ans = 0
    w_ore = cnt[0] < ceil((max(cost[0],cost[1],cost[2],cost[4])*t-bag[0])/t)
    w_clay = cnt[1] < ceil((cost[3]*t-bag[1])/t)
    w_obs = cnt[2] < ceil((cost[5]*t-bag[2])/t)

    if bag[0] >= cost[4] and bag[2] >= cost[5]:
        # geode robot
        ans = max(ans,trav((bag[0]-cost[4]+cnt[0],bag[1]+cnt[1],bag[2]-cost[5]+cnt[2]),cost,cnt,t-1)+t-1)
    if bag[0] >= cost[2] and bag[1] >= cost[3] and w_obs:
        # obsidian robot
        ans = max(ans,trav((bag[0]-cost[2]+cnt[0],bag[1]-cost[3]+cnt[1],bag[2]+cnt[2]),cost,(cnt[0],cnt[1],cnt[2]+1),t-1))
    if bag[0] >= cost[0] and w_ore:
        # ore robot
        ans = max(ans,trav((bag[0]-cost[0]+cnt[0],bag[1]+cnt[1],bag[2]+cnt[2]),cost,(cnt[0]+1,cnt[1],cnt[2]),t-1))
    if bag[0] >= cost[1] and w_clay and w_obs:
        # clay robot
        ans = max(ans,trav((bag[0]-cost[1]+cnt[0],bag[1]+cnt[1],bag[2]+cnt[2]),cost,(cnt[0],cnt[1]+1,cnt[2]),t-1))
    ans = max(ans,trav((bag[0]+cnt[0],bag[1]+cnt[1],bag[2]+cnt[2]),cost,cnt,t-1))
    dp[(bag,cnt,t)] = ans
    return ans

ans = []
for line in open("inpd19.txt","r").read().split("\n"):
    w = [int(x) for x in line.split() if x.isnumeric()]
    dp = {}
    t_s = time.time()
    ans.append(trav((0,0,0),tuple(w),(1,0,0),32))
    t_e = time.time()
    print(ans[-1],int(t_e-t_s))
    if len(ans) == 3:
        break
print(ans[0]*ans[1]*ans[2])