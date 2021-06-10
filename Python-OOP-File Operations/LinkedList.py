class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
	
	def printList(self):
		temp = self.head
		while (temp):
			print(temp.data)
			temp = temp.next

	def push(self, data):
		new = Node(data)
		new.next = self.head
		self.head = new

	def insert(self, prev,  data):
		if prev is None:
			return 
		new = Node(data)
		new.next = prev.next
		prev.next = new

	def append(self, data):
		new = Node(data)
		if self.head is None:
			self.head = new
			return
		last = self.head
		while (last.next):
			last = last.next
		last.next = new

	def delete(self, key):
		temp = self.head
		if (temp is not None):
			if temp.data == key:
				self.head = temp.next
				temp = None
				return
		while (temp is not None):
			if temp == key:
				break
			prev = temp
			temp = temp.next
		if temp == None:
			return
		prev.next = temp.next
		temp = None

if __name__ == '__main__':

	llist = LinkedList()

	llist.push(3)

	llist.push(1)
		
	llist.push(2)
	
	llist.push(4)	
	
	llist.delete(2)

	llist.printList()		
