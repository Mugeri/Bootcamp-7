a=[1,2,3,4,5]

for i in range(len(a)-1,-1,-1):
	print a[i]

#print in reverse
'''
i=len(a)

while i > 0:
	print a[i - 1]
	i -= 1
	'''
b=[(2,4),(5,10),(6,20),(50,50)]

for i in range(0,len(b)):
	print "x:{}, y:{}".format(*b[i])

for i in b:
	print "x:{}, y:{}".format(*i)