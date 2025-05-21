'''This code splits a long file into small ones to use them for free plagrism checking. 
No matter the length of the file. This program will split that file into smaller files of 800 words each. '''

#library to convert the docx file to txt for easy operation
import docx2txt  

#Os module to check the directory or to make one for clean management 
import os, os.path

#Following library is to move file from one directory to another, identified with the help of OS library
import shutil

#Following lines of code, import different dependecies of selenium library for automation of Plagiarism-checking
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#Following library and their pre-defined functions helps in copy and pasting of data in the borwser

#for keyboard-like intereaction (for eg: CMD+V while present cursor is at textbox in website)
from pynput.keyboard import Key, Controller 

#The following library copies the data to clipboard that is later used by pynput to paste the data in textbox
import pyperclip    

#time module helps to stop the automation for some time so that there is enough time to load element of website
import time

#Following libraries help to interacti with pdfs, like merging them, making them, adding watermark them or even read them
from fpdf import FPDF
import PyPDF2

#A dependency of selenium browser to have more options while loading the webdriver
options = Options()

#Following lines of code is taken form chat gpt as it is so that the browser window load fast... without these lines, it would take around 4-5minutes for the browser to load
options.add_argument(f'user-data-dir=/Users/tushar/Library/Application Support/Google/Chrome/Default')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

#Following line prevents the driver to automatically close broswer window after finsishing the intended task
options.add_experimental_option("detach", True)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"

windi = []
plag = []

def namefun():
    #Takes the name of the file from the user
    f_name = input("Enter the name of the file you want to split : ") 
    print("!!! WARNING !!! Please ensure that the file exists in the same folder as of this program and shall be named correctly.")
    reply = input("Preass Y/y to continue: ")

    return reply, f_name


while True:
    reply,f_name = namefun()
    with open("Duplichecker-Plagiarism-Report.pdf",'w') as pdfn:
        pass

    folder = f_name
    file_name = f_name

    def conversion():
        try:
            text = docx2txt.process(f_name+'.docx')
            d2txt = f_name+'.txt'
            with open(d2txt, 'w') as cf:
                cf.write(text)
            print("File converted Successfully")
        except:
         print("Sorry! The file could not be converted")
    

    type = input("The file you want to work with is .docx file? : ")
    if type in "yY":
        decision = input("Do you want to convert it into txt file? : ")
        if decision in "yY":
            conversion()
            print("document converted succesfully")
        else:
            print("Sorry the file can not be processed")
            break


    if reply in "yY":
        f_name = f_name + '.txt'
        try:

            #opening file with context manager for ease of method
            with open(f_name,'r') as f:                     
                info = f.read()

                #splits the file with space as splittor and braks the data word by word which we can use with count function to count the number of words.
                words_count = info.split()  
                n_words = len (words_count)   
                print("The number of words in your file is : ", n_words)

                #since we have to work with logical data, files must be spliited by pargarph and '\n\n' depicts paragraph
                para = info.split('\n\n')
                print("Number of paragraph :", len(para))

                # take the max-word limit from user for their convenience
                splitor = int(input("Enter the number of words you want to split files from: "))

                #the following line of code is not necessary but tells the user about the number of file that will be created after splitting the main file
                num_file = n_words/splitor

                #Could it be the file is having more words than rounded off integer then the following lines of code adds an extra file for the remaining words
                if num_file > int(num_file):
                    num_file= int(num_file +1)
                else:
                    num_file= int(num_file)
                n_file = print("Number of files that will be created will be ", num_file)

                buffer=[]  # this is to store the counted paragraphs which are less than splitor but will contribute to the end result
                numwords = 0  # temporary variable that would keep the count So that paragraphs will not be written more than desired
                filenum=0

                for i in para:
                    words_in_para=len(i.split())
                    if (numwords + words_in_para)<splitor:
                        buffer.append(i)
                        numwords+=words_in_para
                            
                    else:
                        nf_name = file_name + str(filenum+1) + '.txt'
                        with open(nf_name, 'w') as nf:
                            nf.write("\n\n".join(buffer) + "\n\n")
                        filenum+=1
                        buffer=[i] # resets the buffer and set the cursor to the next paragraph that is i
                        numwords=words_in_para # reset the Count of number of words in paragraph
                        
                # This snippet Only runs fan buffer is true that is buffer has something in it and is not more than splitter so after ending the loop that is written to the file anyways.
                if buffer:
                    nf_name = file_name + str(filenum + 1) + '.txt'
                    with open(nf_name, 'w') as nf:
                        nf.write("\n\n".join(buffer) + "\n\n")
                    

                print("Files splitted successfully")
            break
        except FileNotFoundError:
            print("The file you named is currently not in the same direcotry as this programm or might be some typo. Please check !!")
            #after the error is displayed, the program will restart automatically 
            continue
    else:
        #continues the loop to ensure the user-friendlt environment
        print("starting over") 


print("Now moving files...")

if not os.path.exists(folder):
    os.makedirs(folder)     

for filename in os.listdir():
    if filename.startswith(file_name) and filename.endswith('.txt'):
        shutil.move(filename, os.path.join(folder, filename))

print(f"Files moved to a folder named {file_name} succesffuly.")

pathforfile=f'/Users/tushar/Documents/GitHub/file_splitter/{folder}/'

frange=0
for ele in os.listdir(pathforfile):
    fpath = os.path.join(pathforfile, ele)
    if os.path.isfile(fpath):
        frange+=1
print(frange)
input()

final_result= input("Since the file is splitted successfully, Do you want to start plag calculation? : ")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(3)

