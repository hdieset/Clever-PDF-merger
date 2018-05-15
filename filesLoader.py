from os import walk, getcwd, path
import numpy as np
from customTypes import *
from shutil import copy2


def loadConfig(fname = "config.txt"):
	if not path.exists(fname):
		f = open(fname,"w")
		initConfigFile(f)
		print("No config file detected. Created one. Please fill inn fields.")
		exit()
		return 0

	with open(fname,'r') as f:
		# Get path data from config file
		configs = CONFIG()
		for line in f:
			if line.startswith("Target folder  :"):
				configs.pdfFolder = line[16:-1]
			elif line.startswith("Temp folder    :"):
				configs.temp_folder = line[16:-1]
			elif line.startswith("Frontpage path :"):
				configs.frontpage = line[16:-1]
			elif line.startswith("Field separator:"):
				configs.field_sep = line[16:-1]
			elif line.startswith("Comment between:"):
				configs.comment_sep = line[16:-1]
			elif line.startswith("Delete temp after completion (y/n):"):
				configs.delTemp = line[35:36]
	return configs


def initConfigFile(f):
	f.write("----------------Paths----------------\n")
	f.write("Target folder  :/target/\n")
	f.write("Temp folder    :/tex/\n")
	f.write("Frontpage path :/frontpage.tex\n")
	f.write("Field separator:_\n")
	f.write("Comment between:'\n")
	f.write("Delete temp after completion (y/n):n\n\n")
	f.write("File scraping profiles\n")
	f.write("Lectures     :L_date_number_name_'comment'\n")
	f.write("Problem set  :PS_date_number\n")
	f.write("Exam relevant:ER_date_comment\n")
	f.close()


def filesLoader(filepath = "/target", fieldSeparator = "_", commentSeparator = "'"):
	filepath = getcwd() + filepath
	rawFileList = []
	for (dirpath, dirnames, filenames) in walk(filepath):
		rawFileList.extend(filenames)
		break

	for files in range(len(rawFileList)):
		if not rawFileList[files].endswith(".pdf"):
			del rawFileList[files]

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
		print("No PDF files found in folder " + filepath)
		exit()
		return 0


def filenameSplitter(fnString, fid, fieldSeparator = "_", commentSeparator = "'"):
	fnList = fnString.split(fieldSeparator)
	formatted = PDF()

	# Lecture case:
	if fnList[0] == "L":
		formatted.fname   = fnString
		formatted.fid 	  = 'f' + str(fid)
		formatted.type    = fnList[0]
		formatted.date    = fnList[1]
		formatted.time	  = fnList[2]
		formatted.num     = fnList[3]
		formatted.name    = fnList[4]
		formatted.comment = fnList[5].split(commentSeparator)[1]

	# Problem set case:
	elif fnList[0] == "PS":
		formatted.fname = fnString
		formatted.fid   = 'f' + str(fid)
		formatted.type  = fnList[0]
		formatted.date  = fnList[1]
		formatted.time  = fnList[2]
		formatted.num   = fnList[3]
	
	# Exam relevant case:
	elif fnList[0] == "ER":
		formatted.fname   = fnString
		formatted.fid 	  = 'f' + str(fid)
		formatted.type    = fnList[0]
		formatted.date    = fnList[1]
		formatted.time	  = fnList[2]
		formatted.comment = fnList[3].split(commentSeparator)[1]

	# If not implemented file syntax:
	else:
		print("Filename:", fnString, "splitting failed.")
		print("Naming convention described in config.txt not used.")
		formatted = 0

	return formatted


def copyPDFsToTemp(files, source = '/target/', dest = '/tex/'):
	for file in files:
		sourcePath = getcwd() + source + file.fname
		destPath = getcwd() + dest + file.fid + ".pdf"
		copy2(sourcePath,destPath)