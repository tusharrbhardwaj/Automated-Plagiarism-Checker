from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import pyperclip
import time

print("hi Tushar here we are testing again")


options = Options()

# Optional: Appear less like a bot
options.add_argument(f'user-data-dir=/Users/tushar/Library/Application Support/Google/Chrome/Default')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("detach", True)

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(3)

j = 1
def search():
    namef = str(j)+'.txt'
    with open(namef, 'r') as readin:
        info = readin.read()
        pyperclip.copy(info)
        count = len(info.split())

    driver.get("https://www.duplichecker.com/")
    time.sleep(5)


    print(f"Result for {namef}")

    driver.maximize_window()

    time.sleep(2)

    paste = driver.find_element(By.ID, 'textBox')

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
    check.click()
    time.sleep(10)
    print("Hit enter once the result is loaded")
    input()
    time.sleep(5)
    plag_report = driver.find_element(By.XPATH, '//*[@id="home"]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/div[1]/div/div/div/p[2]')
    perce = plag_report.text
    print("plag = ", perce)

    time.sleep(5)
    button = driver.find_element(By.XPATH, "//form[@id='form_pdf_report']//button[contains(., 'Download PDF Report')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    time.sleep(1)  # wait a bit in case ad disappears on scroll
    button.click()

    time.sleep(10)



    with open("report",'a') as f:
        Head = f"Plagarism Report of the file {namef}:\n"
        pdata = "plag = " + perce + "\n"
        # Unique = 100-int(perce)
        # udata = "Unique = " + str(Unique)+ "\n"
        w_ords = f"Number of words : {count} \n"
        fdata = Head + pdata + w_ords
        f.writelines(fdata)

    time.sleep(5)
    


    

for i in range (8):
    search()
    j+=1
    driver.switch_to.new_window('tab')











