from util.FileReadWrite import FileReadWrite


class sourceCorpusCreator:
    file_content_all=[]
    file_path_info=[]
    file_content_dict = {}
    def __abs__(self):
        self.file_content_all=[]
        self.file_path_info=[]
        self.file_content_dict={}
    def CorpusCreator(self, folderPath, file_extension):
        # Read each file
        file_read_Write = FileReadWrite(folderPath)
        file_content_all = file_read_Write.readFilesWordByWord(folderPath, file_extension)
        self.file_path_info=file_read_Write.getFilePath()
        return file_content_all
    def getFileP(self):
        return self.file_path_info
    def CorpusCreatorDict(self, folderPath, file_extension):
        file_read_Write = FileReadWrite(folderPath)
        self.file_content_dict = file_read_Write.readFilesWordByWordInDict(folderPath, file_extension)
        #self.file_path_info = file_read_Write.getFilePath()
        #import pdb
        #pdb.set_trace()
        return self.file_content_dict