# Clever PDF merger
A python script that scrapes a target folder for `.pdf` files and combines them into a single `.pdf` document, with the following made automatically:
- Frontpage (template generated automatically, ordinary LaTeX syntax applies).
- Table of contents.
- Chapter markers (visible in Adobe Reader etc.).

based on the file names of the input files.

Three file conventions are implemented, based on the authors usecases, and are named as follows: *Lectures*, *Problem Sets*, and *Exam Relevant*. This script in combination with electronic note taking systems, eg. the [Rocketbook](https://getrocketbook.co.uk), will produce a single document containing all notes organized systematically and with great accessibility.

The `.pdf`s are merged as-is, without any alternations or compressions or any of the sorts. The only two exceptions are that they are adjusted to fit into an A4 page, and hyperlinks are assumed not to be present. If the latter is a problem, the [pdfpages documentation](http://ctan.uib.no/macros/latex/contrib/pdfpages/pdfpages.pdf) can be read to enable this functionality in the `texAgent.py` file, more specifically, the `writePDFimports2mainTex(...)` method.

## File naming
In order to use the three build-in presets, the user should use the following file naming conventions:
- Lectures     : `L_date_time_{lecture number}_^lecture name^_^comment^.pdf`.
- Problem sets : `PS_date_time_{problem set number}_^comment^.pdf`.
- Exam relevant: `ER_date_time_^comment^.pdf`.

At the first run of the program, a `config.txt` file is written, containing paths needed for the program to work. The different symbols used for filename scraping can be changed there. The field separator is by default set to `_` and the comment start and end symbol is set to `^`.
New file scraping profiles can be added to `filesLoader.py`.

Comments are optional. Naming for lectures and exam relevant documents are recommended, but if not present, the program will alert the user. 

## Table of contents
As mentioned, the table of contents is generated automatically based on the files in the target folder. Each of the three types will start with a boldface headline, followed by a LaTeX enumeration environment with pagenumber and other relevant information the author seemed relevant to present at this point in the document. These defaults can be changed by modifying the `texAgent.py` file, if the string operations there aren't too confusing :pensive:.

## How to run
This software was developed using Windows 10, but should work just fine with Linux distros (although not testet).

Note: **Python 3 is required to even run on Windows 10**. Reason: authentication issues with `shutil`s `copy2` method (and other copying methods as well). If errors occur, update.

Simply run `cleverPDFmerger.py` or `main.py`. The first can be run standalone from the other python files, the other is used for debugging purposes, or if you, the reader, wants to make alterations. If the `config.txt` file is not found, the program will create it based on a template, and the exit. Else, it will copy the `.pdf`s into a temp. folder, create the necessary `.tex` files, compile, and finally move the output document out of the temp. folder into the working folder. ~~If set in the `config` file, the temp. folder will be erased.~~ Edit: currently not working in Windows.

[MiKTEX](https://miktex.org/) is assumed to be installed, as the default compiler is set to `pdflatex`. This can be changed in the `texAgent.py` file, in function `runLaTeXcompiler(...)`.

## Python packages
The following packages are required to run the program:
- `os`
- `numpy`
- `shutil`
- `subprocess`
- `PyPDF2`

## LaTeX packages
The following LaTeX packages are used when creating the document:
- `etoolbox`
- `pdfpages`
- `hyperref`
- `enumitem`
- `geometry`
- `inputenc`
- `fontenc`

## Example file names
The following three examples are based on the build in profiles;

Notes taken from a lecture can be named `L_2018.05.12_21.26.38_8_^Code quality, fault tolerance, redundancy^_^Introduction.^.pdf`. A Problem Set can be named `PS_2018.05.12_21.22.54_09_.pdf`. An Exam Relevant document could be named `ER_2018.05.09_18.13.45_^Notes^.pdf`.

Some example documents are provided, some scribbles I made for some of my courses. Despite my ugly handwriting, they show the capabilities for the program.
