#PEP8
class Person:
	#class variable
	people_count = 0

	def __init__(self, name, age):
		#instance variables
		self.name = name
		self.age = age
		Person.people_count += 1

	def __repr__(self):
		return "<object: {},{}>".format(self.name, self.age)

	def say_hello(self):
		return "Hello, I'm {} and {} y/o".format(self.name, self.age)

p2 = Person("George",4)

a = [("Joe", 38),("Jane", 23),('Josh',60),('Jee',18),('Jackie', 34)]

b = []
for name, age in a:
	person = Person(name, age)
	b.append(person)

for person in b:
	print person.say_hello()

#print Person.people_count
#print p2.people_count
print p2.say_hello()

