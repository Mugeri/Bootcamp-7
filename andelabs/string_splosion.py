class StringSplosion(object):

	def __init__(self,string):
		self.string = string

	def manipulate(self):
		string = self.string
		count = 0
		string1 = ''
		while(count <= len(string)):
			string1 = string1 + string[:count]
			count += 1

		return string1
