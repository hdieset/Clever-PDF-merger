# Creates LaTeX project that creates the final output PDF.
from os import getcwd, makedirs
from os import path as p

def initTex(path = '/tex'):
	path = getcwd() + path
	if not p.exists(path):
		makedirs(path)

def mainTexCreator(files, path = '/tex/', fname = 'document.tex'):
	fname = getcwd() + path + fname
	f = open(fname,'w')
	preambleWriter(f)
	documentWriter(files,f)
	f.close()
	print fname

def preambleWriter(f):
	f.write("\\documentclass{article}\n")
	f.write("\\usepackage{etoolbox}\n")
	f.write("\\patchcmd{\\chapter}{plain}{empty}{}{}\n")
	f.write("\\usepackage[final]{pdfpages}\n")
	f.write("\\usepackage{hyperref}\n")
	f.write("\\usepackage{enumitem}\n")
	f.write("\\usepackage{geometry}\n")
	f.write("\\geometry{\n")
	f.write("\ta4paper,\n")
	f.write("\ttop=1in,\n")
	f.write("\tleft=1in,\n")
	f.write("\ttop=1in,\n")
	f.write("\tbottom=0.8in\n")
	f.write("}\n")
	f.write("\\newcounter{includepdfpage}\n")
	f.write("\\newcounter{currentpagecounter}\n")
	f.write("\\newcommand{\\addlabelstoallincludedpages}[1]{\n")
	f.write("\t\\refstepcounter{includepdfpage}\n")
	f.write("\t\\stepcounter{currentpagecounter}\n")
	f.write("\t\\label{#1.\\thecurrentpagecounter}}\n")
	f.write("\\newcommand{\\modifiedincludepdf}[3]{\n")
	f.write("\t\\setcounter{currentpagecounter}{0}\n")
	f.write("\t\\includepdf[pages=#1,pagecommand=\\addlabelstoallincludedpages{#2}]{#3}}\n")
	f.write("\n")

def documentWriter(files,f):
	f.write("\n")
	f.write("\\begin{document}\n\n")
	f.write("\\input{frontpage.tex}\n")
	f.write("\\newpage\n")
	f.write("\\input{toc.tex}\n")
	f.write("\\newpage\n")
	f.write("\\setcounter{page}{1}\n")
	f.write("\\pagestyle{plain}\n\n")
	for i in range(len(files)):
		f.write("\\clearpage\n")
		f.write("\\modifiedincludepdf{-}{")
		f.write(files[i].fid)
		f.write("}{")
		f.write(files[i].fid)
		f.write("}\n")
	f.write("\\clearpage\n\n")
	f.write("\\end{document}")

def tocWriter(files, path = '/tex/', fname = 'toc.tex'):
	fname = getcwd() + path + fname
	f = open(fname,'w')
#	chapters = []
#	for i in range(len(files)): 
#		chapters.append(files[i].chapter)
	f.write("%Table of contents\n")
	f.write("\\Huge{\\bfseries Contents }\n")
	f.write("\\vspace{10mm}\n\n")

	prevChapter = -1
	for file in files:
		if not prevChapter == file.chapter:
			if prevChapter != -1 :
				f.write("\\end{enumerate}\n")
			f.write("\\vspace{0.5mm}\n")
			f.write("\\noindent\n")
			f.write("\\Large{\\textbf{Chapter ")
			f.write(str(file.chapter))
			f.write("}}\n")
			f.write("\\normalsize\n")
			f.write("\\begin{enumerate}[leftmargin=4em]\n")
			prevChapter = file.chapter

		f.write("\t\\item[\\pageref{")
		f.write(file.fid)
		f.write(".1}.] \\textbf{\\hyperref[")
		f.write(file.fid)
		f.write(".1]{")
		f.write(file.name)
		f.write("}}. \\textit{")
		f.write(file.date)
		f.write(".} ")
		f.write(file.comment)
		f.write(".\n")
		#\\textbf{\\hyperref[fil.1]{Headline}.}\n")
		#	"filHere, the comment will appear.\n")
		# f.write("\n")
		# f.write("\n")
		# f.write("\n")
		# f.write("\n")
	f.write("\\begin{enumerate}[leftmargin=4em]\n")


def writeSampleFrontPage(path = '/tex/'):
	frontpagename = getcwd() + path + "frontpage.tex"
	if not p.exists(frontpagename):
		f = open(frontpagename,'w')
		f.write("% Just some frontpage. An example:\n")
		f.write("\\pagestyle{empty}\n")
		f.write("\\clearpage")
		f.write("\\begin{center}\n\n")
		f.write("\\vfill\n")
		f.write("\\vspace*{4cm}\n")
		f.write("\\Huge{\\bfseries Cource code}\n\n")
		f.write("\\vspace{8mm}\n")
		f.write("\\Huge{\\bfseries Cource name}\n\n")
		f.write("\\vspace{8mm}\n")
		f.write("\\Huge{\\bfseries Notes}\n\n")
		f.write("\\vspace{8mm}\n")
		f.write("\\Huge{\\bfseries year}\n\n")
		f.write("\\vfill\n")
		f.write("\\end{center}\n")
		f.close()