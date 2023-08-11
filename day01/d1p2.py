f = open("inpd1.txt","r")
vals = []
for x in f.read().split('\n\n'):
	try:
		vals.append(sum([int(y) for y in x.split('\n')]))
	except:
		pass
print(sum(sorted(vals)[-3:]))