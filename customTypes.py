# Classses and helping functions for these, eg. prints.

class PDF:
	name = ''
	chapter = 0
	date = ''
	time = ''
	comment  = ''

def PDFprint(pdf):
	print 'name   :', pdf.name 
	print "chapter:", pdf.chapter
	print "date   :", pdf.date
	print "time   :", pdf.time
	print "comment:", pdf.comment
