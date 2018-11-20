from functools import reduce

from semanticpy.parser import Parser
from semanticpy.transform.lsa import LSA
from semanticpy.transform.tfidf import TFIDF

import sys


try:
	from numpy import dot
	from numpy.linalg import norm
except:
	print ("Error: Requires numpy from http://www.scipy.org/. Have you installed scipy?")
	sys.exit() 

class VectorSpace:
    """ A algebraic model for representing text documents as vectors of identifiers. 
    A document is represented as a vector. Each dimension of the vector corresponds to a 
    separate term. If a term occurs in the document, then the value in the vector is non-zero.
    """

    collection_of_document_term_vectors = []
    documents=[]
    file_path_all=[]
    document_ID_file_info_mapping=[]
    vector_index_to_keyword_mapping = []
    document_ID_file_info_mapping={}
    transformed_matrix=[]
    parser = None

    def __init__(self, documents = [], transforms = [TFIDF, LSA]):
    	self.collection_of_document_term_vectors = []

        self.transformed_matrix = []
    	self.parser = Parser()
    	if len(documents) > 0:
    		self._build(documents, transforms)

    def __init__(self, documentsdict={}, transforms = [TFIDF, LSA]):
    	self.collection_of_document_term_vectors = []
        self.documents = []
        self.file_path_all=[]
        self.document_ID_file_info_mapping={}
        self.transformed_matrix = []
    	self.parser = Parser()

        self._addToList(documentsdict)
    	if len(self.documents) > 0:
    		self._build(self.documents, transforms)

    def _addToList(self,documents_dict):
        i=1;
        for key in documents_dict:
            self.documents.append(documents_dict[key])
            self.file_path_all.append(key)
            self.document_ID_file_info_mapping[key] = str (i)
            print key, i
            i=i+1

    def get_file_path_all(self):
        return self.file_path_all

    def get_document_ID_file_info_mapping(self):
        return  self.document_ID_file_info_mapping

    def related(self, document_id):
        """ find documents that are related to the document indexed by passed Id within the document Vectors
        How one given document is related to all other documents"""
        ratings = [self._cosine(self.collection_of_document_term_vectors[document_id], document_vector) for document_vector in self.collection_of_document_term_vectors]
        #import pdb
        #pdb.set_trace()
        #ratings.sort(reverse = True)
        return ratings

    def relatedBySVDmatrix(self, document_id):
        #import pdb
        #pdb.set_trace()
        print (self.collection_of_document_term_vectors[document_id])
        ratings = [self._cosine(self.collection_of_document_term_vectors[document_id], document_vector) for document_vector in self.transformed_matrix]
        return ratings

    def setTransform(self, transforms):
        self.transformed_matrix=transforms
        return self.transformed_matrix

    def searchInSVDmatrix(self, searchList):
        queryVector = self._build_query_vector(searchList)
        print (queryVector)
        ratings = [self._cosine(queryVector, documentVector) for documentVector in self.transformed_matrix]
        return ratings

    def search(self, searchList):
        """ search for documents that match based on a list of terms """
        queryVector = self._build_query_vector(searchList)

        ratings = [self._cosine(queryVector, documentVector) for documentVector in self.collection_of_document_term_vectors]
        #import pdb
        #pdb.set_trace()
        #ratings.sort(reverse=True)
        return ratings


    def _build(self, documents, transforms):
    	""" Create the vector space for the passed document strings """
        print ('from vector_space class')
        print(documents)
    	self.vector_index_to_keyword_mapping = self._get_vector_keyword_index(documents)
        #import pdb
        #pdb.set_trace()

    	matrix = [self._make_vector(document) for document in documents]
        #import pdb
        #pdb.set_trace()
        #matrix = reduce(lambda matrix,transform: transform(matrix).transform(), transforms, matrix)
        self.collection_of_document_term_vectors = matrix

    def _get_vector_keyword_index(self, document_list):
    	""" create the keyword associated to the position of the elements within the document vectors """
    	vocabulary_list = self.parser.tokenise_and_remove_stop_words(document_list)
        unique_vocabulary_list = self._remove_duplicates(vocabulary_list)
		
    	vector_index={}
    	offset=0
    	#Associate a position with the keywords which maps to the dimension on the vector used to represent this word
    	for word in unique_vocabulary_list:
    		vector_index[word] = offset
    		offset += 1
    	return vector_index  #(keyword:position)

    def _make_vector(self, word_string):
    	""" @pre: unique(vectorIndex) """

    	vector = [0] * len(self.vector_index_to_keyword_mapping)

    	word_list = self.parser.tokenise_and_remove_stop_words(word_string.split(" "))

    	for word in word_list:
            if(word in self.vector_index_to_keyword_mapping):
                vector[self.vector_index_to_keyword_mapping[word]] += 1; #Use simple Term Count Model
    	return vector


    def _build_query_vector(self, term_list):
    	""" convert query string into a term vector """
    	query = self._make_vector(" ".join(term_list))
    	return query


    def _remove_duplicates(self, list):
        """ remove duplicates from a list """
        return set((item for item in list))
    
        
    def _cosine(self, vector1, vector2):
    	""" related documents j and q are in the concept space by comparing the vectors :
    		cosine  = ( V1 * V2 ) / ||V1|| x ||V2|| """
    	return float(dot(vector1,vector2) / (norm(vector1) * norm(vector2)))
