#python ~/Documents/'more applications'/ElementsofProgrammingInterviews/CrackingTheCodingInterview/Chapter3/3_2_Stackwithmin.py

#3.2 design a stack which in addition to push and pop has min in O(1)



class node:
	def __init__(self, data=None, prevmin=None, next=None):
		self.data=data
		self.prevmin=prevmin
		self.next=next
class Stack():
	def __init__(self, data):
		self.root=node(data,None, None)
		self.currmin=data
	def push(self,data):
		new=node(data,self.currmin, self.root)
		if self.currmin>data:
			self.currmin=data
		self.root=new
	def pop(self):
		if self.root:
			self.currmin=self.root.prevmin
			self.root=self.root.next
	def printS(self):
		curr=self.root
		print('ptinritn')
		while curr:
			print(curr.data)
			curr=curr.next
	def min_s(self):
		return self.currmin

		

if __name__=='__main__':
	print('Stack with push, pop, min in O(1)')
	Stack=Stack(10)
	Stack.push(9)
	Stack.push(8)
	Stack.push(7)
	Stack.push(-1)
	Stack.push(9)
	Stack.push(8)
	Stack.push(7)
	Stack.push(6)
	Stack.printS()
	Stack.pop()
	Stack.pop()
	Stack.printS()
	print('min ',Stack.min_s())
	
