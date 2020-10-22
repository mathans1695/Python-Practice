def prime_numbers(number):
	prime_list = []
	
	if number == 1:
		prime_list = [1]
		return prime_list
		
	elif number == 2:
		prime_list = [1, 2]
		return prime_list
		
	elif number == 3:
		prime_list = [1, 2, 3]
		return prime_list
		
	elif number == 4:
		prime_list = [1, 2, 3]
		return prime_list
		
	elif number > 4:
		prime_list = [1, 2, 3]
		
		i = 5
	
		while i <= number:
		
			j = 3
			
			while j <= i:
			
				if i % j == 0:
					if i == j:
						i = j
						prime_list.append(i)
					break	
				j += 2
				
			i += 2
			
		return prime_list
		
	else:
		return None


def sum_of_prime_number(number):
	prime_numbers_copy = []
	prime_numbers_copy = prime_numbers(number)
	
	j = 0
	for i in prime_numbers_copy:
		j = j + i
		
	return j


def prime_factors(number):
	prime_numbers_copy = []
	prime_numbers_copy = prime_numbers(number)
	
	if len(prime_numbers_copy) == 1:
		
		return prime_numbers_copy
	
	else:
		
		prime_numbers_copy.remove(1)
		
		prime_factors = []
	
		while number > 1:
		
			for i in prime_numbers_copy:
			
				if number % i == 0:
					number = number / i
					prime_factors.append(i)
					
					break
				
		
		return prime_factors
	
	
def sort_prime_factors(number):
	prime_factors_list = []
	prime_factors_list = prime_factors(number)
	
	for i in prime_factors_list:
		
		for j in range(prime_factors_list.index(i) + 1, len(prime_factors_list)):
			
			if i > prime_factors_list[j]:
				
				swap = i
				prime_factors_list[prime_factors_list.index(i)] = prime_factors_list[j]
				prime_factors_list[j] = swap
		
	return prime_factors_list
			
			

def largest_prime_factors(number):
	
	sorted_prime_factors_list = []
	sorted_prime_factors_list = prime_factors(number)
	
	return sorted_prime_factors_list[len(sorted_prime_factors_list) - 1]
	
	
print(prime_numbers(int(input("Enter a number: "))))
	
	