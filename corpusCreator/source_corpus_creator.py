from util.FileReadWrite import FileReadWrite


class sourceCorpusCreator:
    file_content_all=[]
    file_path_info=[]
    def __abs__(self):
        self.file_content_all=[]
        self.file_path_info=[]
    def CorpusCreator(self, folderPath, file_extension):
        # Read each file
        file_read_Write = FileReadWrite(folderPath)
        file_content_all = file_read_Write.readFilesWordByWord(folderPath, file_extension)
        self.file_path_info=file_read_Write.getFilePath()
        return file_content_all
    def getFileP(self):
        return self.file_path_info
