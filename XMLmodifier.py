from xml.etree import ElementTree

from numpy.distutils.system_info import f2py_info

from util.FileReadWrite import FileReadWrite
corpus='AspectJ'
tree = ElementTree.parse("E:\\BugLocator\\data\\"+corpus+"BugRepository.xml")
root = tree.getroot()
# find the first 'item' object
children = root.getchildren()
for child in children:
    print(child.tag, child.attrib)

file_read_write=FileReadWrite("E:\\PhD\\Repo\\"+corpus+"\\data\\bugIdsNotCluded.txt")

bugIDs=file_read_write.fileReadSingleReturnListByLine("E:\\PhD\\Repo\\"+corpus+"\\data\\bugIdsNotCluded.txt")
print(bugIDs)
for b in bugIDs:
    BugID=b[:-1]
    print (BugID)
    for bid in root.findall("./bug/[@id='"+BugID+"']"):
        print(bid.attrib)
        root.remove(bid)


tree.write("E:\\BugLocator\\data\\"+corpus+"BugRepositoryPy.xml")


