
def isPrimeTrivial(number):
	divisor = 2
	while divisor*divisor <= number:
		if number%divisor == 0:
			return False
		divisor += 1
	# else
	return True

def genPrimes():
	curr_num = 2
	while True:
		while not isPrimeTrivial(curr_num):
			curr_num += 1
		yield curr_num
		curr_num += 1

class Factored:
	
	def __init__(self, number=1):
		self._factors = {}
		inf_primes = genPrimes()
		curr_prime = next(inf_primes)
		while number>1:
			if number%curr_prime == 0:
				if curr_prime in self._factors:
					self._factors[curr_prime] += 1
				else:
					self._factors[curr_prime] = 1
				number //= curr_prime
			else:
				curr_prime = next(inf_primes)
	
	@property
	def primes(self):
		return list(self._factors.keys())
	
	@property
	def powers(self):
		return list(self._factors.values())

	def __mul__(self, other):
		if not isinstance(other, Factored):
			other = Factored(other)
		prod = Factored()
		for prime in set(self.primes+other.primes):
			power = 0
			if prime in self.primes:
				power += self._factors[prime]
			if prime in other.primes:
				power += other._factors[prime]
			prod._factors[prime] = power
		return prod

	def __repr__(self):
		result = ""
		for prime, power in self._factors.items():
			result += f"{prime}^{power} * "
		return result[:-3]
