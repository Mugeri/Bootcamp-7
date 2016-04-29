class Car(object):
	"""docstring for Car"""
	def __init__(self, name='General', model='GM', car_type='saloon'):

		self.name = name
		self.model = model
		self.car_type = car_type
		self.speed = 0
		
		if car_type == 'trailer':
			self.num_of_wheels = 8
		else:
			self.num_of_wheels = 4

			
		if name == 'Porshe' or name == 'Koenigsegg':
			self. num_of_doors = 2
		else:
			self.num_of_doors = 4

	# def drive(self, number):
	# 	parked_speed = 0
	# 	speed = 0
	# 	if self.car_type == 'trailer':
	# 		speed = number*11
	# 	else:
	# 		speed = number *333.33

	# 	return speed
		
	def speed(self):
		parked_speed = 0
		if self.bcar_type == 'trailer':
			moving_speed = 77
		moving_speed = 1000
		return parked_speed

	def  is_saloon(self):
		if self.car_type =='saloon':
			return 'saloon'
		return 'trailer'

class drive(Car):
	def speed(self):
		parked_speed = 0
		speed = 0
		if self.car_type == 'trailer':
			speed = number*11
		else:
			speed = number *333.33

		return speed
		


# man = Car('MAN', 'Truck', 'trailer')
# opel = Car('Opel', 'Omega 3' 'saloon')

# print man.num_of_wheels
# print opel.num_of_wheels
