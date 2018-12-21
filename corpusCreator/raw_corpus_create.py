import os.path
import re
from util.FileReadWrite import FileReadWrite

def traverse_folder((ext, pathToWrite), dirname, names):
    ext = ext.lower()

    for file_name in names:
        if file_name.lower().endswith(ext):
            print (dirname)
            processed_file_path=process_file_path(dirname)+".java"

            print(os.path.join(dirname, file_name))
            file_content=file_read_write.fileReadSingle(os.path.join(dirname, file_name))
            print file_content

            process_file_content=processFileContent(file_content)
            print (process_file_content)
            print (pathToWrite+'/'+file_name)
            file_read_write.writeFiles(pathToWrite+'\\'+file_name, process_file_content)
            #file_read_write.writeFiles(pathToWrite+processed_file_path, process_file_content)
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
def process_file_path (file_path):
    #print (file_path.rfind('/'))
    print(file_path)
    file_path_new=file_path.replace("\\", ",")
    print(file_path_new)

    list=[]
    for match in re.finditer(',', file_path_new):
        print (match.start(), match.end())
        list.append(str(match.end()))

    print (str(list[6]))


    file_address=file_path_new[int(list[5]): ]
    file_address_new= file_address.replace(",",".")
    print (file_address_new)
    #print (file_address)
    return file_address_new
corpus='SWT'
topdir = 'E:\PhD\LSI\Repo\\'+corpus+'\Source\swt-3.659BLA\\'
exten = '.java'
pathToWrite = 'E:\PhD\LSI\Repo\\'+corpus+'\\ProcessedSourceCorpusDec19\\'

file_read_write=FileReadWrite(topdir)
os.path.walk(topdir, traverse_folder, (exten, pathToWrite))

