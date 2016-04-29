def find_missing(a=None, b=None):
	if a != None and b != None:
		
		c = set(a).symmetric_difference(b)
		answer = list(c)
		for i in answer:
			return i

	return 0
