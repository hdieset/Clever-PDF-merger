from os import walk, getcwd, path
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
		formatted.fname = fnString
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

def filesLoader(filepath = "/target" ):
	filepath = getcwd() + filepath
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

def loadConfig(fname = "config.txt"):
	if not path.exists(fname):
		f = open(fname,"w")
		initConfigFile(f)
		print "No config file detected. Created one. Please fill inn paths."
		return 0
	else:
		with open(fname,'r') as f:
			# Get path data from config file
			paths = PATHS()
			for line in f:
				if line.startswith("Target folder :"):
					paths.target = line[15:]
				elif line.startswith("LaTeX compiler:"):
					paths.compiler = line[15:]
				elif line.startswith("Frontpage path:"):
					paths.frontpage = line[15:]
		return paths

def initConfigFile(f):
	f.write("----------------Paths----------------\n")
	f.write("Target folder :/target\n")
	f.write("LaTeX compiler:C:/program files/blabla\n")
	f.write("Frontpage path:/templates/frontpage.tex\n")
	f.close()