d = {}
dp = {}
def rec(w):
    global d,dp
    if w in dp.keys():
        return dp[w]
    if d[w].isnumeric():
        dp[w] = int(d[w])
        return dp[w]
    v1 = rec(d[w].split()[0])
    v2 = rec(d[w].split()[2])
    if d[w].split()[1] == '+':
        dp[w] = v1+v2
    elif d[w].split()[1] == '-':
        dp[w] = v1-v2
    elif d[w].split()[1] == '*':
        dp[w] = v1*v2
    elif d[w].split()[1] == '/':
        dp[w] = v1/v2
    return dp[w]

for line in open("inpd21.txt","r").read().split("\n"):
    d[line.split(":")[0]] = line.split(": ")[1]

print(int(rec("root")))