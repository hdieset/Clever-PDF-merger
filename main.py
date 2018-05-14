from customTypes import PDF
from filesLoader import *
from texCreator import *


config = loadConfig()
fileList = filesLoader(config.pdfFolder, config.field_sep, config.comment_sep)
for file in fileList:
	print(file.num)
if fileList != 0 :
	initTex()
	copyPDFsToTemp(fileList)
	writeFrontPage(config.temp_folder)
	mainTexCreator(fileList,config.temp_folder)
	tocWriter(fileList,config.temp_folder)

# To be implemented:
#---- Scraping profiles
#1 Lecture      _L_date_num_name_comment
#2 Problem Set  _PS_date_num
#3 Exam Relevant_ER_date_comment
#---- TOC profiles
#1 Lectures
#-num_NAME_/date/_comment
#2 Problem Set
#-num_date
#3 Exam Relevant
#-date_comment