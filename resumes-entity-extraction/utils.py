import re
import os
import json
import glob

import PyPDF2
import docx

def read_pdf(path):
	# creating a pdf file object 
	with open(path, 'rb') as pdf_file:
		pdfReader = PyPDF2.PdfFileReader(pdf_file)
		print(pdfReader.numPages)

		pageObj = pdfReader.getPage(1)

		#print(pageObj.extractText())

		return pageObj.extractText()

def read_docx(path): 
    try:
        doc = docx.Document(path)  # Creating word reader object.
        data = ""
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
            data = '\n'.join(fullText) 
        #print(data)

    except IOError:
        print('There was an error opening the file!')
    return data

def clean_text(text):
	text_new = os.linesep.join([s for s in text.splitlines() if len(s)>1])
	return text_new

if __name__ == '__main__':
	with open('result.json', 'w') as fp:
		fp.write("")
	for filepath in glob.iglob(r'D:/workspace/dataset/IT_resumes/*.docx'):
		print(filepath)
		docx_text = read_docx(filepath)
		docx_text = clean_text(docx_text)
		email_list = re.findall('\S+@\S+', docx_text)
		phone_list = re.findall(r'\+[-()\s\d]+?(?=\s*[+<])', docx_text)
		print(email_list,phone_list)
		with open('result.json', 'a+') as fp:
			json.dump({"text":docx_text}, fp)
			fp.write("\n")
