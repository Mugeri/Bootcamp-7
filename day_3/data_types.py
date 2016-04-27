

def data_type(x):
	'''
	Takes in an argument, x:
		-for integer, return x**2
		-for a float, return x/2
		-for a string, returns "Hello" + x
		-for a boolean, return "boolean"
		-for a long, return "long"
	'''
	if type(x) == int:
		return x ** 2
	elif type(x) == float:
		return x / 2
	elif type(x) == str:
		return "Hello {}".format(x)
	elif type(x) == bool:
		return "boolean"
	elif type(x) == long:
		return "long"
	else:
		return "Not included in function"
