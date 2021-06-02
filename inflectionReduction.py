from util import *

# Add your import statements here




class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""


		reducedText = None

		import nltk
		from nltk.corpus import wordnet

		def wordnetpos(treebank_tag):

			if treebank_tag.startswith('J'):
				return wordnet.ADJ
			elif treebank_tag.startswith('V'):
				return wordnet.VERB
			elif treebank_tag.startswith('N'):
				return wordnet.NOUN
			elif treebank_tag.startswith('R'):
				return wordnet.ADV
			else:
				return wordnet.NOUN #default to prvent issue

		fintxt=[]
		lintxt=[]
		from nltk.stem import WordNetLemmatizer 
		lemmatizer = WordNetLemmatizer()
		for i in range(len(text)):
			tagged=nltk.pos_tag(text[i])
			for j in range(len(text[i])):
				
				lintxt.append(lemmatizer.lemmatize(text[i][j], wordnetpos(tagged[j][1])))
			fintxt.append(lintxt)
			lintxt=[]                
		reducedText=fintxt

		

		#Fill in code here
		
		return reducedText


