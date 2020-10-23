class StudentFileReader:
	def __init__(self, inputSrc):
		self._inputSrc = inputSrc
		self._inputFile = None
		
	def open(self):
		self._inputFile = open(self._inputSrc, 'r')
		
	def close(self):
		self._inputFile.close()
		self._inputFile = None
		
	def fetchAll(self):
		theRecords = list()
		student = self.fetchRecord()
		
		while student != None:
			theRecords.append(student)
			student = self.fetchRecord()
		return theRecords
		
	def fetchRecord(self):
		line = self._inputFile.readline().split(', ')
		if line[0] == '':
			return None
			
		student = StudentRecord()
		student.idNum = int(line[0])
		student.firstName = line[1]
		student.lastName = line[2]
		student.classCode = int(line[3])
		student.gpa = float(line[4])
		return student
	
	def sort(self, sortBy='id'):
		
		self.open()
		self.theData = self.fetchAll()
		self.close()
		
		if sortBy == 'id':
			for i in range(len(self.theData)):
				small = self.theData[i].idNum
				for j in range(i+1, len(self.theData)):
					if small > self.theData[j].idNum:
						temp = self.theData[i]
						self.theData[i] = self.theData[j]
						self.theData[j] = temp
						small = self.theData[i].idNum
						
			self.display()
			
		elif sortBy == 'name':
			for i in range(len(self.theData)):
				small = self.theData[i].firstName
				for j in range(i+1, len(self.theData)):
					if small > self.theData[j].firstName:
						temp = self.theData[i]
						self.theData[i] = self.theData[j]
						self.theData[j] = temp
						small = self.theData[i].firstName
			
			self.display()
			
		else:
			print("Enter either id or name:")
			tem = input()
			self.sort(sortBy = tem)
		
	def display(self):
		print()
		print("{:^50}".format('LIST OF STUDENTS'))
		print()
		
		print("{:5}".format('ID'),end = '  ')
		print("{:25}".format('NAME'),end = '  ')
		print("{:10}".format('CLASS'),end = '  ')
		print("{:4}".format('GPA'))
		
		print("{:5}".format('-' * 5),end = '  ')
		print("{:25}".format('-' * 25),end = '  ')
		print("{:10}".format('-' * 10),end = '  ')
		print("{:4}".format('-' * 4))
		
		className = (None, 'Freshman', 'Sophomore', 'Junior', 'Senior')
		
		for i in range(len(self.theData)):
			
			print("{:5}".format(self.theData[i].idNum),end = '  ')
			
			name = "{}, {}".format(self.theData[i].firstName, self.theData[i].lastName)
			print("{:25}".format(name),end = '  ')
			
			print("{:10}".format(className[self.theData[i].classCode]),end = '  ')
			print("{:4.2f}".format(self.theData[i].gpa),end = '')
			print()
		
		print("{:50}".format('-' * 50 ))
					
class StudentRecord:
	def __init__(self):
		self.idNum = 0
		self.firstName = None
		self.lastName = None
		self.classCode = 0
		self.gpa = 0.0
		
class StudentFileWriter:
	def __init__(self, writeSrc):
		object = StudentFileReader(writeSrc)
		object.open()
		self.theData = object.fetchAll()
		object.close()
		
	def outputToFile(self, fileName='copy.txt'):
		self.theCopy = open(fileName, 'w')
		
		for i in range(len(self.theData)):
			
			self.theCopy.write(str(self.theData[i].idNum))
			self.theCopy.write(', ')
			self.theCopy.write(self.theData[i].firstName)
			self.theCopy.write(', ')
			self.theCopy.write(self.theData[i].lastName)
			self.theCopy.write(', ')
			self.theCopy.write(str(self.theData[i].classCode))
			self.theCopy.write(', ')
			self.theCopy.write(str(self.theData[i].gpa))
			self.theCopy.write('\n')
		
		return fileName
	
	def display(self):
		print()
		print("{:^50}".format('LIST OF STUDENTS'))
		print()
		
		print("{:5}".format('ID'),end = '  ')
		print("{:25}".format('NAME'),end = '  ')
		print("{:10}".format('CLASS'),end = '  ')
		print("{:4}".format('GPA'))
		
		print("{:5}".format('-' * 5),end = '  ')
		print("{:25}".format('-' * 25),end = '  ')
		print("{:10}".format('-' * 10),end = '  ')
		print("{:4}".format('-' * 4))
		
		className = (None, 'Freshman', 'Sophomore', 'Junior', 'Senior')
		
		for i in range(len(self.theData)):
			
			print("{:5}".format(self.theData[i].idNum),end = '  ')
			
			name = "{}, {}".format(self.theData[i].firstName, self.theData[i].lastName)
			print("{:25}".format(name),end = '  ')
			
			print("{:10}".format(className[self.theData[i].classCode]),end = '  ')
			print("{:4.2f}".format(self.theData[i].gpa),end = '')
			print()
		
		print("{:50}".format('-' * 50 ))
		
	def outputToFileInFormat(self, fileName='copy.txt'):
		self.theCopy = open(fileName, 'w')
		
		self.theCopy.write('\n')
		self.theCopy.write("{:^59}".format('LIST OF STUDENTS'))
		self.theCopy.write('\n')
		
		self.theCopy.write("{:8}".format('ID'))
		self.theCopy.write('    ')
		self.theCopy.write("{:25}".format('NAME'))
		self.theCopy.write('  ')
		self.theCopy.write("{:10}".format('CLASS'))
		self.theCopy.write('  ')
		self.theCopy.write("{:4}".format('GPA'))
		self.theCopy.write('\n')
		
		className = (None, 'Freshman', 'Sophomore', 'Junior', 'Senior')
		
		for i in range(len(self.theData)):
			
			self.theCopy.write("{:<5}".format(self.theData[i].idNum))
			self.theCopy.write('  ')
			
			name = "{}, {}".format(self.theData[i].firstName, self.theData[i].lastName)
			self.theCopy.write("{:25}".format(name))
			self.theCopy.write('  ')
			
			self.theCopy.write("{:10}".format(className[self.theData[i].classCode]))
			self.theCopy.write('  ')
			self.theCopy.write("{:4.2f}".format(self.theData[i].gpa))
			self.theCopy.write('\n')
