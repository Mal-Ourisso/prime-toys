
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

class Factored:
	
	def __init__(self, number=1):
		_factors = {}
	
	def __mul__(self, other):
		if not isisntance(other, factored):
			other = Factored(other)
		prod = Factored()
		for prime in set(self.primes+other.primes):
			power = 0
			if prime in self.primes:
				power += self.primes
			if prime in other.primes:
				power += other.primes
			prod._factors[p] = power
		return prod
