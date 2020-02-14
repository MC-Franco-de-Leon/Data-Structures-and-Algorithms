#python ~/Documents/'more applications'/ElementsofProgrammingInterviews/CrackingTheCodingInterview/Chapter1/1_2ReverseC_style.py

##1.2 Write a code to reverse a C-Style String
def ReverseRec(string)->str:
	if len(string)<=1:
		return string
	return ReverseRec(string[1:])+(string[0])
def Reverse2(string)->str:
	mlist=list(string)
	n=len(string)//2

	for i in range(n):
		aux=mlist[i]
		mlist[i]=mlist[~i]
		mlist[~i]=aux
	return ''.join(mlist)
	
	
if __name__=='__main__':
	print('Revrse C-Style')
	mstring='string1'
	print('dE reversa', ReverseRec(mstring))
	print('dE reversa 2', Reverse2(mstring))
