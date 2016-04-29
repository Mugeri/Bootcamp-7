def string_length(A):
	length=[]
	if type(A) == str:
		length.append(len(A))
		return length
	if type(A) == list:
		for i in A:
			print i
			length.append(len(i))
		return length