# Classses and helping functions for these, eg. prints.

class PDF:
	fname = ''
	name = ''
	chapter = 0
	date = ''
	time = ''
	comment  = ''

def PDFprint(pdf):
	print 'File name:', pdf.fname 
	print 'name     :', pdf.name 
	print "chapter  :", pdf.chapter
	print "date     :", pdf.date
	print "time     :", pdf.time
	print "comment  :", pdf.comment

class PATHS:
	pdfFolder = '/target'
	compiler  = ''
	frontpage = ''

class bookStructure:
	chapters = []