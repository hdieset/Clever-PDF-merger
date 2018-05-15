# Classses and helping functions for these, eg. prints.

class PDF:
	fname = ''
	fid = ''
	type = ''
	name = ''
	num = 0
	date = ''
	time = ''
	comment  = ''

def PDFprint(pdf):
	print('File name:', pdf.fname) 
	print('File id  :', pdf.fid)
	print('type     :', pdf.type)
	print('name     :', pdf.name)
	print("number   :", pdf.num)
	print("date     :", pdf.date)
	print("time     :", pdf.time)
	print("comment  :", pdf.comment)

class CONFIG:
	pdfFolder   = "/target/"
	temp_folder = "/tex/"
	frontpage   = "/frontpage.tex"
	field_sep   = "_"
	comment_sep = "'"
	delTemp     = 'n' # y/n