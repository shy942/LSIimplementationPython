from corpusCreator.source_corpus_creator import sourceCorpusCreator
from semanticpy.vector_space import VectorSpace, TFIDF, LSA
from semanticpy.LSIsearch import LSI_search
from util.FileReadWrite import FileReadWrite
from operator import itemgetter
from collections import OrderedDict


def Find_how_much_related(query_content_all, file_path_all, document_ID_file_info_mapping):
    #Retrieve the .txt files which are bug report
    bugIDfiles=[]
    #for content in source_file_path_info:
     #   if '.txt' in content:
      #      print (content)
    query_no=1
    for key in document_ID_file_info_mapping:

        if '.txt' in key:
            print ('Fuck you ' + key + ' ' + document_ID_file_info_mapping[key])
            documnet_id=document_ID_file_info_mapping[key]
            doc_id=int(documnet_id)
            query=query_content_all[key]
            content = []
            for word in query.split():
                content.append(word)
            #print (vector_space.relatedBySVDmatrix(doc_id))
            #resultPerQuery = vector_space.relatedBySVDmatrix(doc_id)
            resultPerQuery=vector_space.searchInSVDmatrix(content)
            sorted_result_per_query = create_result_output(resultPerQuery)
            print (sorted_result_per_query)
            writeToFile(sorted_result_per_query, 10, file_path_all, key, query_no)
            query_no = query_no + 1



# Do the searching
def LSI_search_method(query_content_all, vector_space, source_file_path_info, query_file_path_info):
    query_no=0
    for query in query_content_all:
        #queryInList=query.split()
        content=[]
        for word in query.split():
              content.append(word)
        #print (vector_space.searchInSVDmatrix(content))
        resultPerQuery=vector_space.searchInSVDmatrix(content)
        sorted_result_per_query=create_result_output(resultPerQuery)
        #writeToFile (sorted_result_per_query, 10, source_file_path_info, query_file_path_info[query_no], query_no+1)
        query_no=query_no+1




# Final Result
def create_result_output( resultPerQuery):
    result_content_per_query={}
    sorted_result_per_query={}
    index=0
    for each_result in resultPerQuery:
        result_content_per_query [index]=each_result
        index = index + 1
    print (result_content_per_query)
    sorted_result_per_query = get_sorted_result(result_content_per_query)
    return sorted_result_per_query


# return top-K result with index
def get_sorted_result(result_content_per_query):
    sorted_result=sorted(result_content_per_query.items(), key=itemgetter(1), reverse=True)
    return  sorted_result



def writeToFile(sorted_result_per_query, topK, source_file_path_info, query_file_name, query_no):
    #print (sorted_result_per_query)
    #print (source_file_path_info)
    contentToWrite=''
    queryID=query_file_name

    queryID=queryID[:-4]
    print (queryID)
    index=0;
    for (i, j) in sorted_result_per_query:
        if '.txt' not in source_file_path_info[i]:
            print source_file_path_info[i], j
            processed_file_address=process_file_path(source_file_path_info[i])
            print queryID, processed_file_address, j

            content = queryID + ',' + processed_file_address + ',' +str(j)
                #contentToWrite.append(conetnt)
            contentToWrite = contentToWrite + content + '\n'
            if index > topK-2:
                break
            index = index + 1
    print (contentToWrite)
    file_read_write.writeFiles('E:\PhD\LSI\Repo\\'+corpus+'\data\Results/'+str(query_no)+'.txt', contentToWrite)

def process_file_path (file_path):
    #print (file_path.rfind('/'))
    firstIndex=file_path.rfind('\\')
    print (file_path)
    file_address=file_path[firstIndex + 1: ]
    print (file_address)
    #print (file_address)
    return file_address


def find(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i


# Create the corpus
file_content_all=[]
corpus='Eclipse'
creator = sourceCorpusCreator()
sourcepath = "E:\PhD\LSI\Repo\\"+corpus+"\SourceAndBug\\"
keywordsfilepath='E:\PhD\LSI\Repo\\'+corpus+'\data\keyword-documents.txt'
querypath="E:\PhD\LSI\Repo\\"+corpus+"\BugData\\"
source_content_all={}
source_content_all=creator.CorpusCreatorDict(sourcepath, '.java')


print ('Total files in corpus ')
print(len(source_content_all))
print (source_content_all)

vector_space = VectorSpace(source_content_all)
file_path_all=vector_space.get_file_path_all()
print (file_path_all)
document_ID_file_info_mapping=vector_space.get_document_ID_file_info_mapping()
print (document_ID_file_info_mapping)
keywords_docs_string=str(vector_space.vector_index_to_keyword_mapping)
file_read_write=FileReadWrite(sourcepath)
file_read_write.writeFiles(keywordsfilepath, keywords_docs_string)
print (len(vector_space.vector_index_to_keyword_mapping))
#import pdb
#pdb.set_trace()
print ("Keyords-document vector/matrix")
print vector_space.collection_of_document_term_vectors

document_term_matrix=vector_space.collection_of_document_term_vectors
document_ID_file_info_mapping=vector_space.get_document_ID_file_info_mapping()
# Create LSI model using TF-IDF model
tf_idf = TFIDF(document_term_matrix)
tf_idf_transformated_matrix=tf_idf.transform()

#print tf_idf_transformated_matrix
lsa=LSA(tf_idf_transformated_matrix)
#lsa = LSA(tf_idf_transformated_matrix)
SVD_LSI_matrix=lsa.transform()
print ("After applying SVD")
print (SVD_LSI_matrix)
#print ("Create a instance of tranformed matrix in vector_space class?")
vector_space.setTransform(SVD_LSI_matrix)

# Create query corpus
query_content_all=creator.CorpusCreatorDict(querypath, '.txt')
query_file_path_info=creator.getFileP()
print (query_file_path_info)
print (query_content_all)
#import pdb
#pdb.set_trace()
file_read_write.writeFiles('E:\PhD\LSI\Repo\\'+corpus+'\data\source_info.txt', str(file_path_all))
#LSI_search_method(query_content_all, vector_space, source_file_path_info, query_file_path_info)
#print ("How relates a given documents with all other documents")
# Show score for relatedness against document 1
Find_how_much_related(query_content_all, file_path_all, document_ID_file_info_mapping)

