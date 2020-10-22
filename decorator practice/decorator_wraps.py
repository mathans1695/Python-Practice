from functools import wraps

def decorator_func(original_func):
	
	@wraps(original_func)
	def wrapper(*args, **kwargs):
		print('{}'.format(original_func.__name__))
		return original_func(*args, **kwargs)
	
	return wrapper
	
def display():
	print('Display function')
	
display = decorator_func(display)

print(help(wraps))