#python ~/Documents/'more applications'/ElementsofProgrammingInterviews/CrackingTheCodingInterview/Chapter2/2_2nthtolast.py

#2.2 Implement an algorithm to find the nth to last element of a singly linked list

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
	def nthtolast(self,n):
		curr=self.root
		count=1
		while curr:
			if count==n:
				return curr
			count+=1
			curr=curr.next
def printLL(root):
	curr=root
	print('Newlist')
	while curr:
		print(curr.data)
		curr=curr.next


if __name__=='__main__':
	print('nth to last element')
	n=7
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
	newroot=mLL.nthtolast(n)
	printLL(newroot)
