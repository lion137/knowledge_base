def hexal_to_decimal(s):
	""" s in form 0X< hexal digits>
	returns int in decimal"""
	s = s[2:]
	s = s[::-1]
	s = list(s)
	for i, e in enumerate(s):
		if s[i] == "A": s[i] = "10"
		if s[i] == "B": s[i] = "11"
		if s[i] == "C": s[i] = "12"
		if s[i] == "D": s[i] = "13"
		if s[i] == "E": s[i] = "14"
		if s[i] == "F": s[i] = "15"
	sum = 0
	for i, e in enumerate(s):
		sum += (16 ** i) * int(e)
	return sum

def octal_to_decimal(s):
	"""s in form 0X<octal digits>
	returns int in decimal"""
	s = s[1:]
	s = s[::-1] # reverse
	sum = 0
	for i, e in enumerate(s):
		sum += (8 ** i) * int(e)
	return sum
print(hexal_to_decimal("0XCC"))
print(octal_to_decimal("010"))
