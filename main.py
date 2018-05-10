from customTypes import PDF
from filesLoader import *
from texCreator import *

fileList = filesLoader()
for files in fileList:
	PDFprint(files)

loadConfig()

#initTex()
#writeSampleFrontPage()
#writePreamble()
mainTexCreator(fileList)
tocWriter(fileList)