#python ~/Documents/'more applications'/ElementsofProgrammingInterviews/CrackingTheCodingInterview/Chapter3/3_3_SetOfStacks.py

#3.3 Implement a data structure set of stacks that creates a new stack when a given one exceeds a threshold. we must perform pop and push as a regular stack and pop at index
# follow up, implement remove at idx

class SetofStacks:
	threshold=4
	def __init__(self,value):
		self.SetofStacks=[[value]]
		self.curridx=0
		self.nstacks=1
	def push(self, value):
		if len(self.SetofStacks[self.nstacks-1])>=self.threshold:
			self.SetofStacks.append([value])
			self.nstacks+=1
		else:
			self.SetofStacks[self.nstacks-1].append(value)
		self.curridx+=1
	def pop(self):
		n=len(self.SetofStacks[self.nstacks-1])
		if self.nstacks>0:
			if n>1:
				self.SetofStacks[self.nstacks-1].pop()
			else:
				self.SetofStacks.pop()
				self.nstacks-=1
			self.curridx-=1
			
	def printstacks(self):
		for stack in self.SetofStacks:
			print('Another stack', stack)
			
			
		

if __name__=='__main__':
	print('Set of Stacks')
	Stacks=SetofStacks(10)
	Stacks.push(9)
	Stacks.push(8)
	Stacks.push(7)
	Stacks.push(6)
	Stacks.push(5)
	Stacks.push(4)
	Stacks.push(3)
	Stacks.push(2)
	Stacks.printstacks()
	print('pop')
	Stacks.pop()
	Stacks.pop()
	Stacks.pop()
	Stacks.pop()
	Stacks.pop()
	Stacks.printstacks()
	
	
