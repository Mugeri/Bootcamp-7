
def super_sum(*args):
	'''
		Returns the sum of arguments passed:
			- super_sum() == '' -->'Please enter numbers'
			- super_sum(1,2,3) --> 6
			- super_sum([1,2,3]) --> 6
			- super_sum([10],[20],[30]) --> 60
	'''	
	sum_ = 0
	if not args:
		return 0
	
	else:
		for x in args:
			#x is now [1,2,3]
			if type(x) == list:
				for  i in x:
					#i is  now 1, 2, 3
					sum_ += i
				return sum_
			elif type(x) == str:
				return 0

			elif type(x) == tuple:
				z = list(x)
				for  i in z:
					#i is  now 1, 2, 3
					sum_ += i
				return sum_

			else:
					sum_ += x
		return sum_
	
'''

	elif type(args) is tuple:
		for i in range (len(args)-1):
			sum_ += args[i]
		return sum_
'''