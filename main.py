from customTypes import PDF
from filesLoader import *

fileList = filesLoader()
for files in fileList:
	PDFprint(files)

