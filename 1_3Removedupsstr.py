#python ~/Documents/'more applications'/ElementsofProgrammingInterviews/CrackingTheCodingInterview/Chapter1/1_3Removedupsstr.py

#1.3 Design an algorithm and write a code to remove the duplicate characters in a string without using any additional buffer
def RemoveDups(string)->str:
	mlist=list(string)
	n=len(string)
	last=n-1
	for idx in range(n):
		for idxj in range(idx+1,n):
			if mlist[idx]==mlist[idxj]:
				mlist[idxj]='0'
	#print('mlist',mlist)
	sol=''.join([x for x in mlist if x!='0'])
	#print('so',sol)
	return sol
				
		



if __name__=='__main__':
	print('Remove dups in a string')
	mstring='string with dups'
	mstring2='aabb  cc dd'
	print('Original string',mstring2)
	print('sol: ',RemoveDups(mstring2))
