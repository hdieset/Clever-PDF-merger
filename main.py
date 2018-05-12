from customTypes import PDF
from filesLoader import *
from texCreator import *

config = loadConfig()
print config.pdfFolder
print config.compiler
print config.frontpage
print config.field_sep
print config.comment_sep

fileList = filesLoader(config.pdfFolder, config.field_sep, config.comment_sep)

#for files in fileList:
#	PDFprint(files)



#initTex()
#copyPDFsToTemp(fileList)
#writeSampleFrontPage()
#writePreamble()
#writeSampleFrontPage()
#mainTexCreator(fileList)
#tocWriter(fileList)

# To be implemented:
#---- Scraping profiles
#1 Lecture      _L_num_name_date_comment
#2 Problem Set  _PS_num_date
#3 Exam Relevant_ER_date_comment
#---- TOC profiles
#1 Lectures
#-NAME_num_/date/_comment
#2 Problem Set
#-num_date
#3 Exam Relevant
#-date_comment