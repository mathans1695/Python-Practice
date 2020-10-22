# Creates abstract data types
# This class will be used to create linked list head node
class LinkedList:
	# Constructor which creates the head node
	def __init__(self):
		self.head = None
		
	# Returns the lenght of the linked list
	def __len__(self):
		count = 0
		temp = self.head
		
		# Iterates through list until next is none
		while temp:
			count += 1
			temp = temp.next
			
		return count
		
	# Insert a node at the given position
	def insert(self, position, data):
		# Getting the number of nodes
		count =  len(self)
		
		# Checks whether the given position is within the length
		assert position > count, "Given position is not in the list"
		
		if position == 1:
			temp = self.head
			self.head = Node(data)
			self.head.next = temp
			
		iter_count = 0
		temp = self.head
		
		while temp is not None:
			iter_count += 1
			if position == iter_count:
				break
				
			prev = temp
			temp = temp.next
		
			
		
	# This method will add the node to the front 
	def push(self, data):
		# Creating a node object
		new_node = Node(data)
		
		# Copying the head node reference to new_node
		new_node.next = self.head
		
		# Changing the head reference to new_node
		self.head = new_node
		
		
# This class will create nodes	
class Node:
	# Linked list should have space for data and reference
	def __init__(self, data):
		self.data = data
		self.next = None

# Instantiating linked list and node class		
llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)

# Assigning the second reference to head
llist.head.next = second

# Assigning the third reference to second
second.next = third

temp = llist.head

while temp:
	print(temp.data)
	temp = temp.next

print(llist.head)
print(len(llist))