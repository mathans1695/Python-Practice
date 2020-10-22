def prefix_func(prefix):
	def decorator_func(original_func):
		def wrapper_func(*args, **kwargs):
			print(prefix, ':' 'Wrapper function got executed with the original function: {}'.format(original_func.__name__))
			return original_func(*args, **kwargs)
		return wrapper_func
	return decorator_func
	

@prefix_func('/')
def display():
	print('Display function executed')
	
display()