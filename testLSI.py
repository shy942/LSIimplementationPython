

from semanticpy.vector_space import VectorSpace
from semanticpy.transform.tfidf import TFIDF
from semanticpy.transform.lsa import LSA
from util.FileReadWrite import FileReadWrite

#path = "E:/test/"  # type: str
sourcepath = "E:/PhD/Repo/Zxing/ProcessedSourceCorpus/"
file_read = FileReadWrite(sourcepath)
file_content = file_read.readFilesWordByWord(sourcepath, '.java')
print ("Testing file read")
print(file_content)

querypath="E:/PhD/Repo/Zxing/BugData/357-test.txt"
my_file_handle = open (querypath)
query=[]
query=my_file_handle.read()


vector_space = VectorSpace(file_content)
#["The cat in the hat disabled", "A cat is a fine pet ponies.", "Dogs and cats make good pets.","I haven't got a hat."]
# import pdb
# pdb.set_trace()
# Search for cat
print ("Keywords")
print vector_space.vector_index_to_keyword_mapping  # Show the keywords
keywords_docs = ''.join(vector_space.vector_index_to_keyword_mapping)
file = open('E:/test/keyword-documents.txt','w')
file.write(keywords_docs)
file.close()
print ("Keyords-document vector/matrix")
print vector_space.collection_of_document_term_vectors  # show the keyword-document vector/matrix)
document_vector = ''.join(str(e) for e in (vector_space.collection_of_document_term_vectors))
file2 = open('E:/test/document-vector.txt','w')
file2.write(document_vector)
file2.close()

print ("Keyords-document vector/matrix after applying TF-IDF")

tf_idf = TFIDF(vector_space.collection_of_document_term_vectors)
print tf_idf.transform()
print ("Searching for "+ query)
queryInList=query.split()
print (queryInList)
print vector_space.search(queryInList)
#print ("How relates a given documents with all other documents")
# Show score for relatedness against document 1
#print vector_space.related(1)

lsa = LSA(tf_idf.transform())
print ("After applying SVD")
print (lsa.transform())
print ("Can I print from VectorSpace now?")
print (vector_space.vector_index_to_keyword_mapping)
print ("Create a instance of tranformed matrix in vector_space class?")
print (vector_space.setTransform(lsa.transform()))
print ("Searching in the SVD matrix")
print (vector_space.searchInSVDmatrix(["language"]))