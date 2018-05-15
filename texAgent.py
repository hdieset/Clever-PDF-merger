# Creates LaTeX project that creates the final output PDF.
from os import getcwd, makedirs
from os import path as p
from subprocess import Popen, DEVNULL
from shutil import copy2, rmtree

def initTex(path = '/tex'):
	path = getcwd() + path
	if not p.exists(path):
		makedirs(path)


def writeFrontPage(pathToFrontpage = '/tex/'):
	frontpagename = getcwd() + pathToFrontpage 
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


def mainTexCreator(files, path = '/tex/', fname = '/document.tex'):
	fname = getcwd() + path + fname
	f = open(fname,'w')
	preambleWriter(f)
	documentWriter(files,f)
	f.close()

def preambleWriter(f):
	f.write("\\documentclass{article}\n")
	f.write("\\usepackage{etoolbox}\n")
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

def documentWriter(files,f):
	f.write("\n")
	f.write("\\begin{document}\n\n")
	f.write("\\input{frontpage.tex}\n")
	f.write("\\newpage\n")
	f.write("\\input{toc.tex}\n")
	f.write("\\phantomsection\\addcontentsline{toc}{section}{Contents}\n")
	f.write("\\newpage\n")
	f.write("\\setcounter{page}{1}\n\n")

	lectureFiles      = []
	problemSetfiles   = []
	examRelevantFiles = []
	for file in files:
		if file.type == "L":
			lectureFiles.append(file)
		elif file.type == "PS":
			problemSetfiles.append(file)
		elif file.type == "ER":
			examRelevantFiles.append(file)

	writePDFimports2mainTex(f,lectureFiles,"Lectures","name")
	writePDFimports2mainTex(f,problemSetfiles,"Problem Sets","num")
	writePDFimports2mainTex(f,examRelevantFiles,"Exam Relevant","date")

	f.write("\\clearpage\n\n")
	f.write("\\end{document}")

def writePDFimports2mainTex(out, files, chapTitle, subChapElem):
	if len(files) > 0:
		out.write("\\includepdf[pages=1,pagecommand={")
		out.write("\\thispagestyle{plain},")
		out.write("\\phantomsection\\addcontentsline{toc}{section}{")
		out.write(chapTitle)
		out.write("},\\phantomsection\\addcontentsline{toc}{subsection}{")
		out.write(getattr(files[0], subChapElem))
		out.write("},\\label{")
		out.write(files[0].fid)
		out.write("}}]{")
		out.write(files[0].fid)
		out.write(".pdf}\n")
		out.write("\\includepdf[pages=2-,pagecommand={")
		out.write("\\thispagestyle{plain}")
		out.write("}]{")
		out.write(files[0].fid)
		out.write(".pdf}\n\n")
		
		if len(files) > 1:
			for file in files[1:]:
				out.write("\\includepdf[pages=1,pagecommand={")
				out.write("\\thispagestyle{plain},")
				out.write("\\phantomsection\\addcontentsline{toc}{subsection}{")
				out.write(getattr(file, subChapElem))
				out.write("},\\label{")
				out.write(file.fid)
				out.write("}}]{")
				out.write(file.fid)
				out.write(".pdf}\n")
				out.write("\\includepdf[pages=2-,pagecommand={")
				out.write("\\thispagestyle{plain}")
				out.write("}]{")
				out.write(file.fid)
				out.write(".pdf}\n\n")


def tocWriter(files, path = '/tex/', fname = '/toc.tex'):
	fname = getcwd() + path + fname
	f = open(fname,'w')
	f.write("%Table of contents\n")
	f.write("\\noindent\n")
	f.write("\\Huge{\\textbf{Contents}}\n")
	f.write("\\vspace{10mm}\n\n")

	lectureFiles      = []
	problemSetfiles   = []
	examRelevantFiles = []
	for file in files:
		if file.type == "L":
			lectureFiles.append(file)
		elif file.type == "PS":
			problemSetfiles.append(file)
		elif file.type == "ER":
			examRelevantFiles.append(file)

	lecture2TOCwriter(lectureFiles,f,"Lectures")
	problemSet2TOCwriter(problemSetfiles,f,"Problem Sets")
	examRelecant2TOCwriter(examRelevantFiles,f,"Exam relevant")

	f.close()

def lecture2TOCwriter(files,out,chapTitle):
	if len(files) > 0:
		out.write("\\vspace{0.5mm}")
		out.write("\\noindent")
		out.write("\\Large{\\textbf{")
		out.write(chapTitle)
		out.write("}}\n")
		out.write("\\normalsize\n")
		out.write("\\begin{enumerate}[leftmargin=4em]\n")
		for file in files:
			out.write("\\item[\\pageref{")
			out.write(file.fid)
			out.write("}.] ")
			out.write(" \\hyperref[")
			out.write(file.fid)
			out.write("]{\\textbf{")
			out.write(file.num)
			out.write(" ")
			out.write(file.name)
			out.write("}}. \\textit{")
			out.write(file.date)
			out.write(".} ")
			out.write(file.comment)
			out.write("\n")
		out.write("\\end{enumerate}\n\n")

def problemSet2TOCwriter(files,out,chapTitle):
	if len(files) > 0:
		out.write("\\vspace{0.5mm}")
		out.write("\\noindent")
		out.write("\\Large{\\textbf{")
		out.write(chapTitle)
		out.write("}}\n")
		out.write("\\normalsize\n")
		out.write("\\begin{enumerate}[leftmargin=4em]\n")
		for file in files:
			out.write("\\item[\\pageref{")
			out.write(file.fid)
			out.write("}.] ")
			out.write("\\hyperref[")
			out.write(file.fid)
			out.write("]{\\textbf{")
			out.write(file.num)
			out.write("}. \\textit{")
			out.write(file.date)
			out.write(".}} \n")
		out.write("\\end{enumerate}\n\n")

def examRelecant2TOCwriter(files,out,chapTitle):
	if len(files) > 0:
		out.write("\\vspace{0.5mm}")
		out.write("\\noindent")
		out.write("\\Large{\\textbf{")
		out.write(chapTitle)
		out.write("}}\n")
		out.write("\\normalsize\n")
		out.write("\\begin{enumerate}[leftmargin=4em]\n")
		for file in files:
			out.write("\\item[\\pageref{")
			out.write(file.fid)
			out.write("}.] ")
			out.write("\\hyperref[")
			out.write(file.fid)
			out.write("]{")
			out.write("\\textit{")
			out.write(file.date)
			out.write(".}} \n")
		out.write("\\end{enumerate}\n\n")


def runLaTeXcompiler(projFolder = "/tex/", frontPagePath = "/frontpage.tex", mainDoc = "document.tex"):
	projPath = getcwd() + projFolder
	copy2(getcwd()+frontPagePath,projPath+frontPagePath)
	# Compile twice to ensure hyperlinks is rendered correctly
	p = Popen(["pdflatex", "-synctex=1", "-interaction=nonstopmode", mainDoc], cwd = projPath, stdout=DEVNULL)
	p.wait()
	p = Popen(["pdflatex", "-synctex=1", "-interaction=nonstopmode", mainDoc], cwd = projPath, stdout=DEVNULL)
	p.wait()


def moveFinalPDF(srcFldr = "/tex/", srcName = "document.pdf", dest = "/Notes.pdf"):
	sourcePath = getcwd() + srcFldr + srcName
	destPath = getcwd() + dest
	copy2(sourcePath,destPath)


def clearTempFolder(cmd = "n",delFldr = "/tex/"):
	if cmd == "y":
		rmtree(getcwd()+delFldr, ignore_errors=True)