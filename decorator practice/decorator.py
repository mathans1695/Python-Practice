# Let's practice closures first

# Closures will use first class function - if a function accept or return a function, it's called first class function

# Lets pass a function to another function

# def accepts_func(func):
#	return func()
	
# def passed_func():
#	i = 5
#	return (i * i)
	
# temp = accepts_func(passed_func)

# print(temp)

# Let's implement a closure, closure is nothing but inner function will remember local scope(outer function values) values, even when the outer function finished executed

def decorator_function(original_func):
	def wrapper_function(*args, **kwargs):
		print('Added extra features to the display function')
		print('Keyword Arguments:')
		
		for key, values in kwargs.items():
			print(key, values)
			
		original_func(*args, **kwargs)
		
	return wrapper_function
	
def display(*args, **kwargs):
	print('display function executed')
	print('Positional Arguments:')
	
	for values in args:
		print(values)

display = decorator_function(display)
display(5, 6, name='Mahalingam', career='sales', future='developer')