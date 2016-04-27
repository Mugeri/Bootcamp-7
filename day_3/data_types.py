

def data_type(x):
	'''
	Takes in an argument, x:
		-for integer, return x**2
		-for a float, return x/2
		-for a string, returns "hello" + x
		-for a boolean, return "boolean"
		-for a long, return "long"
	'''
	if type(x) == int:
		return x**2
	elif type(x) == float:
		return x/2
	elif type(x) == str:
		return "hello " + x
	elif type(x) == bool:
		return "boolean"
	elif type(x) == long:
		return "long"
	else:
		return "Not included in function"

print data_type(3)
print data_type(8.50)
print data_type("olive")
print data_type(True)
print data_type(487429237328723838328936473900000000732732893289)
print data_type(20**20)