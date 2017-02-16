
#  cannot assume input is always integers
#  in cases where inputs are characters, using int() won't work
#  use ord() instead

def test(a, b):
	if type(a) == str and type(b) == str:
		return ord(a) * ord(b)
	else:
		return a * b

print test('a', 'b')
