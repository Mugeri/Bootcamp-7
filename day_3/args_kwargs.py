
#unpacking
def hello(name, age,city=""):
	'''
	'''
	if city != "":
		return "I am {} and I'm {}, i live in {}".format(name,age,city)
	return "I am {} and I'm {}".format(name,age)


people = [("Jane",23,"Nairobi"),("Joe",25,"Mombasa"),("Brian",60),("Betty",45,"Mwea")]

for person in people:
	print hello(*person)

def super_sum(a,b,*args):
	'''
		Takes in variable number of items,
		and returns the sum.
		e.g. super_sum(10,20) = 30
			super_sum(10,20,30) =60
	'''
	total = 0
	for i in args:
		total += i
	return total + a + b


print super_sum(10, 20)
print super_sum(1,4,5,7)
a = [10, 40, 60]
print super_sum(*a)

def hello_again(**kwargs):
	return "I am {} and I'm {}".format(kwargs['name'],kwargs['age'])

Joe = {"name":"Joe", "age":98}

print hello_again(name="Jane", age=23)
print hello_again(**Joe)
