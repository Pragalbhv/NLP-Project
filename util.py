# Add your import statements here
def doc_list(query_id, qrels):
    
    true_doc_IDs = []
    for query_dict in qrels:
        if int(query_dict['query_num']) == query_id:
            true_doc_IDs.append(int(query_dict['id']))
    return true_doc_IDs


def dict_list(query_id, qrels):
    """
    this function gives list of dictionaries which are relevant to a given query
    :param query_id: int
                    query no for which we are intrested
    :param qrels: list of dict
                    obtained from qrels.json
    :return: rel_list: list of dict
                    subset of qrels which have re for a single query
    """
    rel_list = []
    for query_dict in qrels:
        if int(query_dict['query_num']) == query_id:
            rel_list.append(query_dict)

    return rel_list


def scoremake(pred_list, rel_list):
    """
     this is a helper function used to covert scores in qrels.json to 5,4,3,2,1,0 format with 5 being most relevant
     and 0 being not relevant
    :param pred_list:list of int
                        list of docIDs for which score is needed
    :param rel_list: list of dict
                        list of dictionaries for a given query
    :return: a list in which ith entry is score of ith docID in pred_list
    """
    score_list = []
    for pred_id in pred_list:
        p = 0
        for query_dict in rel_list:
            if int(query_dict['id']) == pred_id:
                p = 1
                score_list.append(5 - int(query_dict['position']))
                break
        if p == 0:
            score_list.append(0)
    return score_list

# Add your import statements here
import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import seaborn as sns


# Add any utility functions here

def build_word_index(docs,doc_ids):
    corpora = [] # a list of words
    #word_map = {}
    for doc in docs:
        for sent in doc:
            for word in sent:
                corpora.append(word)
    corpora = set(corpora)  # unique words
    word_map = {word : idx for idx,word in enumerate(set(corpora),0)} # for assigning a unique label to each word

    return word_map






# Add any utility functions here