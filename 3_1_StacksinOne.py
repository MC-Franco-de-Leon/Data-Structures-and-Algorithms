#python ~/Documents/'more applications'/ElementsofProgrammingInterviews/CrackingTheCodingInterview/Chapter3/3_1_StacksinOne.py

#3.1 Single array to implement 3 stacks 

def push(stack_num:int, value :int)->None:
	idx=stack_num*stack_size+stack_pointer[stack_num]
	stack_pointer[stack_num]+=1
	mbuffer[idx]=value
def pop(stack_num:int)->int:
	idx=stack_num*stack_size+stack_pointer[stack_num]-1
	stack_pointer[stack_num]-=1
	val=mbuffer[idx]
	mbuffer[idx]=None
	return val
def peek(stack_num)->int:
	idx=idx=stack_num*stack_size+stack_pointer[stack_number]-1
	return mbuffer[idx]


	
def printm():
	print('new print')
	for element in mbuffer2:
		print(element.value)


if __name__=='__main__':
	print('Implement 3 stacks in one array')
	stack_size=10
	mbuffer=[0 for _ in range(stack_size*3)]
	stack_pointer=[0,0,0]
	push(0,10)
	push(0,9)
	push(0,8)
	push(0,7)
	push(1,10)
	push(1,9)
	push(2,10)
	push(2,9)
	print(mbuffer)
	pop(0)
	pop(0)
	pop(2)
	push(0,5)
	print(mbuffer)
	print(mbuffer)

	index_used=0
	stack_pointer2=[0,0,0]
	
	print('new buffer')
	class Stack_Node:
		def __init__(self, prev=None, value=None):
			self.value=value
			self.prev=prev
	mbuffer2=[Stack_Node(None, None) for _ in range(stack_size*3)]
	def push2(stack_num: int, value: int)->None:
		global index_used, stack_pointer2
		last_index=stack_pointer2[stack_num]
		stack_pointer2[stack_num]=index_used
		index_used+=1
		mbuffer2[stack_pointer2[stack_num]]=Stack_Node(last_index,value)
		print('pointers',stack_pointer2)
	def pop2(stack_num:int)->int:
		global index_used, stack_pointer2
		last_idx=stack_pointer2[stack_num]
		temp=mbuffer2[last_idx].value
		stack_pointer2[stack_num]=mbuffer2[last_idx].prev
		mbuffer2[last_idx]=Stack_Node(None,None)
		index_used-=1
		print('pointers',stack_pointer2)
		return temp

	#print(mbuffer2)
	push2(0,10)
	push2(0,9)
	push2(0,8)
	push2(0,7)
	push2(0,6)
	push2(1,11)
	push2(2,10)
	push2(2,9)
	#print(mbuffer2)
	printm()

	pop2(1)
	print('pop ',pop2(0))
	print('pop',pop2(0))
	pop2(2)
	
	printm()
	

