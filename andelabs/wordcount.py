def words(A):
	count = dict()

	for i in A:
		if i not in count:
			count[i] = 1
		else:
			count[i] += 1


