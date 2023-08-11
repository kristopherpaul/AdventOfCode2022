f = open("inpd1.txt","r")
mx = 0
for x in f.read().split('\n\n'):
	try:
		mx = max(mx,sum([int(y) for y in x.split('\n')]))
	except:
		pass
print(mx)