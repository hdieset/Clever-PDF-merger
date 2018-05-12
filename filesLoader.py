from os import walk, getcwd, path
import numpy as np
from customTypes import *
from shutil import copy2

def loadConfig(fname = "config.txt"):
	if not path.exists(fname):
		f = open(fname,"w")
		initConfigFile(f)
		print "No config file detected. Created one. Please fill inn fields."
		return 0
	else:
		with open(fname,'r') as f:
			# Get path data from config file
			configs = CONFIG()
			for line in f:
				if line.startswith("Target folder  :"):
					configs.target = line[16:-1]
				elif line.startswith("LaTeX compiler :"):
					configs.compiler = line[16:-1]
				elif line.startswith("Frontpage path :"):
					configs.frontpage = line[16:-1]
				elif line.startswith("Field separator:"):
					configs.field_sep = line[16:-1]
				elif line.startswith("Comment between:"):
					configs.comment_sep = line[16:-1]
		return configs

def filesLoader(filepath = "/target", fieldSeparator = "_", commentSeparator = "'"):
	filepath = getcwd() + filepath
	rawFileList = []
	for (dirpath, dirnames, filenames) in walk(filepath):
		rawFileList.extend(filenames)
		break

	for files in range(len(rawFileList)):
		if not rawFileList[files-1].endswith(".pdf"):
			del rawFileList[files-1]

	formattedList = []
	noFiles = -1
	if len(rawFileList):
		for files in range(len(rawFileList)):
			noFiles = noFiles + 1
			newFile = filenameSplitter(rawFileList[files], noFiles, fieldSeparator, commentSeparator)
			if newFile != 0:
				formattedList.append(newFile)
		return formattedList
	else:
		print "No PDF files found."
		return 0


def filenameSplitter(fnString, fid, fieldSeparator = "_", commentSeparator = "'"):
	fnList = fnString.split(fieldSeparator)
	formatted = PDF()
	# Lecture case:
	if fnList[0] == "L":
		formatted.type    = fnString[0]
		formatted.num     = fnString[1]
		formatted.name    = fnString[2]
		formatted.date    = fnString[3]
		formatted.comment = fnString[4].split(commentSeparator)[1]
		formatted.fname   = fnString
		formatted.fid 	  = 'f' + str(fid)
	# Problem set case:
	elif fnList[0] == "PS":
		formatted.type    = fnString[0]
		formatted.num   = fnString[1]
		formatted.date  = fnString[2]
		formatted.fname = fnString
		formatted.fid   = 'f' + str(fid)
	elif fnList[0] == "ER":
		formatted.type    = fnString[0]
		formatted.date    = fnString[1]
		formatted.comment = fnString[2].split(commentSeparator)[1]
		formatted.fname   = fnString
		formatted.fid 	  = 'f' + str(fid)
#	if len(fnList) == 5:
#		formatted.fname   = fnString
#		formatted.fid 	  = 'f' + str(fid)
#		formatted.name 	  = fnList[0]
#		formatted.chapter = int(fnList[1])
#		formatted.date	  = fnList[2]
#		formatted.time 	  = fnList[3]
#		formatted.comment = fnList[4]
#		return formatted
	else:
		print "Filename:", fnString, "splitting failed."
		print "Naming convention described in config.txt not used."
		return 0




def initConfigFile(f):
	f.write("----------------Paths----------------\n")
	f.write("Target folder  :/target\n")
	f.write("LaTeX compiler :C:/program files/blabla\n")
	f.write("Frontpage path :/templates/frontpage.tex\n")
	f.write("Field separator:_\n")
	f.write("Comment between:'\n")
	f.close()

def copyPDFsToTemp(files, source = '/target/', dest = '/tex/'):
	for file in files:
		sourcePath = getcwd() + source + file.fname
		destPath = getcwd() + dest + file.fid + ".pdf"
		copy2(sourcePath,destPath)