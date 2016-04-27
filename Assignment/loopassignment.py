
f = [(10,20,40), (10,40),(4, 5, 50)]

for i in f:
	#check the length of the tuple
	if len(i)==3:
		print "x:{},    y:{},    z:{}".format(*i)
	print "x:{},    y:{}".format(*i)
