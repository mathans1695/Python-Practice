def largest_prime_factors(number):
	i = 2
	while i <= number:
		i += 1
		if i % 2 == 0:
			continue
		else:
			j = 3
			while j <= i:
				if j % i == 0:
					if j == i:
						if number % j == 0:
							number = number / j
							i = j
							result1 = i
			
				j += 2
	
	return result1
	
result = largest_prime_factors(int(input("Enter a number to find largegst prime factors: ")))
print (result)