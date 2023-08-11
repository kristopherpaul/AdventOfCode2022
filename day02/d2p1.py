f = open("inpd2.txt","r")
order1,order2 = ['A','B','C'],['X','Y','Z']
score = 0
for x in f.read().split('\n'):
	try:
		i1,i2 = order1.index(x.split()[0]),order2.index(x.split()[1])
		if i2 == (i1+1)%3:
			score += 7+i2
		elif i1 == i2:
			score += 4+i2
		else:
			score += i2+1
	except:
		pass
print(score)