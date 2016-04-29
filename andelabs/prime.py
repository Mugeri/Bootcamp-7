
class  PrimeChecker(object):
	def __init__(self, number=None):
		self.number = number

	def is_prime(self):
		prime = False
		if self.number == '':
			return prime
	  	self.number = int(self.number)
	  	number = self.number
		
		if number < 2:
			prime = False
		elif number == 2:
			prime = True
		else:
			for x in range(2,number):
				if number % x == 0:
					prime = False
					return prime
				else:
					prime = True
		return prime
