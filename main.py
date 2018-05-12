from customTypes import PDF
from filesLoader import *
from texCreator import *

loadConfig()
fileList = filesLoader()
for files in fileList:
	PDFprint(files)



initTex()
copyPDFsToTemp(fileList)
#writeSampleFrontPage()
#writePreamble()
writeSampleFrontPage()
mainTexCreator(fileList)
tocWriter(fileList)