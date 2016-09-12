import os

from pdfrw import PdfReader, PdfWriter, IndirectPdfDict

resume_directory_path = os.getcwd() + "/resumes"
resumes = os.listdir(resume_directory_path)
resumes = sorted(resumes)
outfn = 'resume-book.pdf'

writer = PdfWriter()
for resume in resumes:
	if resume.endswith('.pdf'):
		writer.addpages(PdfReader(resume).pages)

writer.write(outfn)