#PEP8
from person import Person
from kenyan import Kenyan

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

k = Kenyan("Anita", 20)
k.probe(True)
print "Is {} corrupt? {}".format(k.name, k.is_corrupt())
print k.say_hello()
