from util import *

# Add your import statements here




class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = None

		#Fill in code here
		tottext=[]
		intext=[]
		t=''
		word=''
		for i in range(len(text)):
			t=text[i].lower()
			for j in range(len(t)):
				if t[j]!=' ':
					word=word+t[j]
				if t[j]==' ':
					intext.append(word)
					word=''
			tottext.append(intext)
			intext=[]
		tokenizedText=tottext

		return tokenizedText



	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = None

		import nltk
		from nltk.tokenize import WordPunctTokenizer
		tokenizer = WordPunctTokenizer()
		tottext=[]
		intext=[]
		
		for i in range(len(text)):
			print(text[i])
			intext=tokenizer.tokenize(text[i])
			tottext.append(intext)
			intext=[]
		tokenizedText=tottext
		
		return tokenizedText