def search():

    namef = f"{pathforfile}{file_name+str(j)}.txt"
    with open(namef, 'r') as readin:
        info = readin.read()
        pyperclip.copy(info)
        count = len(info.split())

    driver.get("https://www.duplichecker.com/")
    time.sleep(5)


    print(f"Result for {folder}-file number{j}")

    driver.maximize_window()

    time.sleep(2)

    paste = driver.find_element(By.ID, 'textBox')
    driver.execute_script("arguments[0].scrollIntoView(true);", paste)
    time.sleep(1)
    paste.click()

    time.sleep(1)
    keyboard = Controller()

    keyboard.press(Key.cmd)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.cmd)

    time.sleep(5)

    print("Enter the Captcha and press any key to continue the automation")
    input()

    check = driver.find_element(By.ID, "form_plag_btn")
    driver.execute_script("arguments[0].scrollIntoView(true);", check)
    time.sleep(1)
    check.click()
    time.sleep(10)
    print("Hit enter once the result is loaded")
    input()
    time.sleep(5)
    plag_report = driver.find_element(By.XPATH, '//*[@id="home"]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/div[1]/div/div/div/p[2]')
    perce = plag_report.text
    nperce = perce.split('%')
    plagpercent = ''.join(nperce)
    plagpercent= int(plagpercent)
    print("plag percentage : ", plagpercent)
    plag.append(plagpercent)
    time.sleep(5)
    button = driver.find_element(By.XPATH, "//form[@id='form_pdf_report']//button[contains(., 'Download PDF Report')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    time.sleep(1)  # wait a bit in case ad disappears on scroll
    button.click()

    time.sleep(10)


    reportfile = f'{folder}-plag-reportfile.txt'
    with open(reportfile,'a') as f:
        Head = f"Plagarism Report of the file {folder} file number {j}:\n"
        pdata = "plag = " + perce + "\n"
        w_ords = f"Number of words : {count} \n"
        windi.append(count)
        fdata = Head + pdata + w_ords
        f.writelines(fdata)

    time.sleep(5)



if final_result in 'yY':
    for j in range (1,frange):
        search()


driver.quit()
print(windi)
print(plag)

pdfs = input('Since the pdf reports from Duplichecker have been downloaded, Do you want to move them into a seperate folder?: ')

if pdfs in 'yY':
    pdffolder='pdffolder'
    if not os.path.exists(pdffolder):
        os.makedirs(pdffolder)     
    for filename in os.listdir():
        if filename.startswith("Duplichecker"):
            shutil.move(filename, os.path.join(pdffolder, filename))

else:
    print("Report pdfs could not be seperated ! ")

sum = 0
for p in range (len(windi)):
    percentage = windi[p]*plag[p]/100
    sum = sum+percentage

pdfin = input("Do you convert this report into pdf? :")

def pdfmaker():
    name = f'{folder}prep.pdf'
    pdf = FPDF()
    pdfs = []

    pdf.add_page()

    pdf.set_font("Arial", size = 30)
    pdf.set_text_color(255, 0, 0)

    pdf.cell(200, 10, txt = f"Plagiarism-Report for {folder.capitalize()}", ln = 1, align = 'C')

    pdf.set_font("Arial", size = 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(200, 10, txt = "By : Tushar Bhardwaj (using duplichecker.com)",ln = 1, align = 'C')
    pdf.cell(0, 10, "", ln=1)
    pdf.cell(0, 10, "", ln=1)
    
    t_plag = round(((sum/n_words)*100),2)
    print("Total plag in file = ", t_plag, "%")
    pdf.cell(0, 10, "", ln=1)
    pdf.cell(0, 10, "", ln=1)
    
    pdf.set_font("Arial", size = 20)
    pdf.set_text_color(255, 0, 0)

    pdf.cell(200, 10, txt = f"Total plag in file = {t_plag} %", ln = 1, align = 'C')

    pdf.set_font("Arial", size = 14)
    pdf.set_text_color(0, 0, 0)
    txtname = f'{folder}-plag-reportfile.txt'
    with open(txtname, 'r') as report:
        for x in report:
            pdf.cell(200, 10, txt = x, ln = 1, align = 'L')

    pdf.output(name)
    pdfs.append(name)
    pwrite = PyPDF2.PdfWriter()
    pmerge = PyPDF2.PdfMerger()
    
    for k in range (1,frange):
        newpdf = f'Duplichecker-Plagiarism-Report ({k}).pdf'
        pathpdf = f'/Users/tushar/Documents/GitHub/file_splitter/pdffolder/{newpdf}'
        pdfs.append(pathpdf)
    
    for pdf in pdfs:
        pmerge.append(pdf)
    
    mergepdf = f'{folder}merged.pdf'
    pmerge.write(mergepdf)
    
    
    w_mark = "watermark.pdf"

    with open(mergepdf,'rb') as main:
        pread = PyPDF2.PdfReader(main)
        

        markpdf = PyPDF2.PdfReader(w_mark)
        markpg = markpdf.pages[0]


        for pg in range (len(pread.pages)):
            
            page = pread.pages[pg]
            page.merge_page(markpg)
            pwrite.add_page(page)
        
        nname = f'/Users/tushar/Desktop/Plag_report/{folder}plag-report.pdf'
        with open(nname, 'wb') as finalpdf:
            pwrite.write(finalpdf)



if pdfin in 'yY':
    pdfmaker()
    
print("Report generated successfully !")

print("Removing additional files")
dpath = '/Users/tushar/Documents/GitHub/file_splitter/pdffolder'
shutil.rmtree(dpath)
print("Deleted all downloaded files from pdf-folder")

os.remove(f'{folder}merged.pdf')
os.remove(f'{folder}prep.pdf')
os.remove(f'{folder}-plag-reportfile.txt')
dpath = f'/Users/tushar/Documents/GitHub/file_splitter/{folder}'
shutil.rmtree(dpath)

print("All additional files delted successfully")




