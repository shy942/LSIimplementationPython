import os.path
import re
from util.FileReadWrite import FileReadWrite

def traverse_folder((ext, pathToWrite), dirname, names):
    ext = ext.lower()

    for file_name in names:
        if file_name.lower().endswith(ext):

            print(os.path.join(dirname, file_name))
            file_content=file_read_write.fileReadSingle(os.path.join(dirname, file_name))
            print file_content

            process_file_content=processFileContent(file_content)
            print (process_file_content)
            file_read_write.writeFiles(pathToWrite+'/'+file_name, process_file_content)
            #import pdb
            #pdb.set_trace()


def processFileContent(file_content):
    # removing special characters
    process_file_content = re.sub('[^A-Za-z0-9]+', ' ', file_content)

    # spliting program identifiers
    processd_final_content=str()
    for word in process_file_content.split():
        processed_word_list=re.findall('[A-Z][^A-Z]*', word)
        if(len(processed_word_list)>0):
            print (processed_word_list)
            for word in processed_word_list:
                if(len(word)>1):
                    print (word)
                    processd_final_content = processd_final_content + word.lower() + ' '
    return processd_final_content

corpus='AspectJ'
topdir = 'E:\PhD\LSI\Repo\\'+corpus+'\Source\ibugs_aspectj-1.3\ibugs_aspectj-1.3'
exten = '.java'
pathToWrite = 'E:\PhD\LSI\Repo\\'+corpus+'\processedSourceCodesibugs_aspectj-1.3'

file_read_write=FileReadWrite(topdir)
os.path.walk(topdir, traverse_folder, (exten, pathToWrite))

