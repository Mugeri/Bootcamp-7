def data_type(A):
	if A == None:
		return 'no value'
	dtype = type(A)
	if dtype == str:
		return len(A)
	elif dtype == bool:
		return True
	elif dtype == int:
		if A < 100:
			return "less than 100"
		elif A == 100:
			return 'equal to 100'
		else:
			return 'more than 100'
	elif dtype == list:
		if len(A) < 3:
			return None
		return A[2]

