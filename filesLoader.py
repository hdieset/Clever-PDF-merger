from os import walk, getcwd
import numpy as np
from customTypes import *

# Create list of pdf files in target folder
def pdfFilesScraper(filepath):
	f = []
	for (dirpath, dirnames, filenames) in walk(filepath):
		f.extend(filenames)
		break

	for files in range(len(f)):
		if not f[files-1].endswith(".pdf"):
			del f[files-1]

	return f


def filenameSplitter(fnString, splitter = "_"):
	fnList = fnString.split(splitter)
	formatted = PDF()
	if len(fnList) == 5:
		formatted.name 	  = fnList[0]
		formatted.chapter = int(fnList[1])
		formatted.date	  = fnList[2]
		formatted.time 	  = fnList[3]
		formatted.comment = fnList[4]
		return formatted
	else:
		print "Filename:", fnString, "splitting failed."
		print "Naming convention name_chapter_date_time_comment not used."
		return 0

def filesLoader(filepath = getcwd() + "/target" ):
	rawFileList = pdfFilesScraper(filepath)
	formattedList = []
	if len(rawFileList):
		for files in range(len(rawFileList)):
			newFile = filenameSplitter(rawFileList[files])
			if newFile != 0:
				formattedList.append(newFile)
		return formattedList
	else:
		print "No PDF files found."
		return 0
