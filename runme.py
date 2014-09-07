# -*- coding: utf-8 -*-

def haveSameLetters(dest , norm):
	
	dlst = list(dest)
	nlst = list(norm)
	dlst.sort()
	nlst.sort()

	for i in range(len(dlst)):
		if dlst[i] != nlst[i] :
			return False
	return True
	

def main():
	print "Πατήστε ENTER για να τερματίσετε το πρόγραμμα."
	scrambled = raw_input("Εισάγεται την ανακατεμένη λέξη. Το πρόγραμμα θα προσπαθήσει να βρεί τη λύση: ")
	while scrambled != "" :
		answerlist = [] 
		words = file("dict.txt" , "r").read().split()
		for normal in words:
			if len(normal) == len(scrambled) :
				if haveSameLetters(scrambled,normal):
					answerlist.append(normal)
		for i in range(len(answerlist)):
			print answerlist[i] 
		scrambled = raw_input("Εισάγεται την ανακατεμένη λέξη. Το πρόγραμμα θα προσπαθήσει να βρεί τη λύση: ")

if __name__ == "__main__": main()