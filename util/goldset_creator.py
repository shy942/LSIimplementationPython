from util.FileReadWrite import FileReadWrite
def goldset_creator(git_content_list, list_of_source_files, list_no_of_method_dict):
    i=0
    all_bug_ids=''
    content_to_write=''
    content_to_write_all=''
    total_fixed_files_existed = 0
    count=0
    bugID=''
    no_of_files=0
    total_processed_file_path=''
    total_file_path=''
    total_file=0
    for line in git_content_list:
        #print (line)
        line_content=line.split()
        line_length=len(line_content)
        #print (line_length)
        if(line_length==2):
            if (count > 0):
                #print (no_of_files)
                #print (total_fixed_files_existed)
                if(str(no_of_files) ==  str(total_fixed_files_existed)):
                    i = i+1
                    #print (i)
                    #import pdb
                    #pdb.set_trace()
                    content_to_write = content_to_write + bugID +' '+ str(no_of_files) + '\n' +total_processed_file_path
                    content_to_write_all = content_to_write_all + bugID + ' ' + str(total_file) + '\n' + total_file_path
                    all_bug_ids = all_bug_ids + '\n' +bugID
                    print bugID
            bugID=line_content[0]
            no_of_files=line_content[1]
            total_fixed_files_existed = 0
            total_processed_file_path = ''
            total_file_path = ''
            total_file=0
        if(line_length==1):
            #import pdb
            #pdb.set_trace()
            file_path=line
            processed_file_path=process_file_path(file_path,'.')

            for i in range(0, len(list_of_source_files)):
                source_path=list_of_source_files[i]+'\n'
                if(processed_file_path == source_path):

                    total_fixed_files_existed = total_fixed_files_existed +1
                    total_processed_file_path = total_processed_file_path + processed_file_path
                    file_address=process_file_path_without_last_part(file_path,'.')
                    No_of_method=''
                    No_of_method=(list_no_of_method_dict.get(file_address+'.'+processed_file_path.split('\n')[0]))

                    if No_of_method is not None:
                        No_of_method=No_of_method.split('\n')[0]
                        #print('-----------------------------------'+No_of_method)
                        #filePathWithMethodInfo=file_address+'.'+No_of_method+'.'+processed_file_path

                        for j in range(1, int(No_of_method)+1):
                            filePathWithMethodInfo = file_address + '.' + str(j) + '.' + processed_file_path
                            total_file=total_file+1
                            total_file_path = total_file_path + filePathWithMethodInfo
                count = count +1
            #print (total_file_path)
            #print(processed_file_path)
            #if(found==1):
                #content_to_write = content_to_write + processed_file_path
    #import pdb
    #pdb.set_trace()
    print(str(content_to_write_all))
    file_read_write.writeFiles('E:\PhD\LSI\Repo\\'+corpus+'\\gitInfo'+corpus+'SingleFile.txt', str(content_to_write))
    file_read_write.writeFiles('E:\PhD\LSI\Repo\\' + corpus + '\\gitInfo' + corpus + 'All.txt', str(content_to_write_all))
    file_read_write.writeFiles('E:\PhD\LSI\Repo\\'+corpus+'\\data/bugID.txt', str(all_bug_ids))
    return str(content_to_write)

def process_file_path(file_path, ch):
    #print file_path
    file_path_without_java=file_path[:-6]
    #print (file_path_without_java)
    last_Index = file_path_without_java.rfind(ch)
    file_address = file_path[last_Index+1:]
    return file_address




def process_file_path_without_last_part(file_path, ch):
    #import pdb
    #pdb.set_trace()
    file_path_without_java = file_path[:-6]
    #print (file_path_without_java)
    last_Index = file_path_without_java.rfind(ch)
    file_address = file_path[:last_Index]
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

def readNoMethodInfo(path_address):
    sourceFileRead=FileReadWrite(path_address)
    file_content=sourceFileRead.fileReadSingleReturnListByLine(path_address)

    #print('---------------------------------------------------------------------------------------------------------------------------')
    #print (str(file_content))
    list_no_of_method_dict = {}
    for line in file_content:
        #print (line)
        line_content=line.split(',')
        line_length=len(line_content)
        bsourceID = line_content[0]
        no_of_method = line_content[1]
        list_no_of_method_dict[bsourceID]=no_of_method
    return list_no_of_method_dict

def processSourceCorpusPaths(file_path_info):
    list_of_files=[]
    for i in range (0, len(file_path_info)):
        #print (file_path_info[i])
        processed_file_path = process_file_path(file_path_info[i], '\\')
        #print(processed_file_path)
        list_of_files.append(processed_file_path)
    return list_of_files


corpus='SWT'
file_read_write = FileReadWrite('E:\PhD\LSI\Repo\\'+corpus+'\\data\gitInfo'+corpus+'.txt')
git_content=[]
git_content=file_read_write.fileReadSingleReturnListByLine('E:\PhD\LSI\Repo\\'+corpus+'\\data\gitInfo'+corpus+'.txt')
list_of_source_files=readSourceCorpus('E:\PhD\LSI\Repo\\'+corpus+'\processedSourceCodes3')
list_no_of_method_dict=readNoMethodInfo("E:\PhD\LSI\Repo\\"+corpus+"\data\\listNoOfMethod.txt")
#print (str(git_content))
content_to_write = goldset_creator(git_content, list_of_source_files, list_no_of_method_dict)


#checkSourceExistance(content_to_write, list_of_source_files)