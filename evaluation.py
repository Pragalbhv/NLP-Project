from util import *
import math
# Add your import statements here




class Evaluation():
	def _init_(self):
			self.ground_truth = None

	def queryPrecision(self, query_doc_ids_ordered, query_id, true_doc_ids, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the ids of documents in
			their predicted order of relevance to a query
		arg2 : int
			The id of the query in question
		arg3 : list
			The list of ids of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""

		precision = len(list(set(query_doc_ids_ordered[:k]).intersection(true_doc_ids))) / k

		#Fill in code here

		return precision


	def meanPrecision(self, doc_ids_ordered, query_ids, qrels, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of ids
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of ids of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean precision value as a number between 0 and 1
		"""

		precision_sum=0
		for i in range(len(query_ids)):
			precision_sum+=self.queryPrecision(doc_ids_ordered[i], query_ids[i], doc_list(query_ids[i],qrels), k)
			meanPrecision = precision_sum / len(query_ids)


		#Fill in code here

		return meanPrecision

	
	def queryRecall(self, query_doc_ids_ordered, query_id, true_doc_ids, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the ids of documents in
			their predicted order of relevance to a query
		arg2 : int
			The id of the query in question
		arg3 : list
			The list of ids of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""

		try:
			recall = len(list(set(query_doc_ids_ordered[:k]).intersection(true_doc_ids))) / len(true_doc_ids)
		except :
			recall = 0
			print(query_id, true_doc_ids)
		return recall


	def meanRecall(self, doc_ids_ordered, query_ids, qrels, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of ids
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of ids of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean recall value as a number between 0 and 1
		"""

		recall_sum = 0
		for i in range(len(query_ids)):
				recall_sum += self.queryRecall(doc_ids_ordered[i], query_ids[i],doc_list(query_ids[i], qrels), k)
		meanRecall = recall_sum / len(query_ids)
		return meanRecall


	def queryFscore(self, query_doc_ids_ordered, query_id, true_doc_ids, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the ids of documents in
			their predicted order of relevance to a query
		arg2 : int
			The id of the query in question
		arg3 : list
			The list of ids of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The fscore value as a number between 0 and 1
		"""

		precision = self.queryPrecision(query_doc_ids_ordered, query_id, true_doc_ids, k)
		recall = self.queryRecall(query_doc_ids_ordered, query_id, true_doc_ids, k)
		if precision == 0 and recall == 0:#prevent the zero division error
			fscore = 0
		else:
			fscore = 2 * ((precision * recall) / (precision + recall))
		return fscore

		#Fill in code here



	def meanFscore(self, doc_ids_ordered, query_ids, qrels, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of ids
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of ids of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value
		
		Returns
		-------
		float
			The mean fscore value as a number between 0 and 1
		"""

		meanFscore = -1
		fscore_sum = 0
		for i in range(len(query_ids)):
			fscore_sum += self.queryFscore(doc_ids_ordered[i], query_ids[i],doc_list(query_ids[i], qrels), k)
		meanFscore = fscore_sum / len(query_ids)
		return meanFscore
	

	def queryNDCG(self, query_doc_ids_ordered, query_id, true_doc_ids, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the ids of documents in
			their predicted order of relevance to a query
		arg2 : int
			The id of the query in question
		arg3 : list
			The list of ids of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The nDCG value as a number between 0 and 1
		"""

		nDCG = -1

		# Fill in code here
		relevance = {}
		DCG = 0
		# Since only 4 positions, starting from 4 for first position and decreasing for
		# each position, the one at position at 4 is given a relevance of 1
		MAXIMUM_RELEVANCE = 5

		DCG = 0
		iDCG = 0
		ground_truth = self.ground_truth
		if ground_truth == None:
				raise "Ground truth relevance scores not populated"
		ground_truth_ids = ground_truth.keys()
		for i, docid in enumerate(query_doc_ids_ordered[:k]):
				if docid in ground_truth_ids:
						DCG += (MAXIMUM_RELEVANCE - ground_truth[docid]) / math.log2(i + 2)
		
		sorted_ground_truths = sorted(ground_truth, key=ground_truth.get)[:k]
		for i, docid in enumerate(sorted_ground_truths):
				iDCG += (MAXIMUM_RELEVANCE - ground_truth[docid]) / math.log2(i + 2)
		nDCG = DCG / iDCG
		return nDCG

		#Fill in code here

		# return nDCG


	def meanNDCG(self, doc_ids_ordered, query_ids, qrels, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of ids
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of ids of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean nDCG value as a number between 0 and 1
		"""

		meanNDCG = -1

		# Fill in code here
		NDCGs = []

		for query_id, query_doc_ids_ordered in zip(query_ids, doc_ids_ordered):
				self.ground_truth = dict((int(rel["id"]), int(rel["position"])) for rel in qrels if int(rel["query_num"]) == int(query_id))
				NDCGs.append(
						self.queryNDCG(
								query_doc_ids_ordered,
								query_id,
								self.ground_truth.keys(),
								k
						)
				)

		if len(NDCGs) > 0:
				meanNDCG = sum(NDCGs) / len(NDCGs)
		return meanNDCG


	def queryAveragePrecision(self, query_doc_ids_ordered, query_id, true_doc_ids, k):
		"""
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the ids of documents in
			their predicted order of relevance to a query
		arg2 : int
			The id of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""

		count=1
		precision_sum=0
		avgPrecision = -1
		for i in range(k):
						try:
							if query_doc_ids_ordered[i] in true_doc_ids:
									count+=1
									precision_sum += self.queryPrecision(query_doc_ids_ordered, query_id, true_doc_ids, i+1)
						except: 
							count=k #end has been reached
							break

		#Fill in code here
		avgPrecision= precision_sum / count

		return avgPrecision


	def meanAveragePrecision(self, doc_ids_ordered, query_ids, q_rels, k):
		"""
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of ids
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of ids of the queries
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The MAP value as a number between 0 and 1
		"""

		# meanAveragePrecision = -1
		avgPrecision_sum=0
		for i in range(len(query_ids)):
				avgPrecision_sum += self.queryAveragePrecision(doc_ids_ordered[i], query_ids[i], doc_list(query_ids[i],q_rels), k)
		meanAveragePrecision = avgPrecision_sum/len(query_ids)
		#Fill in code here

		return meanAveragePrecision

