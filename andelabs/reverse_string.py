def reverse_string(string):
	if string == '':
		return None
	string1 = string[::-1]
	if string1 == string:
		return True
	return string1
