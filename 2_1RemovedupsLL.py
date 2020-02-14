#python ~/Documents/'more applications'/ElementsofProgrammingInterviews/CrackingTheCodingInterview/Chapter2/2_1RemovedupsLL.py

#1.1 Write a code to remove duplicates from an unsorted linked list


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
	def printLL(self):
		print('New print')
		curr=self.root
		while curr:
			print(curr.data)
			curr=curr.next
	def RemoveDups(self):
		curri=self.root
		while curri:
			vali=curri.data
			prev=curri
			currj=curri.next
			while currj:
				if vali==currj.data:
					prev.next=currj.next
				else:
					prev=currj
				currj=currj.next	
					
			curri=curri.next
		return self.root
		

if __name__=='__main__':
	print('remove duplicates from unsorted linked list')
	mLL=LL(0)
	mLL.addnode(1)
	mLL.addnode(1)
	mLL.addnode(1)
	mLL.addnode(2)
	mLL.addnode(1)
	mLL.addnode(2)
	mLL.addnode(2)
	mLL.printLL()
	mLL.RemoveDups()
	mLL.printLL()
