from customTypes import PDF
from filesLoader import *
from texAgent import *

config = loadConfig("config.txt")
fileList = filesLoader(config.pdfFolder, config.field_sep, config.comment_sep)
initTex()
copyPDFsToTemp(fileList,config.pdfFolder,config.temp_folder)
writeFrontPage(config.frontpage)
mainTexCreator(fileList,config.temp_folder)
tocWriter(fileList,config.temp_folder)
runLaTeXcompiler(config.temp_folder,config.frontpage,"document.tex")
moveFinalPDF(config.temp_folder,"document.pdf","/","Notes.pdf")
clearTempFolder(config.delTemp,config.temp_folder)