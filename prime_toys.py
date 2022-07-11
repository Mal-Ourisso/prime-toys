
class Checker:

	def __init__(self, main_alg="trivial"):
		pass
	
	def trivial(self, number):
		divisor = 2
		while divisor**2 <= number:
			if number%divisor == 0:
				return False
		# else
		return False
