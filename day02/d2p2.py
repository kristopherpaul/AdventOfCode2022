f = open("inpd2.txt","r")
order1 = ['A','B','C']
score = 0
for x in f.read().split('\n'):
	try:
		i1 = order1.index(x.split()[0])
		cond = x.split()[1]
		if cond == "X":
			score += 1+((i1-1+3)%3)
		elif cond == "Y":
			i2 = i1
			score += 4+i2
		else:
			score += 7+((i1+1)%3)
	except:
		pass
print(score)