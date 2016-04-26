def sum_digits(A):
	'''
	Takes a list A, and returns 
	the sum of all the digits in the list
	e.g[10, 30, 45] should return 1+0+3+0+4+5
	'''
	total = 0
	
	for each in A:
		c = str(each)
		for each1 in c:
			total += int(each1)
	return total

print sum_digits([10,30,45])
