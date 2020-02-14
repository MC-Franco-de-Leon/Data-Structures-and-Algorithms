#python ~/Documents/'more applications'/ElementsofProgrammingInterviews/CrackingTheCodingInterview/Chapter2/2_3delnodeinLL.py

#2.3 Implement an algorithm to delete a node in the middle of a single LL, given only access to that node

class node:
	def __init__(self,data=None,next=None):
		self.data=data
		self.next=next
class LL:
	def __init__(self,data=None,next=None):
		self.root=node(data,next)
	def addnode(self, data):
		new=node(data, self.root)
		self.root=new
	def delnode(self,curr):
		if curr==self.root:
			if curr.next:
				self.root=curr.next
			else:
				self.root=None
		else:
			
			if curr.next:
				curr.data=curr.next.data
				curr.next=curr.next.next
			else:
				curr=None
		
		
def printLL(root):
	curr=root
	print('Newlist')
	while curr:
		print(curr.data)
		curr=curr.next

if __name__=='__main__':
	print('delete node')
	mLL=LL(10)
	mLL.addnode(9)
	mLL.addnode(8)
	mLL.addnode(7)
	mLL.addnode(6)
	mLL.addnode(5)
	mLL.addnode(4)
	mLL.addnode(3)
	mLL.addnode(2)
	mLL.addnode(1)
	printLL(mLL.root)
	print('root',mLL.root.data)
	mLL.delnode(mLL.root)
	mLL.delnode(mLL.root.next.next.next.next.next.next.next)
	printLL(mLL.root)

