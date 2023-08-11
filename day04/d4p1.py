count = 0
for x in open("inpd4.txt","r").read().split('\n'):
    l1,r1 = int(x.split(',')[0].split('-')[0]),int(x.split(',')[0].split('-')[1])
    l2,r2 = int(x.split(',')[1].split('-')[0]),int(x.split(',')[1].split('-')[1])
    if (l1 <= l2 and r2 <= r1) or (l2 <= l1 and r1 <= r2):
        count += 1
print(count)