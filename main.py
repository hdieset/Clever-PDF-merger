from customTypes import PDF
from filesLoader import *
from texAgent import *

config = loadConfig("config.txt")
fileList = filesLoader(config.pdfFolder, config.field_sep, config.comment_sep)
initTex(config.temp_folder)
copyPDFsToTemp(fileList,config.pdfFolder,config.temp_folder)
writeFrontPage(config.frontpage,config.temp_folder)
tocWriter(fileList,config.temp_folder)
mainTexCreator(fileList,config.temp_folder)
runLaTeXcompiler(config.temp_folder,config.frontpage,"document.tex")
moveFinalPDF(config.temp_folder,"document.pdf",config.outfile)
clearTempFolder(config.delTemp,config.temp_folder)