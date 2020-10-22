class Counter:
	
	def __init__(self):
		self.count = 0
		
	def display(self):
		print(self.count)
		
	def reset(self):
		self.count = 0
		self.display()
		
	def push(self):
		self.count += 1
		self.display()


