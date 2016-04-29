def find_max_min(i):
	max_ = i[0]
	min_ = i[0]

	for x in i:
		if x > max_:
			max_ = x
		if x < min_:
			min_ = x
	if min_ == max_:
		return [len(i)]

	return [max_, min_]	

print find_max_min([4, 66, 6, 44, 7, 78, 8, 68, 2])	
print find_max_min([4, 4, 4, 4])	 