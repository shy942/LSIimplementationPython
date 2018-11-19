from util.FileReadWrite import FileReadWrite
def goldset_creator(git_content_list):
    content_to_write=''
    for line in git_content_list:
        print (line)
        line_content=line.split()
        line_length=len(line_content)
        if(line_length==2):
            content_to_write = content_to_write + line
        if(line_length==1):
            file_path=line
            processed_file_path=process_file_path(file_path)
            print(processed_file_path)
            content_to_write = content_to_write + processed_file_path
    file_read_write.writeFiles('E:\PhD\LSI\Repo\AspectJ\gitInfoAspectJSingleFile.txt', str(content_to_write))

def process_file_path(file_path):
    file_path_without_java=file_path[:-6]
    print (file_path_without_java)
    last_Index = file_path_without_java.rfind('/')
    file_address = file_path[last_Index + 1 :]
    return file_address

def find(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i






file_read_write = FileReadWrite('E:\PhD\LSI\Repo\AspectJ\data\gitInfoAspectJ.txt')
git_content=[]
git_content=file_read_write.fileReadSingleReturnListByLine('E:\PhD\LSI\Repo\AspectJ\data\gitInfoAspectJ.txt')
goldset_creator(git_content)