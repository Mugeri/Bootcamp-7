from person import Person
class Kenyan(Person):
	corrupt = False
	from person import Person
	"""docstring for Kenyan"Personf __init__(self, arg):
		from person import Person
		super(Kenyan,Person.__init__()
		self.arg = arg
	"""
	def probe(self, corrupt):
		self.corrupt = corrupt

	def is_corrupt(self):
		if self.corrupt:
			return "Yes"
		return "No"


