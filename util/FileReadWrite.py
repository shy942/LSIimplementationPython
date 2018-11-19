import os,sys
import math

import sys




class FileReadWrite:
    file_content=[]
    file_path_info=[]
    file_content_dict={}
    def __init__(self, folder_path):
        self.file_content=[]
        self.file_path_info=[]
        self.file_content_dict={}
    def readFilesWordByWord(self, fpath, file_extension):
        if(os.path.exists(fpath)):
            self.item = os.listdir(fpath)
            for i in range(0,len(self.item)):
                print(i)
                file_name=self.item.pop(0);
                full_file_path = os.path.join(fpath, file_name)
                #print (full_file_path)
                if(full_file_path.endswith('.java') or full_file_path.endswith('.txt')):
                    content=''
                    with open(full_file_path, 'r') as f:
                        for line in f:
                            for word in line.split():
                                content+=word+' '
                                #content.append(word)
                        f.close()
                    #print(content)
                    self.file_content.insert(i, content)
                    self.file_path_info.insert(i, full_file_path)
        return self.file_content

    def readFilesWordByWordInDict(self, fpath, file_extension):
        if(os.path.exists(fpath)):
            self.item = os.listdir(fpath)
            for i in range(0,len(self.item)):
                print(i)
                file_name=self.item.pop(0);
                full_file_path = os.path.join(fpath, file_name)
                #print (full_file_path)
                if(full_file_path.endswith('.java') or full_file_path.endswith('.txt')):
                    content=''
                    with open(full_file_path, 'r') as f:
                        for line in f:
                            for word in line.split():
                                content+=word+' '
                                #content.append(word)
                        f.close()
                    print(content)
                    self.file_content_dict[file_name]= content
                    self.file_path_info.insert(i, full_file_path)

        return self.file_content_dict

    def getFilePath(self):
        return self.file_path_info

    def writeFiles(self, fpath, contentToWrite):
        try:
            my_file_handle = open(fpath, 'w')
            my_file_handle.write(contentToWrite)
            my_file_handle.close()
        except:
            print ("problem with file writing")

    def fileReadSingle(self, fpath):
        content = ''
        with open(fpath, 'r') as f:
            for line in f:
                for word in line.split():
                    content += word + ' '
                    # content.append(word)
            f.close()
        return content

    def fileReadSingleReturnListByLine(self, fpath):
        content = []
        with open(fpath, 'r') as f:
            for line in f:
               content.append(line)
            f.close()
        return content