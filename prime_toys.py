
_inf = float("inf")

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

def genPrimes(quant=_inf):
	isPrime = Checker()
	curr_num = 2
	while quant > 0:
		while not isPrime(curr_num):
			curr_num += 1
		yield curr_num
		curr_num += 1
	
