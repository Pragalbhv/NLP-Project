from util import *

# Add your import statements here




class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""

		segmentedText = None
		list1=[]
		sent=""
		for i in range(len(text)):
			if text[i]!='.' and text[i]!='?' and text[i]!='!' :
				sent=sent+text[i]
	#             print([text[i]+sent])
			elif text[i]=='.' or text[i]=='?' or text[i]=='!':
				#insert more tests for abbreviations, etc.
				list1.append(sent)
				sent=""
        
        
		segmentedText=list1

		#Fill in code here

		return segmentedText





	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""

		segmentedText = None

		import nltk
		from nltk.tokenize import PunktSentenceTokenizer
		tokenizer = PunktSentenceTokenizer()
		segmentedText=tokenizer.tokenize(text)
		
		return segmentedText