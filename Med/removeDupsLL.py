#remove duplicates from an unsorted, singly linked list
#bonus challenge: do so without using a buffer to store encountered values

class Node :
	def __init__( self, data ) :
		self.data = data
		self.next = None
		self.prev = None

class LinkedList :
	def __init__( self ) :
		self.head = None

	def add( self, data ) :
		node = Node( data )
		if self.head == None :
			self.head = node
		else :
			node.next = self.head
			node.next.prev = node
			self.head = node

	def search( self, k ) :
		p = self.head
		if p != None :
			while p.next != None :
				if ( p.data == k ) :
					return p
				p = p.next
			if ( p.data == k ) :
				return p
		return None

	def remove( self, p ) :
		tmp = p.prev
		p.prev.next = p.next
		p.prev = tmp

	def __str__( self ) :
		s = ""
		p = self.head
		if p != None :
			while p.next != None :
				s += p.data
				p = p.next
			s += p.data
		return s

	#simple sorting algorithm - kinda bad (it's no quicksort!) but okay for a proof of concept
	def sort(self):
		start = self.head
		beginNode = start
		while beginNode:
			tempNode = beginNode
			tempNode2 = beginNode
			smallest = beginNode.data
			while tempNode:
				if smallest > tempNode.data:
					smallest = tempNode.data
					tempNode2 = tempNode
				tempNode = tempNode.next

			temp = beginNode.data
			beginNode.data  = tempNode2.data
			tempNode2.data  = temp
			beginNode = beginNode.next

	#implementation that does use buffer - This is the most time efficient but isn't super
	#space efficient due to the buffer - see below for O(n Log n) solution that doesn't use any
	#additional space
	def removeDupsTimeEff(self):
		p = self.head
		#We use a dictionary to store previously encountered values,  it doesn't particularly matter
		#what the value is in the key/value pair, we only care about the ability to access whether or
		#not a node has been encountered (ie whether or not a key is in the dictionary) in O(1) time,
		#something that using an array as a buffer wouldn't allow us to do
		prevVals = {}
		while (p != None):
			if p.data in prevVals.keys():
				self.remove(p)
			else:
				prevVals[p.data] = True
			p = p.next
		return True

	#this implementation relies on the sorting algorithm being used being an efficient O(n log n) sort
	#mine isn't, but if it were this would be O(n log n). We rely on the sorting algorithm moving duplicates
	#next to each other - we simply remove all the duplicates until only one remains!
	def removeDupsSpaceEff(self):
		self.sort()
		p = self.head
		while(p.next != None):
			if p.data == p.next.data:
				self.remove(p.next)
			p = p.next


def main():
	l = LinkedList()

	l.add( 'a' )
	l.add( 'f' )
	l.add( 'b' )
	l.add( 'c' )
	l.add( 'f' )
	l.add( 'c' )
	print(l)
	l.removeDupsTimeEff()
	print(l)
	l.add( 'a' )
	l.add( 'b' )
	print(l)
	l.removeDupsSpaceEff()
	print(l)

main()
