from util.FileReadWrite import FileReadWrite
def goldset_creator(git_content_list, list_of_source_files):
    content_to_write=''
    total_fixed_files_existed = 0
    count=0
    bugID=''
    no_of_files=0
    total_processed_file_path=''
    for line in git_content_list:
        #print (line)
        line_content=line.split()
        line_length=len(line_content)

        if(line_length==2):
            if (count > 0):
                print (no_of_files)
                print (total_fixed_files_existed)
                if(str(no_of_files) ==  str(total_fixed_files_existed)):
                    content_to_write = content_to_write + bugID +' '+ str(total_fixed_files_existed) + '\n' +total_processed_file_path
            bugID=line_content[0]
            no_of_files=line_content[1]
            total_fixed_files_existed = 0
            total_processed_file_path = ''
        if(line_length==1):
            file_path=line
            processed_file_path=process_file_path(file_path,'/')
            found=0
            for i in range(0, len(list_of_source_files)):
                source_path=list_of_source_files[i]+'\n'
                if(processed_file_path == source_path):
                    total_fixed_files_existed = total_fixed_files_existed +1
                    total_processed_file_path = total_processed_file_path + processed_file_path
                    count = count +1
            #print(processed_file_path)
            #if(found==1):
                #content_to_write = content_to_write + processed_file_path
    file_read_write.writeFiles('E:\PhD\LSI\Repo\AspectJ\gitInfoAspectJSingleFile.txt', str(content_to_write))
    return str(content_to_write)

def process_file_path(file_path, ch):
    #import pdb
    #pdb.set_trace()
    file_path_without_java=file_path[:-6]
    #print (file_path_without_java)
    last_Index = file_path.rfind(ch)
    file_address = file_path[last_Index + 1 :]
    return file_address

def find(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i


def checkSourceExistance(content_to_write, list_of_source_files):
    print content_to_write
    print list_of_source_files



def readSourceCorpus(source_path_address):
    sourceFileRead=FileReadWrite(source_path_address)
    file_content_dict=sourceFileRead.readFilesWordByWordInDict(source_path_address, '.java')
    file_path_info=sourceFileRead.getFilePath()
    #print('---------------------------------------------------------------------------------------------------------------------------')
    #print (str(file_path_info))

    list_of_files=processSourceCorpusPaths(file_path_info)
    return list_of_files

def processSourceCorpusPaths(file_path_info):
    list_of_files=[]
    for i in range (0, len(file_path_info)):
        #print (file_path_info[i])
        processed_file_path = process_file_path(file_path_info[i], '\\')
        #print(processed_file_path)
        list_of_files.append(processed_file_path)
    return list_of_files


corpus='AspectJ'
file_read_write = FileReadWrite('E:\PhD\LSI\Repo\AspectJ\data\gitInfoAspectJ.txt')
git_content=[]
git_content=file_read_write.fileReadSingleReturnListByLine('E:\PhD\LSI\Repo\AspectJ\data\gitInfoAspectJ.txt')
list_of_source_files=readSourceCorpus('E:\PhD\LSI\Repo\\'+corpus+'\processedSourceCodes')
content_to_write = goldset_creator(git_content, list_of_source_files)


#checkSourceExistance(content_to_write, list_of_source_files)