

def super_sum(A):
	'''
	Takes a list A, and:
		halves every even number
		doubles every odd number
	and returns the sum of all
	'''
	total = 0

	for each in A:
		if each % 2== 0:
			total += each / 2
		else:
			total += each * 2
	
	return total



