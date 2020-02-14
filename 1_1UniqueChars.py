#python ~/Documents/'more applications'/ElementsofProgrammingInterviews/CrackingTheCodingInterview/Chapter1/1_1UniqueChars.py

##1.1 Implement an algorithm to determine if a string has all unique characters

# Brute force for each char we check the rest to see if there is any repetition O(n**2) time and O(1) space

#With hash table we have O(n) time and O(n) space
from collections import defaultdict

def CheckUnique_Chars(string)-> bool:
	mdict=defaultdict(int)
	for char in string:
		mdict[char]+=1
		if mdict[char]>1:
			return False
	return True
def CheckUnique_Chars2(string)->bool:
	aux=0
	for char in string:
		val=ord(char)-ord('a')
		if aux & (1<<val)>0: return False
		aux=aux|(1<<val)
	return True	
if __name__=='__main__':
	print('Unique Characters')
	mstring1='my string m'
	mstring2='abcdefgtha'
	sol=CheckUnique_Chars2(mstring2)
	if sol:
		print('Chars are unique')
	else:
		print('Not unique')
