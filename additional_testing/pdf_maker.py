from fpdf import FPDF
import PyPDF2
import os, os.path

name = input("Enter the name of the final report file : ")


pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", size = 30)
pdf.set_text_color(255, 0, 0)

pdf.cell(200, 10, txt = f"Plagiarism-Report for {name.capitalize()}", ln = 1, align = 'C')

pdf.set_font("Arial", size = 12)
pdf.set_text_color(0, 0, 0)
pdf.cell(200, 10, txt = "By : Tushar Bhardwaj (using duplichecker.com)",ln = 1, align = 'C')
pdf.cell(0, 10, "", ln=1)
pdf.cell(0, 10, "", ln=1)

pdf.set_font("Arial", size = 14)

with open('report.txt', 'r') as report:
    for x in report:
        pdf.cell(200, 10, txt = x, ln = 1, align = 'L')

name = name + '.pdf'
pdf.output(name)

pathforfile = f'/Users/tushar/Documents/GitHub/file_splitter/'
frange=0
for ele in os.listdir(pathforfile):
    fpath = os.path.join(pathforfile, ele)
    if os.path.isfile(fpath):
        frange+=1
pwrite = PyPDF2.PdfWriter()
# for path in pdf_paths:
#     try:
#         pdf_merger.append(path)
#     except Exception as e:
#         print(f"Error appending {path}: {e}")
#         continue
#     with open(output_path, "wb") as output_file:
#         pdf_merger.write(output_file)

w_mark = "watermark.pdf"

with open(name,'rb') as main:
    pread = PyPDF2.PdfReader(main)
    

    markpdf = PyPDF2.PdfReader(w_mark)
    markpg = markpdf.pages[0]


    for pg in range (len(pread.pages)):
        
        page = pread.pages[pg]
        page.merge_page(markpg)
        pwrite.add_page(page)
    
    pname = name.split('.')
    pname.remove('pdf')
    nname = f"{''.join(pname)}-plag-report.pdf"
    with open(nname, 'wb') as finalpdf:
        pwrite.write(finalpdf)




