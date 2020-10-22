from functools import wraps

def logger_dec(original_func):
	import logging
	logging.basicConfig(filename='{}.log'.format(original_func.__name__), level=logging.DEBUG)
	
	@wraps(original_func)
	def wrapper(*args, **kwargs):
		print('Executed')
		logging.debug('Wrapper function is running through: {}:Aruguments:{}:{}'.format(original_func.__name__, args, kwargs))
		print('Wrapper function executed: {}'.format(original_func.__name__))
		return original_func(*args, **kwargs)
	return wrapper
	
def time1(original_func):
	import time
	
	@wraps(original_func)
	def wrapper(*args, **kwargs):
		start = time.time()
		result = original_func(*args, **kwargs)
		end = time.time()
		print('Wrapper function executed: {}'.format(original_func.__name__))
		print(end - start)
		return result
	return wrapper

@logger_dec
@time1
def display(name, age):
	import time
	time.sleep(1)
	print('Display function is running')
	print('Name: {} and Age: {}'.format(name, age))
	
display('Maha', 30)